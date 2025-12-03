[app]

# App info
title = GeoFence Tracker
package.name = geofencetracker
package.domain = org.pratik

# Source
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt

# Version
version = 1.0

# FIXED REQUIREMENTS (openssl removed – causes toolchain crash)
requirements = python3,kivy==2.2.1,plyer,requests,geopy

# Orientation & fullscreen
orientation = portrait
fullscreen = 1

# Permissions (GPS + internet)
android.permissions = INTERNET,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,ACCESS_BACKGROUND_LOCATION,FOREGROUND_SERVICE

# Android API levels
android.api = 33
android.minapi = 21
android.ndk = 25b
android.arch = arm64-v8a  # Single arch for stability (faster build, modern phones)

[buildozer]

# Debug logs
log_level = 2

# Ignore root warning (GitHub runner)
warn_on_root = 0
