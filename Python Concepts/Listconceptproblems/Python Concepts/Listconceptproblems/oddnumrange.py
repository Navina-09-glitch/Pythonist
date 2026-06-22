start=int(input("Enter start number: "))
end=int(input("Enter end number: "))
print("even numbers in the range")
count=0
for i in range(start,end+1):
    if i%2!=0:
        print(i,end=" ")
        count=count+1
print()
print("count of num",count)