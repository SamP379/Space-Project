from iss import ISS
from user import User


def iss_routine():
    iss = ISS()
    user_address = input("Enter your address: ")
    user = User(user_address)
    user.display_position()
    iss.display_status()
    iss.display_distance(user.get_position())  