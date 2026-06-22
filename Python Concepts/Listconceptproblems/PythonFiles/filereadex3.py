#Program for Displaying OR Reading  the Content of any File
try:
    filename=input("Enter the filename: ")
    with open(filename) as fp:
        filedata=fp.readlines() #Here filedata is type list
        for data in filedata:
            print(data,end="")
        print()
except FileNotFoundError:
    print("File doesn't exist")