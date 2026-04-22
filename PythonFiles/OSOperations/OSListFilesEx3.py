#Program for Listing all Python Files of Folder
#OSListFilesEx3.py
import os
Fileslist=os.listdir("C:\\Users\\Administrator\\PycharmProjects\\PythonProject1\\PythonFiles")
print("-----------------------------------------------------")
print("Number of Files=", len(Fileslist))
nop=0
print("-----------------------------------------------------")
for filename in Fileslist:
    if(filename[-3:]==".py"):  #. is -3,p is-2,y is -1 so from last if file ends with.py it will count
        print("\t\t{}".format(filename))
        nop=nop+1
print("-----------------------------------------------------")
print("Number of Python Files=",nop)
print("-----------------------------------------------------")

#foldername I entered:C:\\Users\\Administrator\\PycharmProjects\\PythonProject1\\PythonFiles\\OSOperations