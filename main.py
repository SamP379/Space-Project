from iss import ISS
from user import User


def main():
    iss = ISS()
    print("")
    user_address = input("Enter your address: ")
    user = User(user_address)
    user.display_position()
    iss.display_status()
    iss.display_distance(user.get_position()) 


if __name__ == "__main__":
    main()