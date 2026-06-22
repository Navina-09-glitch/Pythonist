n=input("enter how many numbers you want to generate")
if(n.isdigit()):
    num=int(n)
    if(num==0):
        print("zero is invalid input".format(num))
    else:
        print("numbers from {} to 1".format(num))
        i=num
        while(i>=1):
            print(i)
            i=i-1
        else:
            print("_"*50)
else:
    print("{} is invalid input".format(n))