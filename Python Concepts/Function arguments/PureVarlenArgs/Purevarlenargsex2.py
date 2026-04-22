def disp(*kvr):
    if(len(kvr) == 0):
        print("empty")
    else:
        for val in kvr:
            print("{}".format(val),end=" ")
        print()
    print("-"*50)

#Main Program

disp(10,20,30,40,50)
disp(10,20,30,40)
disp(10,20,30)
disp(10,20)
disp(10)
disp() 