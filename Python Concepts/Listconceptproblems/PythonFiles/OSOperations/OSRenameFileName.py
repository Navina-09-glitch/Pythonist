import os
try:
    os.rename(dst="C:\\INDIA\\TS\\HYD\\python\\anjali.txt",src="C:\\INDIA\\TS\\HYD\\python\\index.txt")#Here src and dst order can be changed but it should be specified which is source and destination
    print("File name Renamed---verify")
except FileNotFoundError:
    print("Source File Name Does Not Exist")

#rename multiple files?--by putting files to be renamed in a dictionary
#Filenames=["stud.data":"file1.data","stud2.data":"file2.data","stud3.data":"file3.data"]
#for srcfile,dstfile in filenames.items():
#	os.rename(srcfile,dstfile)