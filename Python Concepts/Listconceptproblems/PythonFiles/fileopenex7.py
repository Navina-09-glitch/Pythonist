try:
    with open("stud4.data","x+") as fp:
        print("File created and opened in write mode")
        print("Type of fp:{}".format(type(fp)))
        print("Is file closed={}".format(fp.closed))
        print("\t\tFile Name:",fp.name)
        print("\t\tFile Mode:",fp.mode)
        print("\t\tIs File readable:",fp.readable())
        print("\t\tIs File writable:",fp.writable())
    print("out-off with open() as indentation")
    print("\t\tIs File closed:".format(fp.closed))
except FileExistsError:
    print("File exists--try with new file name")
