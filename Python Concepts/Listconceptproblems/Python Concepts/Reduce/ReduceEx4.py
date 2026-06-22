#Program for finding biggest of list of Values
import functools #predefined module
def bigv(k,v):
    if(k>v):
        return k
    else:
        return v
def smallv(k,v):
    if(k<v):
        return k
    else:
        return v
lst=list(map(float,input("Enter list of Values separated by space:").split()))
print("Given values")
print(lst)
bv=functools.reduce(bigv,lst)
sv=functools.reduce(smallv,lst)
print("Max({})={}".format(lst,bv))
print("Min({})={}".format(lst,sv))