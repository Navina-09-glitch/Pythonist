n=int(input("enter no."))
if(n<=0):
    print("{} is invalid".format(n))
elif(n%2==0):
    print("{} is even".format(n))
elif(n%2!=0):
    print("{} is odd".format(n))
print("Iam from if... elif ...else statement")
