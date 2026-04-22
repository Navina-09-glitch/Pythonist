lst=[10,-12,30,-40,-50,13,56,-23,-78,90,0,16,-17,66,-55,10]
print("Given list of elements=",lst)
pslist=[val for val in lst if val>0] #list comprehension
print("positive list of elements=",pslist)
nglist=[val for val in lst if val<0] #list comprehension
print("negative list of elements=",nglist)