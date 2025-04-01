import os
import cv2
import ctypes
import dotenv
import requests


# Load environment variables
dotenv.load_dotenv()


APOD_ENDPOINT = "https://api.nasa.gov/planetary/apod"
NASA_API_KEY = os.getenv("NASA_API_KEY")
APOD_FILE_PATH = "apod.jpg"


# Check API key correctly loaded
if not NASA_API_KEY:
    print("Error loading API key...")
    exit(1)


def get_image_url():
    payload = {"api_key" : NASA_API_KEY}
    try:
        response = requests.get(url = APOD_ENDPOINT, params = payload)
        content = response.json()
        image_url = content["hdurl"]
        return image_url
    except requests.exceptions.RequestException as error:
        print(f"A requests error occured...")
    return None


def save_image(image_url : str):
    """Gets an image from a given url using requests and saves it to a file called 'apod.jpg'"""
    response = requests.get(url = image_url)
    image_bytes = response.content
    with open(APOD_FILE_PATH, mode = "wb") as file:
        file.write(image_bytes)


def change_wallpaper(path : str):
    style = 0
    SPI_SETDESKWALLPAPER = 20
    image = ctypes.c_wchar_p(path)
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image, style)



def main():
    image_url = get_image_url()
    save_image(image_url)
    wallpaper_path = r"C:\Users\sampa\Documents\Programming\Python\Projects\image-of-the-day-NASA\apod.jpg"
    change_wallpaper(wallpaper_path)
   
    



main()