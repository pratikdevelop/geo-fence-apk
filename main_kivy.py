from gps_reader import get_gps
from geo_fence import is_outside_geofence
from alerts import send_email_alert, telegram_alert, sms_alert
import config
import time

is_outside_before = False

print("🚀 Geo-Fence System Started (CLI Mode)…")

while True:
    lat, lon = get_gps()
    if lat is None or lon is None:
        print("❌ GPS signal lost. Retrying...")
        time.sleep(5)
        continue

    print(f"📍 Current Location: {lat:.6f}, {lon:.6f}")

    is_outside, distance = is_outside_geofence(
        lat, lon,
        config.FENCE_LAT,
        config.FENCE_LON,
        config.RADIUS_M
    )

    print(f"📏 Distance from center: {distance:.2f} m")

    if is_outside and not is_outside_before:
        msg = f"⚠️ ALERT: Device exited geofence! 📍 {lat:.6f}, {lon:.6f} | {distance:.1f}m"
        print(msg)
        send_email_alert(msg)
        telegram_alert(msg)
        sms_alert(msg)

    if not is_outside and is_outside_before:
        msg = "✔️ Device re-entered safe zone."
        print(msg)
        telegram_alert(msg)

    is_outside_before = is_outside
    time.sleep(5)