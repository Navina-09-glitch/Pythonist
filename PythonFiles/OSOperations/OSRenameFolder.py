#Program for Renaming a Folder
#OSRenameFolder.py
import os
try:
    os.rename("C:\\INDIA\\TS\\HYD\\PYTHON","C:\\INDIA\\TS\\HYD\\python")
    print("Folder Renamed---verify")
except FileNotFoundError:
    print("Source Folder doesn't exist")