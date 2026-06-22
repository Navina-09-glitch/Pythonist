try:
    fp=open("stud2.data","r")
except FileNotFoundError:
    print("File does not exist")
else:
    print("Iam from else block")
    print("File opened in read mode successfully")
    print("Type of fp=",type(fp))
    print("Is file closed=",fp.closed)
finally:
    try:
        print("Iam from finally block")
        fp.close() #Manual closing
        print("File closed safely")
        print("Is file closed=",fp.closed)
    except NameError:
        print("File not at all opened in read mode---No need to close")