n=int(input("Enter a number:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    if(n%2==0):
        print("{} is even".format(n))
    else:
        print("{} is odd".format(n))
    print("Iam from inner if.. else statement")
print("Iam from outer if...else statement")