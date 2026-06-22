#Program for Listing all Python Files of Folder
#OSListFilesEx3.py
import os
foldername=input("Enter the folder name: ")
Fileslist=os.listdir(foldername)
print("-----------------------------------------------------")
print("Number of Files=", len(Fileslist))
nop=0
print("-----------------------------------------------------")
for filename in Fileslist:
    if (filename.startswith("OS") and filename.endswith((".py"))):  #. is -3,p is-2,y is -1 so from last if file ends with.py it will count
        print("\t\t{}".format(filename))
        nop=nop+1
print("-----------------------------------------------------")
print("Number of Python Files=",nop)
print("-----------------------------------------------------")