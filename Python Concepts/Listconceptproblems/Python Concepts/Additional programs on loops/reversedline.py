line=input("enter line of text")
if(len(line)>=0):
    print("line={}".format(line))
    words=line.split()
    for word in words:
        print("\t\t{}--->{}".format(word,len(word)))
    rw=[]
    for w in words:
        rw.append(w[::-1])
    else:
        print("reversed line with words={}".format(" ".join(rw)))
else:
    print("no words")