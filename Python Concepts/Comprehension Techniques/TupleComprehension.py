lst=(12,4,15,8,-5,0,17)
print("Given lst: {}".format(lst))
sqlist=(val**2 for val in lst)
#Not a tuple comprehension
#Here sqlist is an object of <class 'generator'>
#convert generator object sqlist into tuple
#if we convert it in to set it will not maintain order of elements like set(sqlist) we can check . so use tuple to maintain order
sqlelements=set(sqlist)
print("Given sqlist: {}".format(sqlist))
for ov,sv in zip(lst,sqlelements):
    if(type(sv)!=complex):
        print("\t{}\t\t\t{}".format(ov,round(sv,2)))
    else:
        print("\t{}\t\t\t{}".format(ov,sv))
print("-"*50)