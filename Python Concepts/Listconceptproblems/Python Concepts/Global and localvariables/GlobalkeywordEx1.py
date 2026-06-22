#Program for demonstrating the need of global keyword
#GlobalKeywordEx1.py
def update1():
    global a
    a=a+1 #Here a is considered by PVM as a global variable because of global keyword

def update2():
    global a
    a=a*2 #Here a is considered by PVM as a global variable because of global keyword

#Main Program
a=10 #Global variable
print("Main Program--val of a before update1()={}".format(a))
update1() #Function call
print("Main Program--val of a after update1()={}".format(a))
update2()
print("Main Program--val of a after update2()={}".format(a))


