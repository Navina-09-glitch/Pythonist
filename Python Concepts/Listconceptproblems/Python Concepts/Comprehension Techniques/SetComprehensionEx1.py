#program for accepting list of values and print unique number of positive and negative values from list of values
#SetComprehensionEx1.py

lst=[10,-12,30,-40,-50,13,56,-23,-78,90,0,16,-17,66,-55,10]
print("Given list of elements=",lst)
pslist={val for val in lst if val>0} #set comprehension
print("Given list of elements=",pslist)
nglist={val for val in lst if val<0}#set comprehension
print("Given list of elements=",nglist)

#We have used set comprehension to print unique elements
