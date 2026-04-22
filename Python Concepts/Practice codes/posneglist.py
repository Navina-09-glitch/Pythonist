#Accept number of elements
n=int(input("Enter the number of elements:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        val=int(input("Enter value :".format(i)))
        lst.append(val)
    print("original list:{}".format(lst))
    #Separate positive and negative values
    positives=[]
    negatives=[]
    for num in lst:
        if(num>0):
            positives.append(num)
        elif(num<0):
            negatives.append(num)
    #Print results
    print("positive numbers:{}".format(positives))
    print("negative numbers:{}".format(negatives))
    #Using list comprehension
    positive_num=[x for x in lst if x>0]
    negative_num=[x for x in lst if x<0]
    print("positive_numbers:{}".format(positive_num))
    print("negative_numbers:{}".format(negative_num))
