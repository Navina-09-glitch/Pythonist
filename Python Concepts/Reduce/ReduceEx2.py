#Program for finding sum of list of values
import functools #predefined module
def sumop(x,y):
    return (x+y)

#Main Program
lst=list(map(float,input("Enter list of values separated by space").split()))
print("Given values")
print(lst)
#find sum of list of values
res=functools.reduce(sumop,lst)
print("Sum({})={}".format(lst,res))