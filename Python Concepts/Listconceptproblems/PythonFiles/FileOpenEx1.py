try:
    fp=open("C:/Users/Administrator/PycharmProjects/PythonProject1/Python Concepts/Continue/nusrath.csv","r")
    print(fp)
except FileNotFoundError:
    print("File does not exist")
else:
    print("File opened in readmode successfully")

