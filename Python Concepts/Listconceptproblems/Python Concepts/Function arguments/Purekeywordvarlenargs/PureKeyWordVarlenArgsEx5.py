#PureKeyWordVarLenArgsEx5.py
def findtotalmarks(ID,sname,cls,*vals, city="HYD",**submarks):
	print("-"*50)
	print("\tStudent Number:{}".format(ID))
	print("\tStudent Name:{}".format(sname))
	print("\tStudent Class:{}".format(cls))
	print("\tStudent Living City={}".format(city))
	print("Variable Length args={} and Length={}".format(vals,len(vals)))
	print("-"*50)
	if(len(submarks)!=0):
		tot=0
		print("\tSubject Name\tMarks")
		print("-"*50)
		for subject,marks in submarks.items():
			print("\t{}\t\t{}".format(subject,marks))
			tot=tot+marks
		print("-"*50)
		print("\tTOTAL MARKS={}".format(tot))
		print("-"*50)
#Main Program
findtotalmarks(100,"Praveen","X",10,13,14,9,17,15,telugu=70,hindi=80,english=85,maths=90,science=89,social=80)
findtotalmarks(200,"Sandeep","XI",2.3,4.5,5.6,6.7,5,Sanskrit=99,Eng=95,Maths=75,Phy=60,Che=58)
findtotalmarks(300,"Balaji","B.Tech","A","B","C","D",OS=70,DBMS=60,NW=50,C=59)
findtotalmarks(400,"Rossum","Research",1,2,3,city="NL")
findtotalmarks(500,"Shankar","V",Tel=50,Eng=60,Maths=70,abacus=40,city="FINLAND")
findtotalmarks(600,"Athar","MCA",11,22,city="AP",AI=40,CG=60)