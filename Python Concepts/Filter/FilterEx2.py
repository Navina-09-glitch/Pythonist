def positive(val):
    if(val>0):
        return True
    else:
        return False
def negative(val):
    if(val<0):
        return True
    else:
        return False
#Main Program
print("Enter list of elements separated by space")
lst=[float(val) for val in input().split()]
pslist=list(filter(positive,lst))
nglist=list(filter(negative,lst))
print("Given elements=",lst)
print("List of positive elements=",pslist)
print("List of negative elements=",nglist)