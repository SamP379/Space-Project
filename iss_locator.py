import requests
from geopy.geocoders import Nominatim


def get_iss_position(api_endpoint: str) -> tuple:
    """Returns the longitude and latitude of the International Space Station"""
    try:
        response = requests.get(url=api_endpoint)
        content = response.json()
        iss_position = content["iss_position"]
        return (iss_position["longitude"], iss_position["latitude"])
    except Exception as error:
        print(f"An error occurred: {error}")
        return None


def get_coordinates(address : str) -> tuple:
    """Returns the longitude and latitude of a given address"""
    geolocator = Nominatim(user_agent = "my_locator")
    location = geolocator.geocode(address)
    coordinates = location[-1]