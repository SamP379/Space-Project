import os
import cv2
import dotenv
import requests


class APOD:
    """A class to represent an Astronomy Picture of The Day. An APOD is a daily
    picture released by NASA, and can be obtained using the APOD API. This class
    represents the current APOD."""

    dotenv.load_dotenv()
    API_KEY = os.getenv("NASA_API_KEY") 
    ENDPOINT = "https://api.nasa.gov/planetary/apod"

    
    def __init__(self):
        self.was_loaded = False
        self.url = self.get_url()
        self.file_path = "apod.jpg"
        self.save_image()

        
    def get_url(self):
        """Gets the url of the apod image from NASA's APOD api"""
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
        """Gets the apod image if the url was found and writes it to a file"""
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
        """Displays the apod image using the cv2 library, if it was loaded"""
        if self.was_loaded:
            image = cv2.imread(self.file_path)
            cv2.imshow("APOD", image)
            cv2.waitKey(0)
        else:
            print("Unable to load image")