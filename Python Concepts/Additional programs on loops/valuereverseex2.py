val=input("enter any value")
print("given value :{}".format(val))
rval=""
for v in val[::-1]:
    rval=rval+v
else:
    print("reversed value=",rval)