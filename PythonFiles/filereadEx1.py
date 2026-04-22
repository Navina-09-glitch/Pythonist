try:
    with open("hyd.info","r") as fp:
        filedata=fp.read()
        print(filedata)
except FileNotFoundError:
    print("File doesn't exist")