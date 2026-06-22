print("Enter list of elements separated by space")
lst=[float(val) for val in input().split()]
pslist=list(filter(lambda val:val>0,lst))
nglist=list(filter(lambda val:val<0,lst))
print("positive elements=",pslist)
print("negative elements=",nglist)