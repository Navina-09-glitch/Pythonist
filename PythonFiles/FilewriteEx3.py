x=range(100,121,2)
with open("peoples.info","a") as fp:
    fp.writelines(str(x)+"\n")
    print("Iterable Object Data written to the File")