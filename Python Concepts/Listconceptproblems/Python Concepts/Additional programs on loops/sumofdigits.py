num=input("enter a number")
if num.isdigit():
    num=int(num)
    if (num<=0):
        print("sorry no number".format(num))
    else:
        sum=0
        for x in str(num):
            sum=sum+int(x)
        else:
            print("sum of digits is ({})={}".format(num,sum))
else:
    print("sorry no number last".format(num))