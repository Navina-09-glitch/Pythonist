def findtotalmarks(ID,sname,cls,**submarks):
    print("-"*50)
    print("\tStudent Number:{}".format(ID))
    print("\tStudent Name:{}".format(sname))
    print("\tStudent Class:{}".format(cls))
    print("-"*50)
    if(len(submarks)!=0):
        tot=0
        print("\tSubject Name\tMarks")
        for subject,marks in submarks.items():
            tot+=marks
        print("\tTotal Marks:{}".format(tot))
        print("-"*50)
findtotalmarks(100,"Praveen","X",telugu=70,hindi=80,english=85,maths=90,science=89,social=80)
findtotalmarks(200,"Sandeep","XI",Sanskit=99,Eng=95,Maths=75,Phy=60,Che=58)
findtotalmarks(300,"Balaji","B.tech",OS=70,DBMS=60,NW=50,C=59)
findtotalmarks(400,"Rossum","Research")