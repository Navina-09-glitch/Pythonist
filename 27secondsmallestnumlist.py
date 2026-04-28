n=int(input("enter numbers:"))
if (n<=1):
    print("need at least 2 numbers to find the second smallest number")
else:
    numbers=[]
    for i in range(n+1):
        val=float(input("enter value {}:".format(i)))
        numbers.append(val)
    print("original list:", numbers)
    numbers.sort()
    print("The second smallest number is :", numbers[1])