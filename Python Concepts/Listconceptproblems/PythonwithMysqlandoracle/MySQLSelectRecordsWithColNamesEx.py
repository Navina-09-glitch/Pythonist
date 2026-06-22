import mysql.connector as orc
def getrecordwithcolnames():
    try:
        con=orc.connect(user='root',password='password',database='batch11am')
        cur=con.cursor()
        sq="select * from employee order by name"
        cur.execute(sq)
        #code for getting the colnames
        print("-"*50)
        colinfo=cur.description #Here type of colinfo is list
        #Here description is an attribute which is used for getting the colnames of the table
        for col in colinfo:
            print(col[0],end="\t\t")
        print()
        print("-"*50)
        #code for getting the records
        records=cur.fetchall()
        for record in records:
            for val in record:
                print(val,end="\t\t")
            print()
        print("-"*50)
    except orc.DatabaseError as db:
        print(db)

#Main Program
getrecordwithcolnames()
