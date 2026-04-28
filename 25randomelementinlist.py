import random
n=int(input("enter no of elements:"))
if(n<=0):
    print("{} is an invalid input".format(n))
else:
    lst=[]
    for i in range(n+1):
        val=float(input("enter {}:".format(i)))
        lst.append(val)
    print("original list:{}",lst)
random_item=random.choice(lst)
print("original list:{}",lst)
print("random item:{}",random_item)