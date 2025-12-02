import tkinter as tk
from tkinter import ttk, scrolledtext
import threading
import time
import os
import webview  # ← NEW: For embedding the map
from gps_reader import get_gps
from geo_fence import is_outside_geofence
from alerts import telegram_alert
import config
from datetime import datetime

# For map generation
import folium

class GeoFenceApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🚨 Real-time GPS Geo-Fence Monitor")
        self.root.geometry("1200x700")
        self.root.configure(bg="#2b2b2b")

        self.is_outside_before = False
        self.map_file = "map.html"
        self.window = None  # ← NEW: Webview window

        self.create_map()
        self.setup_ui()
        self.start_gps_thread()

    def create_map(self):
        """Initial map with geo-fence."""
        m = folium.Map(location=[config.FENCE_LAT, config.FENCE_LON], zoom_start=17)
        
        # Geo-fence circle
        folium.Circle(
            location=[config.FENCE_LAT, config.FENCE_LON],
            radius=config.RADIUS_M,
            color="#ff0000",
            fill=True,
            fill_opacity=0.2,
            popup="GEO-FENCE BOUNDARY"
        ).add_to(m)

        # Center marker
        folium.Marker(
            [config.FENCE_LAT, config.FENCE_LON],
            popup="Safe Zone Center",
            icon=folium.Icon(color="green", icon="home")
        ).add_to(m)

        m.save(self.map_file)

    def setup_ui(self):
        # Top: Map Embed (NEW: Full screen embed)
        # We'll use webview to embed – but for Tkinter fallback, add a frame
        frame_map = tk.Frame(self.root, bg="white")
        frame_map.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Button to toggle embedded map (NEW)
        btn_embed = tk.Button(frame_map, text="🗺️ Load Embedded Map (Inside Window)", 
                              command=self.open_embedded_map,
                              bg="#2196F3", fg="white", font=("Arial", 12, "bold"))
        btn_embed.pack(pady=10)

        # Placeholder label until map loads
        self.map_label = tk.Label(frame_map, text="Click button above to load interactive map here!", 
                                  font=("Arial", 12), fg="gray", bg="white")
        self.map_label.pack(expand=True)

        # Right: Logs & Status (same as before)
        frame_right = tk.Frame(self.root, width=400, bg="#2b2b2b")
        frame_right.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)
        frame_right.pack_propagate(False)

        tk.Label(frame_right, text="📍 Live GPS Tracker", font=("Arial", 16, "bold"), 
                 fg="#00ff00", bg="#2b2b2b").pack(pady=10)

        self.status_label = tk.Label(frame_right, text="Status: Waiting for GPS...", 
                                     font=("Arial", 12), fg="yellow", bg="#2b2b2b")
        self.status_label.pack(pady=5)

        self.log_text = scrolledtext.ScrolledText(frame_right, height=25, bg="#1e1e1e", fg="#00ff00", font=("Consolas", 10))
        self.log_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def open_embedded_map(self):
        """NEW: Open map in embedded webview window (same app)."""
        # Create a new window for the map (resizable, interactive)
        self.window = webview.create_window(
            "🗺️ Live Geo-Fence Map", 
            self.map_file, 
            width=800, 
            height=600,
            resizable=True,
            on_top=True  # Keeps it above the main window
        )
        webview.start(debug=False)  # Starts the embedded browser

    def log(self, msg):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_text.insert(tk.END, f"[{timestamp}] {msg}\n")
        self.log_text.see(tk.END)

    def update_map_marker(self, lat, lon):
        """Regenerate map with current position marker (same as before)."""
        m = folium.Map(location=[lat, lon], zoom_start=18)
        
        # Fence circle (color based on status)
        circle_color = "#ff0000" if self.is_outside_before else "#00ff00"
        folium.Circle(
            location=[config.FENCE_LAT, config.FENCE_LON],
            radius=config.RADIUS_M,
            color=circle_color,
            weight=3,
            fill=True,
            fill_opacity=0.2,
            popup="Geo-Fence Boundary"
        ).add_to(m)

        # Current position marker
        icon_color = "red" if self.is_outside_before else "blue"
        folium.Marker(
            [lat, lon],
            popup=f"Current Position\nLat: {lat:.6f}\nLon: {lon:.6f}",
            icon=folium.Icon(color=icon_color, icon="car", prefix="fa")
        ).add_to(m)

        # Center marker
        folium.Marker(
            [config.FENCE_LAT, config.FENCE_LON],
            popup="Safe Zone Center",
            icon=folium.Icon(color="green", icon="home")
        ).add_to(m)

        m.save(self.map_file)
        
        # NEW: If embedded window is open, reload it
        if self.window:
            self.window.load_url(f"file://{os.path.abspath(self.map_file)}")

    def gps_loop(self):
        while True:
            try:
                lat, lon = get_gps()
                if lat is None or lon is None:
                    self.log("❌ GPS signal lost.")
                    time.sleep(3)
                    continue

                is_outside, distance = is_outside_geofence(
                    lat, lon, config.FENCE_LAT, config.FENCE_LON, config.RADIUS_M
                )

                status = "OUTSIDE GEOFENCE! ⚠️" if is_outside else "Inside Safe Zone ✔️"
                color = "red" if is_outside else "lightgreen"
                self.status_label.config(
                    text=f"Status: {status}\nDistance: {distance:.1f}m", 
                    fg=color
                )

                self.update_map_marker(lat, lon)
                self.log(f"📍 {lat:.6f}, {lon:.6f} | {distance:.1f}m | {status}")

                if is_outside and not self.is_outside_before:
                    msg = f"⚠️ ALERT: Device LEFT geo-fence!\n📍 {lat:.6f}, {lon:.6f}\nDistance: {distance:.1f}m"
                    self.log(msg)
                    threading.Thread(target=telegram_alert, args=(msg,)).start()

                if not is_outside and self.is_outside_before:
                    msg = "✔️ Device returned to safe zone."
                    self.log(msg)
                    threading.Thread(target=telegram_alert, args=(msg,)).start()

                self.is_outside_before = is_outside

            except Exception as e:
                self.log(f"Error: {e}")

            time.sleep(3)

    def start_gps_thread(self):
        thread = threading.Thread(target=self.gps_loop, daemon=True)
        thread.start()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = GeoFenceApp()
    app.run()