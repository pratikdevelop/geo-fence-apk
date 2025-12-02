from geopy.distance import geodesic

def is_outside_geofence(current_lat, current_lon, center_lat, center_lon, radius_m):
    """
    Check if current position is outside the geo-fence using Haversine formula.
    Returns: (is_outside: bool, distance: float in meters)
    """
    current_point = (current_lat, current_lon)
    center_point = (center_lat, center_lon)
    
    distance = geodesic(current_point, center_point).meters
    return distance > radius_m, distance