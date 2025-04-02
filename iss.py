import requests
from geopy.geocoders import Nominatim


ISS_ENDPOINT = "http://api.open-notify.org/iss-now.json"


def get_iss_position(api_endpoint: str) -> tuple:
    """Returns a tuple which holds the latitude and longitude of the International Space Station"""
    try:
        response = requests.get(url = api_endpoint)
        content = response.json()
        iss_position = (float(content["iss_position"]["latitude"]), float(content["iss_position"]["longitude"]))
        return iss_position
    except Exception as error:
        print(f"An error occurred: {error}")
        return None


def get_position(address : str) -> tuple:
    """Returns a tuple which holds the latitude and longitude of an address given as a string"""
    geolocator = Nominatim(user_agent = "locator")
    location = geolocator.geocode(address)
    position = location[-1]
    return position


# Get the address of a given set of coordinates
def get_address(position : str):
    geolocator = Nominatim(user_agent = "locator")
    location = geolocator.reverse(position)
    address = location.address
    return address


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




"""

Sample output:

    Enter your address: 47 Chipping Vale, Emerson Valley, Milton Keynes
    Locating your position...
    Your position is: (53.234, -723434)
    
    Locating the position of the International Space Station...
    The position of the International Space Station is: (3.1224, -1.1324)
    The International Space Station is somewhere over Ohio, USA
    
    Calculating distance...
    The International Space Station is about 4320 KM from you


    

ISS MODULE




def locate_user():
    user_address = input("Enter your address: ")
    print("Locating your position...")
    user_position = get_address_position(user_address)
    if user_position is None:
        return None
    else:
        print("Your position is: {user_position})
        return user_position


find_distance():

    user_position = locate_user()
    iss_position = locate_iss()

    if user_position is None or iss_position is None:
        print("An error occured. Please try again later)
    else:
        print("Calculating distance...")
        distance = haversine_distance(user_position, iss_position)
        print(f"The International Space Station is about {distance} KM from you)

        


"""