import random
n = int(input("Enter number of elements: "))
if n <= 0:
    print("{} is an invalid input".format(n))
else:
    lst = []
    for i in range(1, n + 1):
        val = float(input("Enter value {}: ".format(i)))
        lst.append(val)
    print("Original list:", lst)
    random.shuffle(lst)
    print("Shuffled list:", lst)