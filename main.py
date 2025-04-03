"""

import time
import requests
import distance
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


def get_iss_speed():
    iss_position1 = get_iss_position(ISS_ENDPOINT)
    timestamp1 = time.time()
    time.sleep(5)
    iss_position2 = get_iss_position(ISS_ENDPOINT)
    timestamp2 = time.time()
    if iss_position1 is None or iss_position2 is None:
        return None
    else:
        distancekm = distance.haversine(iss_position1, iss_position2)
        time_secs = timestamp2 - timestamp1
        speed = distancekm / time_secs
        return round(speed)





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
        distance = distance.haversine(user_position, iss_position)
        speed = get_iss_speed()
        print(f"The International Space Station is about {distance} km from you")
        if speed is not None:
            print(f"It is travelling at a speed of about {speed} km per second\n")"""