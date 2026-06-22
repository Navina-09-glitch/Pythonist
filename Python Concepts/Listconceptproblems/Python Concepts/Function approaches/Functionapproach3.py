#Input: Taking from Function call
#Process: Inside Function body
#Output: Inside of Function body

def sumop(x,y):
    z=x+y
    print("Sum of {} and {} is {}".format(x,y,z))

#Main program
a=float(input("Enter first number"))
b=float(input("Enter second number"))
sumop(a,b) #Function call taking input but not returning value
