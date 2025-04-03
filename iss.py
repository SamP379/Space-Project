"""
import time
import requests


class ISS:

    API_ENDPOINT = "http://api.open-notify.org/iss-now.json"

    
    def __init__(self):
        self._position = self.get_latest_position()
        self._speed = self.get_latest_speed()
    
        
    def get_latest_position(self):
        try:
            response = requests.get(url = ISS.API_ENDPOINT)
            content = response.json()
            iss_position = (float(content["iss_position"]["latitude"]), float(content["iss_position"]["longitude"]))
            return iss_position
        except Exception as error:
            print(f"\nAn error occurred, unable to locate the ISS.\n")
            return None
    
            
    def update_position(self):
        self._position = self.get_latest_position()
    
        
    def get_position(self):
        return self._position
    
        
    def get_latest_speed(self):
        position1 = self.get_latest_position()
        timestamp1 = time.time()
        time.sleep(5)
        position2 = self.get_latest_position()
        timestamp2 = time.time()
        if position1 or position2 is None:
            return None
        else:
            distance_km = distance.haversine(iss_position1, iss_position2)
            time_secs = timestamp2 - timestamp1
            speed = distance_km / time_secs
            return round(speed)






import time
import distance


class ISS:

    API_ENDPOINT = "http://api.open-notify.org/iss-now.json"

    def __init__(self):
        self.position
        self.speed
    
        
    def was_found(self):
        return self.position is not None and self.speed is not None
    
        
    def display_status(self):
        if self.was_found():
            print("Locating the position of the International Space Station...")
            time.sleep(3)
            print(f"The position of the International Space Station is: {self.position})
            print(f"It is moving at a speed of about {self.speed} km per second")
        else:
            print("Unable to locate the ISS")
    
            
    def distance_between(self, second_position):
        if self.was_found():
            print("Calculating distance...")
            time.sleep(3)
            distance_km = distance.haversine(self.position, second_position)
            print(f"The International Space Station is about {distance_km} km from you")
        else:
            print("Unable to locate the ISS)


    
"""