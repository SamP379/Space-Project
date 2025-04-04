"""

    
class SpaceWatch:

    def __init__(self):
        self.menu_choice = None
        self.commands = {}
    
        
    def display_menu(self):
        print("1. Track the ISS")
        print("2. How many people are in space?")
        print("3. Timeline of space exploration)
    
        
    def get_menu_choice(self):
        choice = input("Enter choice: ")
        self.menu_choice = choice
    
        
    def handle_menu_choice(self):
        if self.choice == "track the iss":
            iss.iss_routine()
        
    
    def main_loop(self):
        self.display_menu()
        self.get_menu_choice()
        self.handle_menu_choice()



"""