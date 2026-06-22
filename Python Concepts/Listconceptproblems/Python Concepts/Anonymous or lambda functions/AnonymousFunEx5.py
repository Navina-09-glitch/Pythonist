def kvrmax(lst):
    maxv=lst[0]
    for v in lst:
        if(v>maxv):
            maxv=v
    return maxv
def kvrmin(lst):
    minv=lst[0]
    for v in lst:
        if(v<minv):
            minv=v
    return minv
#Anonymous Function Defs
findmax=lambda lst: kvrmax(lst)
findmin=lambda lst: kvrmin(lst)
#Main Program
print("Enter list of values separated by comma")
lst=[float(val) for val in input().split(",")]
maxv=findmax(lst)
minv=findmin(lst)
print("Max value is ({})={}".format(lst, maxv))
print("Min value is ({})={}".format(lst, minv))