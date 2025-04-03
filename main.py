
"""



import time
import distance




def main():

    user_position = (52.003854, -0.776971)

    iss = ISS()

    if iss.was_found():
        iss.display_status()
        distance = self.calculate_distance()
        iss.distance_between()
    else:
        print("Unable to locate the ISS")
            

         
"""




# Enter your address: 47 Chipping Vale, Emerson Valley, Milton Keynes
# Locating your position...
# Your position is: (53.234, -723434)
     
# Locating the position of the International Space Station...
# The position of the International Space Station is: (3.1224, -1.1324)
# The International Space Station is somewhere over Ohio, USA
# It is moving at a speed of about 7 km per second
     
# Calculating distance...
# The International Space Station is about 4320 KM from you