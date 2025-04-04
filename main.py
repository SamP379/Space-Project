
"""


def main():

    user_address = input("Enter your address: ")
    user = User(user_address)
    user.display_position()
    
    iss = ISS()
    iss.display_status()
   

"""


# Enter your address: 47 Chipping Vale, Emerson Valley, Milton Keynes
# Locating your position...
# Your position is: (53.234, -723434)
     
# Locating the position of the International Space Station...
# The position of the International Space Station is: (3.1224, -1.1324)
# The International Space Station is somewhere over Ohio, USA
     
# Calculating distance...
# The International Space Station is about 4320 KM from you