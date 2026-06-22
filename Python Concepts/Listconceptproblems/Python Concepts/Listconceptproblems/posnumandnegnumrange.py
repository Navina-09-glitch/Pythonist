start=int(input("Enter start number: "))
end=int(input("Enter end number: "))
print("positive numbers in the range")
pos_count=0
neg_count=0
for i in range(start,end+1):
    if i>0:
        print(i,end=" ")
        pos_count=pos_count+1
print()
print("count of positive num",pos_count)
#negative number range
for i in range(start,end+1):
    if i<0:
        print(i,end=" ")
        neg_count=neg_count+1
print()
print("count of negative num",neg_count)