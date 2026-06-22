from LoginValidation import validation
from LoginException import LoginUserError,LoginPasswordError
while(True):
    try:
        user=input("Enter User Name:")
        password=input("Enter your Password:")
        validation(user,password)
    except LoginUserError:
        print("{} invalid user name:".format(user))
    except LoginPasswordError:
        print("{} invalid password:".format(password))
    else:
        ch=input("\nDo you want to login with another details (yes/no):")
        if(ch.lower()=="no"):
            print("Thanks for this program")
            break