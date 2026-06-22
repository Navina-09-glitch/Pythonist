print("Enter list of numbers separated by spaces:")
numbers=[]
for val in input().split():
    numbers.append((val))
print("Given numbers:",numbers)
nums23=list(filter(lambda num:num.isdigit() and len(num) in [2,3], numbers))
print("Numbers with 2 or 3 in length:",nums23)