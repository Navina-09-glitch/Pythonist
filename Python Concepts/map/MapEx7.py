#Program for adding two unequal list elements
lst1=list(map(float,input("Enter first line Elements:").split()))
lst2=list(map(float,input("Enter second line Elements:").split()))
#In the case list1 contains more elements than list2
if(len(lst1)>len(lst2)):
    for i in range(len(lst1)-len(lst2)):
        lst2.append(0)
elif (len(lst2)>len(lst1)):
    for i in range(len(lst2)-len(lst1)):
        lst1.append(0)
#add two list objects data
sumlist=list(map(lambda a,b:a+b,lst1,lst2))
print("\tlist1\t\tlist2\t\tsumlist")
for val1,val2,val3 in zip(lst1,lst2,sumlist):
    print("{}\t\t{}\t\t{}\t\t{}".format(val1,val2,val3,round(val3,2)))
print("-"*50)