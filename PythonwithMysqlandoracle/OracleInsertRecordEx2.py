#Program for reading the Values from KBD and Insert then as Record in Employee Table
#OracleInsertRecordEx2.py
import oracledb as orc
def recordinsert():
    try:
        con = orc.connect("system/Venky%7119@127.0.0.1:1522/orcl")
        cur = con.cursor()
        #read emp values from KBD
        print("--------------------------------------")
        eno=int(input("Enter Employee Number:"))
        ename=input("Enter Employee Name:")
        empsal = float(input("Enter Employee Salary:"))
        compname = input("Enter Employee Comp Name:")
        print("--------------------------------------")
        #iq = "insert into employee values(%d,'%s',%f,'%s')"
        #cur.execute(iq %(eno,ename,empsal,compname))
        #OR
        cur.execute("insert into employee values(%d,'%s',%f,'%s')" %(eno,ename,empsal,compname) )
        con.commit()
        print("{} Record Inserted in Table--verify".format(cur.rowcount))
    except orc.DatabaseError as db:
        print("Problem in Oracle database:",db)
#Main Program
recordinsert()