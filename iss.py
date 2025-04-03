"""

import time
import distance
import requests


class ISS:

    API_ENDPOINT = "http://api.open-notify.org/iss-now.json"

    
    def __init__(self):
        self.position = self.get_new_position()
        self.timestamp
        self.speed = self.get_speed()
    
    
    def get_new_position(self):
        try:
            response =  requests.get(url = ISS.ENDPOINT)
            content = response.json()
            iss_position = (float(content["iss_position"]["latitude"]), float(content["iss_position"]["longitude"]))
            return iss_position
        except Exception as error:
            print("\nAn Error occured, unable to locate the ISS.\n)
            return None
        
    
    def was_found(self):
        return self.position is not None and self.speed is not None
    
        
    def get_speed(self):
        new_iss = ISS()
        if self.was_found() and new_iss.was_found():
            distance_km = distance.haversine(self.position, new_iss.get_position())
            time_secs = new_iss.get_timestamp() - self.timestamp
            speed = distance_km / time_secs
            return round(speed)
        else:
            return None

        
    def display_status(self):
        if self.was_found():
            print("Locating the position of the International Space Station...")
            time.sleep(3)
            print(f"The position of the International Space Station is: {self.position})
            print(f"It is moving at a speed of about {self.speed} km per second")
        else:
            print("Unable to locate the ISS")

"""