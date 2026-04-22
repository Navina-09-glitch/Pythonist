#This Program Program will not execute as it is bcoz Python Compiler and PVM can performs Interpretation Process and
#It can remember only Latest Function Function.
def dispvalues(eno,ename,sal,compname):
    print(eno,ename,sal,compname)
def dispvalues(sno,sname,cm,cppm,pm):
    print(sno,sname,cm,cppm,pm)
def dispvalues(tno,tname,subject1,subject2,subject3,colname):
    print(tno,tname,subject1,subject2,subject3,colname)
def dispvalues(cid,cname,job):
    print(cid,cname,job)

#Main Program
dispvalues(eno=10,ename="RS",sal=45.67,compname="PSF")
dispvalues(sno=20,sname="Travis",cm=30,cppm=56,pm=58)
dispvalues(tno=30,tname="Ritchie",subject1="PYTHON",subject2="JAVA",subject3="C",colname="JNTU")
dispvalues(cid=40,cname="Hunter",job="Student")