lst=[2,14,16,9,3,15,25,81]
sqrd={}
for val in lst:
    sqrd[val]=val**2
print(sqrd)
#Using DictComprehension
lst=[2,14,16,9,3,15,25,81]
sqrd={val:val**2 for val in lst} #Dict Comprehension
print("Given value\t\tSquare")
for val,squareval in sqrd.items():
    print("\t{}\t\t\t{}".format(val,squareval))
print("-"*50)
sqrtd={val:val**0.5 for val in lst} #Dict Comprehension
print("Given value\t\tSquare root")
for v,sv in sqrtd.items():
    print("\t{}\t\t\t{}".format(v,round(sv,2)))
print("-"*50)
