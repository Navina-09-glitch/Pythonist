import oracledb as orc
def createtable():
    try:
        con=orc.connect("system/password@localhost:1522/orcl")
        cur=con.cursor()
        q=input("Enter table creation query in oracle DB: ")
        cur.execute(q)
        print("Table created successfully")
    except orc.DatabaseError as db:
        print("Problem on oracle Database:",db)

#Main Program
createtable()

#create table citizen(adc number(4),cname varchar2(10))