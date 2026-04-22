def dispvalues(**kvr):
    print("-"*50)
    for k,v in kvr.items():
        print("\t{}-->{}".format(k,v))
    print("-"*50)

# Main Program
dispvalues(eno=10, ename="RS", sal=45.67, compname="PSF")
dispvalues(sno=20, sname="Travis", cm=30, cppm=56, pm=58)
dispvalues(tno=30, tname="Ritchie", subject1="PYTHON", subject2="JAVA", subject3="C", colname="JNTU")
dispvalues(cid=40, cname="Hunter", job="Student")