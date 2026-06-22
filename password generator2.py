#attempts need to be captured
#maxattempts need to be captured somewhere
#i need to ask the customer to enter password only 3 times.
#increase the attempts by 1 everytime he gets it wrong
#keep asking him password until the number of attempts is 3
from Projects.passwordchecker import attempts

#input statement to capture the password
#chck if the password is correct or not
#if its correct then print password accepted
#else ask the user to input the password again
correctpassword="admin123"
attempts=0
maxattempts=3
while attempts<maxattempts:
    enteredpassword=input("enter your password:")
    if enteredpassword==correctpassword:
        print("password accepted")
        break
    else:
        attempts=attempts+1
        if attempts<maxattempts:
            print(f'sorry you got your password wrong please try again')
        else:
            print('max attempt reached,please contact administrator')