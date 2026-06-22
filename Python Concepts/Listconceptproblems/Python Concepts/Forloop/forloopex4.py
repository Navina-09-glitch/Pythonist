lst=[10,20,30,40,50]
s=0
for v in lst:
    print("\t{}".format(v))
    s=s+v
else:
    print("sum={}".format(s))
    print("average={}".format(round(s/len(lst),2)))
    