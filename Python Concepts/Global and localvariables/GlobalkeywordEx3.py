# GlobalKeywordEx3.py
def update1():
    global a, b
    a = a + 1  # Here a is considered by PVM as global Var  bcoz of global kwd
    b = b + 1  # Here b is considered by PVM as global Var  bcoz of global kwd
def update2():
    global a, b
    a = a * 2  # Here a is considered by PVM as global Var bcoz of global kwd
    b = b * 2  # Here b is considered by PVM as global Var  bcoz of global kwd
def update3():
    c=a+2 #Here we are accessing the global var a but not modifying.so no need to write global keyword
    d=b+2 #Here we are accessing the global var b but not modifying. so no need to write global keyword
    print("In Update3() c={} and d={}--they are local".format(c, d))#since c and d are local variables we cannot call outside of function
# Main Program
a, b = 10, 20  # Global Variable
print("Main Program--before update1():  a={}  b={}".format(a, b))
update1()  # Function Call
print("Main Program----after update1():  a={}  b={}".format(a, b))
update2()
print("Main Program----after update2():  a={}  b={}".format(a, b))
update3()
print("Main Program----after update3():  a={}  b={}".format(a, b))
#Here you can notice before and after update3 a,b values are not modified. since we are not modifying it and
#c and d are local variables

