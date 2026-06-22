n=int(input("Enter a number: "))
if n<=0:
    print("res {} is invalid input".format(n))
elif(n%2==0):
    print("res {} is  even".format(n))
else:
    print("res {} is  odd".format(n))