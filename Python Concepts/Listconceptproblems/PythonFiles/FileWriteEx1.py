eno=200
ename="SS"
sal=14.8
with open("emp data","a") as fp:
    fp.write(str(eno)+"\t"+ename+"\t"+str(sal)+"\n")
    print("Data written to the file---verify")