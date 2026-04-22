#Program for finding biggest of list of values
import functools #predefined module
def bigv(k,v):
    return (k if k<v else v)
def smallv(k,v):
    return (k if k>v else v)
lst=list(map(float,input("Enter list of values separated by space: ").split()))
print("Given Values:")
print(lst)
#logic for finding Max and min from list of values
bv=functools.reduce(bigv,lst)
sv=functools.reduce(smallv,lst)
print("Max({})={}".format(lst,bv))
print("Min({})={}".format(lst,sv))