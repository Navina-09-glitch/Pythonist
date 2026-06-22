import mysql.connector as orc
def selectrecord():
    try:
        con=orc.connect(user='root',password='password',host='localhost',database='batch11am')
        cur=con.cursor()
        sq="select * from employee"
        cur.execute(sq)
        #get the records from cursor objects by using fetchone()
        print("-"*50)
        print("\t\tList of records")
        print("-"*50)
        records=cur.fetchall()
        for record in records:
            for val in record:
                print("\t {}".format(val),end="\t")
            print()
        print("-"*50)
    except orc.DatabaseError as db:
        print("problem with MySQL DB:",db)

#Main Program
selectrecord()