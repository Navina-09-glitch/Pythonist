try:
    with open("stud3.data","x") as fp:
        print("File created and opened in write mode")
        print("Type of fp:{}".format(type(fp)))
        print("File properties")
        print("Is file closed={}".format(fp.closed))
        print("\t\tFile Name:",fp.name)
        print("\t\tFile Mode:",fp.mode)
        print("\t\tIs File Readable:",fp.readable())
        print("\t\tIs File Writable:",fp.writable())
    print("-"*50)
    print("out-off with open() as Indentation")
    print("Is file closed={}".format(fp.closed))
except FileExistsError:
    print("File already exist---try with new file name")