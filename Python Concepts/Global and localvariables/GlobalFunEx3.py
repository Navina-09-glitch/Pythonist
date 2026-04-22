a=10
b=40
def infoglobals():
    d=globals()
    print(len(d))
    print("Invisible and programmer-defined global variables")
    print(d,type(d))
    for k,v in d.items():
        print("t{}-->{}".format(k,v))
    print("-"*50)

    print("Programmer-defined global variables---way-1")
    print("\tGlobal var a",d.get('a'))
    print("\tGlobal var b",d.get('b'))

    print("Programmer-defined global variables---way-2")
    print("\tGlobal var a=", d['a'])
    print("\tGlobal var b=", d['b'])

    print("Programmer-defined global variables---way-3")
    print("\tGlobal var a=",globals()['a'])
    print("\tGlobal var b=",globals()['b'])
    
    print("Programmer-defined global variables---way-4")
    print("\tGlobal var a=",globals().get('a'))
    print("\tGlobal var b=",globals().get('b'))

#Main Program
infoglobals()