from plyer import gps
import time

# Enable GPS (request permission on first run)
gps.configure(on_location=lambda **kwargs: globals().update(kwargs))  # Global for location

def get_gps():
    """
    Get GPS on Android via Plyer. Falls back to mock for testing.
    """
    try:
        gps.start(minTime=1000, minDistance=1)  # Start GPS service
        time.sleep(1)  # Wait for fix
        if 'lat' in globals() and 'lon' in globals():
            gps.stop()
            return globals()['lat'], globals()['lon']
        gps.stop()
        return None, None
    except NotImplementedError:
        # Mock for non-Android testing
        center_lat, center_lon = 23.0205, 72.5714
        offset = 0.003 * abs((time.time() % 60 - 30) / 30)
        import random
        return center_lat + offset + random.uniform(-0.00005, 0.00005), center_lon + random.uniform(-0.00005, 0.00005)