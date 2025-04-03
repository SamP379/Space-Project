"""import requests


class ISS:

    API_ENDPOINT = "http://api.open-notify.org/iss-now.json"

    
    def __init__(self):
        self._position = self.get_latest_position()
    
        
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

"""