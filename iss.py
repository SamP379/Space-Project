"""




import time
import requests
import geo_utils


class ISS:

    #ENDPOINT = "http://api.open-notify.org/iss-now.json"
    ENDPOINT = "http://api.open-notiasdsfy.org/iss-now.json"

    
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
            print(f"An Error occured: {error}") # TODO Change this when code is finished
            return None
    
            
    def get_speed(self):
        new_position = self.get_new_position()
        new_timestamp = time.time()
        if self.position is not None and new_position is not None:
            distance_km = geo_utils.haversine_distance(self.position, new_position)
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
    
            
    def display_distance(self, compare_position : tuple):
        if self.was_found() and compare_position is not None:
            print("Calculating distance...")
            time.sleep(4)
            distance = geo_utils.haversine_distance(self.position, compare_position)
            print(f"The International Space Station is about {distance} km from you")
        else:
            print("Unable to locate both positions")
            

            
"""