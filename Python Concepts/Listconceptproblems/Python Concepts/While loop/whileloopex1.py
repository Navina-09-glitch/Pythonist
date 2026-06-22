n=int(input("enter how many numbers you want to generate"))
if(n<=0):
    print("{} is an invalid input".format(n))
else:
    i=1
    while(i<=n):
        print(i)
        i=i+1
    else:
        print("Iam from else part of while loop")
    print("while loop is over")
print("Iam from if...else statement")