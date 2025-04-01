import requests
from geopy.geocoders import Nominatim

ISS_ENDPOINT = "http://api.open-notify.org/iss-now.json"


def get_iss_position(api_endpoint: str) -> tuple:
    """Returns a tuple which holds the latitude and longitude of the International Space Station
       RETURNS LONGTITUDE FIRST AND THEN LAT"""
    try:
        response = requests.get(url = api_endpoint)
        content = response.json()
        iss_position = content["iss_position"]
        return (iss_position["longitude"], iss_position["latitude"])
    except Exception as error:
        print(f"An error occurred: {error}")
        return None


def get_coordinates(address : str) -> tuple:
    """Returns a tuple which holds the latitude and longitude of an address given as a string"""
    geolocator = Nominatim(user_agent = "locator")
    location = geolocator.geocode(address)
    coordinates = location[-1]
    return coordinates


from math import cos, asin, sqrt, pi

def haversine_distance(coordinates1 : tuple, coordinates2 : tuple):
    lat1 = coordinates1[0]
    lon1 = coordinates1[1]
    lat2 = coordinates2[0]
    lon2 = coordinates2[1]

    r = 6371 # km
    p = pi / 180

    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    return 2 * r * asin(sqrt(a))







# https://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula