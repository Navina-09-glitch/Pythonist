def disp(sno,sname,*kvr,city="HYD"):
    print("Student Number:{}".format(sno))
    print("Student Name:{}".format(sname))
    print("Student City:{}".format(city))
    s=0
    for k in kvr:
        s=s+k
    else:
        print("\tsum={}".format(s))
#Main Program

disp(100,"Rossum",10,20,30,40,50)
disp(200,"Travis",10.2,20.2,30.3,40.4)
disp(300,"Hunter",10,20,30)
disp(400,"James",10.2,20)
disp(500,"Ststrup")
disp(600,"KVR",40,city="AP",50,60,80)
disp(600,"KVR",40,50,60,80,"AP")
disp(600,"KVR",40,50,60,80,city="AP")