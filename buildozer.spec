[app]

# (str) Title of your application
title = GeoFence Tracker

# (str) Package name
package.name = geofencetracker

# (str) Package domain (needed for android/ios packaging)
package.domain = org.pratik

# (str) Source files to include (let blank to include all the files)
source.dir = .

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin

# (list) Application requirements
requirements = python3,kivy==2.2.1,plyer,requests,geopy,folium,pywebview,openssl

# (str) Application versioning (method 1)
version = 1.0

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) Permissions
android.permissions = INTERNET,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,ACCESS_BACKGROUND_LOCATION

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (list) Pattern to whitelist for the whole project
#android.whitelist_src =

# (bool) Indicate if the application should be fullscreen
fullscreen = 1

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (str) Path to build artifact storage, absolute or relative to .buildozer
#build_dir = .buildozer
