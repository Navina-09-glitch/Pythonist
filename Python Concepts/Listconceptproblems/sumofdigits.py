num=int(input("enter number"))
if(num<=0):
    print("{} is invalid input".format(n))
else:
    temp=num
    sum=0
    while(num>0):
        digit=num%10
        sum=sum+digit
        num=num//10
    print("sum of digits ({})={}".format(temp,sum))
