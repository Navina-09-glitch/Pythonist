import os
try:
    os.mkdir("HYD\\PYTHON") #here i have not mentioned path ,so it will take current working directory python files
    print("Folder Created Successfully--verify")
except FileExistsError:
    print("Folder already exists--verify--try on another name")
except FileNotFoundError:
    print("Root Folder Does not Exist")
# If you want to create multiple subfolders
#You have to create parent folder first . then create subfolders like using os.mkdir("C:\\KVR\\PYTHON\\KVR")
#os.mkdir can help you to create only one folder at a time, to create all subfolder at a time we can use os.makedirs("")