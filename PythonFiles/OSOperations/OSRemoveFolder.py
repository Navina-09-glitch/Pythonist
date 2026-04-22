#Program for Removing a Folder
import os
try:
    os.rmdir("HYD\\PYTHON")
    print("Folder removed successfully--verify")
except FileNotFoundError:
    print("Folder doesnot exist")
except OSError:
    print("Make sure that Folder must be empty")