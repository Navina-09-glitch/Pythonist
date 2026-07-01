while True:
    try:
        n=int(input("enter numbers:"))
        if(n<2):
            print("need atleast two elements to find the second smallest number")
        else:
            numbers=[]
            for i in range(n):
                val=float(input("enter value:{}".format(i)))
                numbers.append(val)
            print("original list",numbers)
            numbers.sort()
            print("the second smallest number is:",numbers[1])
    except ValueError:
        print("please try again with valid input")