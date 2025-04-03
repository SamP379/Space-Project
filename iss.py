

import time
import requests
from math import cos, asin, sqrt, pi
from geopy.geocoders import Nominatim


ISS_ENDPOINT = "http://api.open-notify.org/iss-now.json"


def get_address_position(address : str):
    geolocator = Nominatim(user_agent = "locator")
    location = geolocator.geocode(address)
    if location is None:
        return None
    position = location[-1]
    return position


def locate_user():
    print("") # TODO Fix this bug
    user_address = input("Enter your address: ")
    print("Locating your position...")
    time.sleep(4)
    user_position = get_address_position(user_address)
    if user_position is None:
        print("Unable to find your position.")
        return None
    else:
        print(f"Your position is: {user_position}")
        return user_position
    

def get_iss_position(endpoint: str) -> tuple:
    try:
        response = requests.get(url = endpoint)
        content = response.json()
        iss_position = (float(content["iss_position"]["latitude"]), float(content["iss_position"]["longitude"]))
        return iss_position
    except Exception as error:
        print(f"An error occurred, unable to locate the ISS.")
        return None


def locate_iss():
    print("\nLocating the position of the International Space Station...")
    time.sleep(4)
    iss_position = get_iss_position(ISS_ENDPOINT)
    if iss_position is None:
        return None
    else:
        print(f"The position of the International Space Station is: {iss_position}")
        # TODO "The International Space Station is somewhere over Ohio, USA"
        return iss_position

        
# def get_iss_speed():
#     Get the position of the ISS
#     Create a time variable of the seconds passed since the epoch
#     Create a time delay of about 5 seconds
#     Get the position of the ISS again
#     Create a second time variable of the seconds passed since the epoch

 
def haversine_distance(position1 : tuple, position2 : tuple):
    # https://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula
    lat1 = position1[0]
    lon1 = position1[1]
    lat2 = position2[0]
    lon2 = position2[1]    
    r = 6371 
    p = pi / 180
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    return round(2 * r * asin(sqrt(a)))


def find_distance():

    user_position = locate_user()
    if user_position is None:
        return

    iss_position = locate_iss()
    if iss_position is None:
        return

    else:
        print("\nCalculating distance...")
        time.sleep(4)
        distance = haversine_distance(user_position, iss_position)
        print(f"The International Space Station is about {distance} km from you\n")
        

find_distance()