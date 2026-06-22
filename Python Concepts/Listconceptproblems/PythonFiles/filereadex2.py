try:
    with open("hyd.info","r") as fp:
        filedata=fp.readlines()
        for data in filedata:
            print(data,end="")
        print()
except FileNotFoundError:
    print("File doesn't exist")