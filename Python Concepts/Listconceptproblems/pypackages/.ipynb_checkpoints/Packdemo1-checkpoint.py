import sys
sys.path.append("C:\\Users\\Administrator\\PycharmProjects\\PythonProject1\\Python Concepts\\Demo of packages")
#The above mentioned path is the absolute path of the folder where modules are present
#you can also use \\ or / else it throws unicode error since \U has original meaning in PVM
#import sys
#print(type(sys.path))
#Path is an global variable and its type is list
from welcome import greet
greet("GUIDO VAN ROSSUM")