import os
import cv2
import dotenv
import requests


class APOD:

    dotenv.load_dotenv()
    API_KEY = os.getenv("NASA_API_KEY") 
    ENDPOINT = "https://api.nasa.gov/planetary/apod"

    
    def __init__(self):
        self.was_loaded = False
        self.url = self.get_url()
        self.file_path = "apod.jpg"
        self.save_image()

        
    def get_url(self):
        payload = {"api_key" : APOD.API_KEY}
        try:
            response = requests.get(url = APOD.ENDPOINT, params = payload)
            content = response.json()
            image_url = content["hdurl"]
            return image_url
        except Exception as error:
            print(f"An error occured: {error}")
        return None
    
        
    def save_image(self):
        if self.url is not None:
            try:
                response = requests.get(url = self.url)
                image_bytes = response.content
                with open(self.file_path, mode = "wb") as file:
                    file.write(image_bytes)
                    self.was_loaded = True
            except Exception as error:
                print("An error occured: {error}")
            

    def display(self):
        if self.was_loaded:
            image = cv2.imread(self.file_path)
            cv2.imshow("APOD", image)
            cv2.waitKey(0)
        else:
            print("Unable to load image")