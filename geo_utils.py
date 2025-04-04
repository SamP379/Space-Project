
from geopy.geocoders import Nominatim

def get_position(address : str):
    geolocator = Nominatim(user_agent = "locator")
    location = geolocator.geocode(address)
    if location is None:
        return None
    position = location[-1]
    return position