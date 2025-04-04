
from iss import ISS
from user import User



def iss_routine():
    
    iss = ISS()
    print("")
    user_address = input("Enter your address: ")
    user = User(user_address)

    user.display_position()
    iss.display_status()
     
    # Calculating distance...
    # The International Space Station is about 4320 KM from you



def main():
    iss_routine()

    
   
main()