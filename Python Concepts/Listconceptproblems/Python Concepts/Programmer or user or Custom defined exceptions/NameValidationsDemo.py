from NameExceptions import InvalidNameError,ZeroLengthNameError,SpaceError
from NameValidations import validate
try:
    name=input("Enter your name:")
    res=validate(name)
except InvalidNameError:
    print("{} is Invalid Name".format(name))
except ZeroLengthNameError:
    print("Try to Enter your Name")
except SpaceError:
    print("Dont give only space for your Name")
else:
    print("{} is valid name".format(res))