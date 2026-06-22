for i in range(1,6):
    print("Outer loop:Value of i=",i)
    for j in range(1,4):
        print("Inner loop:Value of j=",j)
    else:
        print("\t out-off inner loop")
else:
    print("\t out-off inner loop")