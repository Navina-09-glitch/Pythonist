import os
try:
    os.remove("C:\\Users\\packdemo1.py")
    print("File name removed--verify")
except FileNotFoundError:
    print("File name doesn't exist")


#remove multiple files?--by putting files to be removed in a list
#Filenames=["stud.data","stud2.data","stud3.data"]
#for filename in filenames:
#	os.remove(filename)

