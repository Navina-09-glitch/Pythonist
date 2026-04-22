#Program for finding biggest of list of values
import functools #predefined module
lst=list(map(float,input("Enter list of values separated by space:").split()))
print("Given Values")
print(lst)
#logic for finding Max and min from list of values
bv=functools.reduce(lambda x,y:x if x>y else y ,lst)
sv=functools.reduce(lambda x,y:x if x<y else y ,lst)
print("Max({})={}".format(lst,bv))
print("Min({})={}".format(lst,sv))