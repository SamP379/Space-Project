"""


import os
import dotenv
import requests


class APOD:

    def __init__(self):
        dotenv.load_dotenv()
        self.file_path = "apod.jpg"
        self.api_key = os.getenv("NASA_API_KEY") 
        self.endpoint = "https://api.nasa.gov/planetary/apod"
        self.image_url = self.get_image_url()

        
    def get_image_url():
        payload = {"api_key" : self.api_key}
        try:
            response = requests.get(url = self.endpoint, params = payload)
            content = response.json()
            image_url = content["hdurl"]
            return image_url
        except Exception as error:
            print(f"An error occured: {error}")
        return None
    
        
    def save_image():
        response = requests.get(url = self.image_url)
        image_bytes = response.content
        with open(self.file_path, mode = "wb") as file:
            file.write(image_bytes)


"""