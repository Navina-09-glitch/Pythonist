#OSCreateFoldersHierarchy.py
#Program for Creating Folders Herarchy
import os
try:
    os.makedirs("C:\\INDIA\\TS\\HYD\\PYTHON")
    print("Folders Hierarchy Created")
except FileExistsError:
    print("Folders Hierarchy already Exist")