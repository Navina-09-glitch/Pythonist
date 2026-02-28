n=int(input("Enter no of elements:"))
if (n<=0):
    print("Invalid no of elements".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        val=float(input("Enter value {}: ".format(i)))
        lst.append(val)
    print(lst)
    x=int(input("Element to find:"))
    count=0
    for num in lst:
        if num==x:
            count=count+1
    print("{} occured {} times".format(x,count))


#after defining list
#frequency={}
#for j in lst:
    #if j in frequency:
        #frequency[j]= frequency[j]+1
    #else:
        #frequency[j]=1
#print("\n frequency of elements")
#for key,value in frequency.items():
    #print("key {} and value {}".format(key,value))