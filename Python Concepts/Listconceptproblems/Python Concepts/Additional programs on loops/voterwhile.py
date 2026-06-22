#loop is used here to keep asking the user for their age until they enter a valid voting age (18 or older).
while(True):
    age=int(input("Enter your age: "))
    if(age<18):
        print("\t {} Years citizen is not eligible to vote".format(age))
    else:
        print("\t {} Years citizen is eligible to vote".format(age))