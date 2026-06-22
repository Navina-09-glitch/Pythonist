#Program for Listing all Python Files  starts with OS*.py
#OSListFilesEx4.py
import os
foldername=input("Enter Any Folder Name to View Files:")
Fileslist=os.listdir(foldername)
print("-----------------------------------------------------")
print("Number of Files=", len(Fileslist))
print("-----------------------------------------------------")
for filename in Fileslist:
    print("\t\t{}".format(filename))
print("-----------------------------------------------------")