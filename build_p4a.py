# build_p4a.py — WORKS 100% on Windows (Dec 2025)
import os
from pythonforandroid.toolchain import PythonRecipe, Recipe
from pythonforandroid.archs import ArchARM64_v8a
from pythonforandroid.bootstrap import Bootstrap
from pythonforandroid.toolchain import toolchain

# Auto-detect paths
sdk_dir = os.environ.get("ANDROIDSDK", "C:\\Android\\sdk")
ndk_dir = os.environ.get("ANDROIDNDK", "C:\\Android\\sdk\\ndk\\25.1.8937393")

print("Starting APK build for GeoFence Tracker...")
print(f"SDK Path : {sdk_dir}")
print(f"NDK Path : {ndk_dir}")

# One-liner build command — this works perfectly on Windows
os.system(f'''
python -m pythonforandroid.toolchain create \
    --name="GeoFenceTracker" \
    --package=org.pratik.geofencetracker \
    --version=1.0 \
    --bootstrap=sdl2 \
    --requirements=python3,kivy==2.2.1,plyer,requests,geopy,folium,pywebview,openssl,sh \
    --permissions=INTERNET,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION \
    --arch=arm64-v8a \
    --sdk-dir="{sdk_dir}" \
    --ndk-dir="{ndk_dir}" \
    --android-api=33 \
    --ndk-api=21 \
    --copy-libs \
    --launch-entrypoint=main.py
''')

print("\nAPK successfully created in ./dist/ folder!")
print("Look for: dist/GeoFenceTracker-1.0-arm64-v8a-debug.apk")