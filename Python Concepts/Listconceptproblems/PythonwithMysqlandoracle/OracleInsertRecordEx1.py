import oracledb as orc
def recordinsert():
    try:
        con=orc.connect("system/password@127.0.0.1:1522/orcl")
        cur=con.cursor()
        iq="insert into employee values(30,'Hunter',2.3,'matplot')"
        cur.execute(iq)
        con.commit()
        print("Record inserted in table---verify")
    except orc.DatabaseError as db:
        print("Problem in Oracle Database:",db)

#Main Program
recordinsert()