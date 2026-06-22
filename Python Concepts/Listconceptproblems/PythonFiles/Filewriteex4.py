x=(10,"Rossum",45.67,True,2+3j)
with open("peoples1.info","a") as fp:
    fp.writelines(str(x)+"\n")