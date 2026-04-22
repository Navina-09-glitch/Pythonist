def positive(val):
    if (val>0):
        return True
    else:
        return False
def negative(val):
    if (val<0):
        return True
    else:
        return False
#Main Program
lst=[10,-20,-30,40,0,-50,60,-70,12]
print("List of values=",lst)
obj1=filter(positive,lst)
obj2=filter(negative,lst)
#convert filter object int list,tuple,set
pslist=list(obj1)
nglist=list(obj2)
print("Given Elements=",lst)
print("Positive elements=",pslist)
print("Negative elements=",nglist)