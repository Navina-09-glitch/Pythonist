#Program for Listing all Files of Folder
import os
Fileslist=os.listdir("C:\\Users\\Administrator\\PycharmProjects\\PythonProject1\\Python Concepts")
print(Fileslist)
print("Number of Files:", len(Fileslist))
for filename in Fileslist:
    print("\t\t{}".format(filename))
