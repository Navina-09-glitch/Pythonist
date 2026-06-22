#Program for listing all python files of folder
import os
Fileslist=os.listdir("C:\\Users\\Administrator\\PycharmProjects\\PythonProject1\\PythonFiles")
print(Fileslist)
print("Number of Files:", len(Fileslist))
nop=0
for filename in Fileslist:
    if filename.endswith(".py"):
        print("\t\t{}".format(filename))
        nop=nop+1
print("Number of Files:",nop)