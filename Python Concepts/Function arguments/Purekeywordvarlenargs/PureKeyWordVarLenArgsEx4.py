def findtotalmarks(ID,sname,cls,city="HYD",**submarks):
    print("\tStudent Number:{}".format(ID))
    print("\tStudent Name:{}".format(sname))
    print("\tStudent Class:{}".format(cls))
    print("\tStudent City:{}".format(city))
    if(len(submarks)!=0):
            tot=0
            print("\tSubject Name\tMarks")
            for k,v in submarks.items():
                print("\t{}\t{}".format(k,v))
                tot+=v
            print("\tTotal Marks:{}".format(tot))
findtotalmarks(100,"Praveen","X",telugu=70,hindi=80,english=85,maths=90,science=89,social=80)
findtotalmarks(200,"Sandeep","XI",Sanskrit=99,Eng=95,Maths=75,Phy=60,Che=58)
findtotalmarks(300,"Balaji","B.Tech",OS=70,DBMS=60,NW=50,C=59)
findtotalmarks(cls="Research",sname="Rossum",city="NL",ID=400)
findtotalmarks(500,"Shankar","V",Tel=50,Eng=60,Maths=70,abacus=40,city="FINLAND")
findtotalmarks(600,"Athar","MCA","AP",AI=40,CG=60)