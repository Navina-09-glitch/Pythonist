import oracledb as orc
def droptable():
    try:
        con=orc.connect("system/password@localhost:1522/orcl")
        cur=con.cursor()
        #dq="drop table temp"
        cur.execute("drop table temp")
        print("Table dropped--verify")
    except orc.DatabaseError as db:
        print("Problem on oracle Database:",db)

#Main Program
droptable()