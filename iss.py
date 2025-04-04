"""


import time
import distance
import requests


class ISS:

    ENDPOINT = "http://api.open-notify.org/iss-now.json"

    
    def __init__(self):
        self.position = self.get_new_position()
        self.timestamp = time.time()
        self.speed = self.get_speed()
    
    
    def get_new_position(self):
        try:
            response =  requests.get(url = ISS.ENDPOINT)
            content = response.json()
            iss_position = (float(content["iss_position"]["latitude"]), float(content["iss_position"]["longitude"]))
            return iss_position
        except Exception as error:
            print(f"An Error occured: {error}")
            return None
    
            
    def get_speed(self):
        new_position = self.get_new_position()
        new_timestamp = time.time()
        if self.position is not None and new_position is not None:
            distance_km = distance.haversine(self.position, new_position)
            time_secs = new_timestamp - self.timestamp
            speed_km = distance_km / time_secs
            return round(speed_km)
        else:
            return None
    

    def update_position(self):
        self.position = self.get_new_position()
        self.timestamp = time.time()
    
    
    def was_found(self):
        return self.position is not None and self.speed is not None
    
        
    def display_status(self):
        if self.was_found():
            print("Locating the position of the International Space Station...")
            time.sleep(4)
            print(f"The position of the International Space Station is: {self.position}")
            print(f"It is moving at a speed of about {self.speed} km per second")
        else:
            print("Unable to locate the ISS")
            
            

            
"""