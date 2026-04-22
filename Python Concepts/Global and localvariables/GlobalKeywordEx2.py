def update1():
    global a,b
    a=a+1 #a is considered by PVM as global var because of global keyword
    b=b+1 #b is considered by PVM as global var because of global keyword
def update2():
    global a,b
    a=a*2 #a is considered by PVM as global var because of global keyword
    b=b*2 #b is considered by PVM as global var because of global keyword

#Main Program
a,b=10,20
print("Main Program--val of a before update1(): a={} b={}".format(a,b))
update1() #Function call
print("Main Program--val of a after update1(): a={} b={}".format(a,b))
update2()
print("Main Program--val of a after update2(): a={} b={}".format(a,b))