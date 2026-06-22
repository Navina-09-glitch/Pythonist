with open ("stud2.data","a") as fp:
    print("File created and opened in write mode successfully")
    print("Type of fp:{}".format(type(fp)))
    print("-"*50)

    print("File Properties")
    print("Is file closed={}".format(fp.closed))
    print("\t\tFile Name:",fp.name)
    print("\t\tFile Mode:",fp.mode)
    print("\t\tIs File Readable:",fp.readable())
    print("\t\tIs File Writable:",fp.writable())
print("out-off with open() as Indentation")
print("Is file closed={}".format(fp.closed))