import os
try:
    os.removedirs("C:\\INDIA\\TS\\HYD\\PYTHON")
    print("Folders Hierarchy removed successfully--verify")
except FileNotFoundError:
    print("Folders Hierarchy doesnot exist")
except OSError:
    print("Make sure the folder empty")