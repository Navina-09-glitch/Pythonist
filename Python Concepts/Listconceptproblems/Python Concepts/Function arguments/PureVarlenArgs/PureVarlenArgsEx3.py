#This program demonstrates the need of variable length arguments
def disp(sno,sname, *hyd):
    print("Student Number: {}".format(sno))
    print("Student Name: {}".format(sname))
    s=0
    for val in hyd:
        print("\t{}".format(val))
        s=s+val
    else:
        print("\t{}".format(s))

disp(100,"Rossum",10,20,30,40,50)
disp(200,"Travis",10.2,20.2,30.3,40.4)
disp(300,"Hunter",10,20,30)
disp(400,"James",10,20,30)
disp(500,"Ststrup")
        