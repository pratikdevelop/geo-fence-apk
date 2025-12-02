[app]
title = GeoFence Tracker
package.name = geofencetracker
package.domain = org.pratik

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt

version = 1.0
requirements = python3,kivy==2.2.1,plyer,requests,geopy,folium,pywebview,openssl

[buildozer]
log_level = 2

[app]
android.permissions = INTERNET,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,ACCESS_BACKGROUND_LOCATION,FOREGROUND_SERVICE
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.arch = arm64-v8a
orientation = portrait
fullscreen = 0

[buildozer]
warn_on_root = 1