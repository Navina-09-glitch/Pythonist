line=input("enter line :")
if len(line)>=1:
    words=line.split()
    print("Given line={}".format(line))
    for w in words:
        print("\t\t{}--->{}".format(w,len(w)))
