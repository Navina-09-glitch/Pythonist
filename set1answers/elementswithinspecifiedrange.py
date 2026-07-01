n = int(input("Enter number of elements: "))
if n <= 0:
    print("Please enter a number greater than zero")
else:
    lst = []
    for i in range(1, n+1):   # include n
        val = float(input("Enter number {}: ".format(i)))
        lst.append(val)

    print("Original list:", lst)

    startingrange = float(input("Enter starting range: "))
    endingrange = float(input("Enter ending range: "))

    # Collect elements within range
    in_range = [x for x in lst if startingrange <= x <= endingrange]

    print("Elements between {} and {}: {}".format(startingrange, endingrange, in_range))
    print("Count of elements:", len(in_range))
