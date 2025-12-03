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

# FIXED REQUIREMENTS (no openssl/geopy issues)
requirements = python3,kivy==2.2.1,plyer,requests,geopy

# Orientation & fullscreen
orientation = portrait
fullscreen = 1

# Permissions (GPS + internet)
android.permissions = INTERNET,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,ACCESS_BACKGROUND_LOCATION,FOREGROUND_SERVICE

# Android API levels (minapi=24 fixes Ubuntu 24.04 toolchain crashes)
android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a  # Plural 'archs' – fixes warning

[buildozer]

# Debug logs
log_level = 2

# Ignore root warning (GitHub runner)
warn_on_root = 0
