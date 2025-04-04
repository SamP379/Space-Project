import time 
import geo_utils

class User:

    def __init__(self, address : str):
        self.address = address
        self.position = geo_utils.get_position(address)
    
    def was_found(self):
        return self.position is not None
    
    def display_positon(self):
        print("Locating your position...")
        time.sleep(4)
        if self.was_found():
            print(f"Your position is: {self.position}")
        else:
            print("Unable to locate your position")
