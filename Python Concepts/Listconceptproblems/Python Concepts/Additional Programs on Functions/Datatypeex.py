def dispval(x):
    if(type(x)==int):
        print("Value: {} Type:{}".format(x,type(x)))
    elif(type(x)==float):
        print("Value: {} Type:{}".format(x,type(x)))
    elif(type(x)==bool):
        print("Value: {} Type:{}".format(x,type(x)))
    elif(type(x)==complex):
        print("Value: {} Type:{}".format(x,type(x)))
    elif(type(x)==str):
        print("Value: {} Type:{}".format(x,type(x)))
    elif(type(x)==bytes):
        print("Value: {} Type:{}".format(x,type(x)))
    elif(type(x)==bytearray):
        print("Value: {} Type:{}".format(x,type(x)))
    elif(type(x)==list):
        print("Value: {} Type:{}".format(x,type(x)))
    elif(type(x)==tuple):
        print("Value: {} Type:{}".format(x,type(x)))
    elif(type(x)==set):
        print("Value: {} Type:{}".format(x,type(x)))
    elif(type(x)==frozenset):
        print("Value: {} Type:{}".format(x,type(x)))
    elif(type(x)==dict):
        print("Value: {} Type:{}".format(x,type(x)))
        for k,v in x.items():
            print("\t\t{}: {}".format(k,v))
    else:
        print("Value: {} Type:{}".format(x,type(x)))

#Main Program
print("Fundamental Category Data Types")
dispval(10)
dispval(10.4)
dispval(True)
dispval(2+3j)
print("Sequential Category Data Types")
dispval("Python")
dispval("bytes([10,20,30,40])")
dispval("bytearray([10,20,30,40])")
dispval(range(10,21,2))
print("List Category Data Types")
dispval([10,20,30,40])
dispval(list("PYTHON"))
dispval(tuple("TUPLE"))
dispval((10,20,30,40))
print("Set Category Data Types")
dispval({10,20,30,40})
dispval(frozenset((10,20,30,40)))
print("Dict Data Types")
dispval({10:1.2,3:4.5,6:6.7})
dispval(dict([(10,"RS"),(20,"TR"),(30,"DR")]))
dispval(dict(zip(["Python","C","C++","Java"],[1,2,3,4])))
print("None Category Data Types")
dispval(None)


