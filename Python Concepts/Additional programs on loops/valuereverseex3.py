n=int(input("enter numerical value"))
print("given value".format(n))
sum=0
while(n>0):
    r=n%10
    sum=sum*10+r
    n=n//10
else:
    print("reversed value={}".format(sum))