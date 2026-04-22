def dispstudvals(sno,sname,marks,crs="PYTHON",cnt="INDIA"):
    print("\t{}\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs,cnt))
print("\tSNO\tSNAME\tMARKS\tCRS\tCOUNT")

dispstudvals(10,"RS",34.56)
dispstudvals(20,"TR",44.16)
dispstudvals(30,"DR",24.76)
dispstudvals(40,"RS",44.16)
dispstudvals(50,"JH",24.16)
dispstudvals(60,"DT",11.11,"JAVA","USA")
dispstudvals(70,"JB",21.21,cnt="USA")
dispstudvals(80,"PR",33.32,cnt="FRANCE",crs="HTML")