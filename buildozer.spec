[app]

# App info
title = GeoFence Tracker
package.name = geofencetracker
package.domain = org.pratik

# Source
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt,html,js,css

# Version
version = 1.0

# ONLY COMPATIBLE PACKAGES (folium & pywebview REMOVED!)
requirements = python3,kivy==2.2.1,plyer,requests,geopy,openssl

# Orientation & fullscreen
orientation = portrait
fullscreen = 1

# Permissions (GPS + internet)
android.permissions = INTERNET,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,ACCESS_BACKGROUND_LOCATION,FOREGROUND_SERVICE

# Android API levels
android.api = 33
android.minapi = 21
android.ndk = 25b

# (Optional) Add icon later
# icon.filename = icon.png
# presplash.filename = splash.png

[buildozer]

# Debug logs (very helpful)
log_level = 2

# Warn if running as root (not needed on GitHub)
warn_on_root = 0
