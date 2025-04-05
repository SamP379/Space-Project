
import iss
from apod import APOD
    
class SpaceWatch:

    def __init__(self):
        self.menu_choice = None 
        self.apod = APOD()
        

    def display_menu(self):
        print("\n1. Track the ISS")
        print("2. Get NASA's Astronomy Picture of the Day\n")
    
        
    def get_menu_choice(self):
        choice = input("Enter choice: ")
        self.menu_choice = choice
    
        
    def handle_menu_choice(self):
        if self.menu_choice == "iss":
            iss.iss_routine()
        elif self.menu_choice == "apod":
            self.apod.display()
        
    
    def main_loop(self):
        while True:
            self.display_menu()
            self.get_menu_choice()
            self.handle_menu_choice()