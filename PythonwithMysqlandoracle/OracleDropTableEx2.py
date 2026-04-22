import oracledb as orc
def droptable():
    try:
        con=orc.connect("system/password@localhost:1522/orcl")
        cur=con.cursor()
        #dp="drop table temp"
        tname=input("Enter Table name to remove: ")
        cur.execute("drop table %s" %tname)
        print("Table dropped--verify")
    except orc.DatabaseError as db:
        print("Problem on oracle Database:",db)

#Main Program
droptable()

#just enter only table name in the output console