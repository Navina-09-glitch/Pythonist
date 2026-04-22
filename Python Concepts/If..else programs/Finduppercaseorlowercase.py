print(ord("A"))
print(ord("Z"))
def decide():
    s=input("Enter letter : ")
    if (len(s)==1 and ord(s) in range(65,91)):
        print("It is upper")
    elif(ord(s) in range(97,123)):
        print("It is lower")
    else:
        print("It is special symbol")
#Call the function
decide()

