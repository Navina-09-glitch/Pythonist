lst=[12,4,15,8,45,-5,0,17]
print("Given list",lst)
sqlist=[val**0.5 for val in lst]
print("-"*50)
print("Given value\t\tSquare Root")
print("-"*50)
for ov,sv in zip(lst,sqlist):
    if(type(sv)!=complex):
        print("\t{}\t\t\t{}".format(ov,round(sv,2)))
    else:
        print("\t{}\t\t\t{}".format(ov,sv))
print("-"*50)
