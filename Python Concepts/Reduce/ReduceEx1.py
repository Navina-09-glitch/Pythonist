#Program for finding sum of list of values
import functools #predefined module
lst=list(map(float,input("Enter list of values separated by space:").split()))
print("Given values:")
print(lst)
res=functools.reduce(lambda x,y:x+y,lst)
print("Sum({})={}".format(lst,res))