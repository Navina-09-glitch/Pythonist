import mysql.connector
def tablecreate():
    try:
        con=mysql.connector.connect(host="localhost",user="root",password="password",database="batch11am")
        cur=con.cursor()
        #Create table employee
        tc="create table employee(eno int primary key,name varchar(10) not null,sal real not null,compname varchar(10))"
        cur.execute(tc)
        print("table created in mysql--verify")
    except mysql.connector.DatabaseError as db:
        print("Problem in MYSQL: {}".format(db))

#Main Program
tablecreate()