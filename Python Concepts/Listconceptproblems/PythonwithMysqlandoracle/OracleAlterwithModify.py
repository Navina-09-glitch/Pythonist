import oracledb as orc
def altertablecolsizes():
    try:
        con=orc.connect("system/password@localhost:1522/orcl")
        cur=con.cursor()
        aq="alter table employee modify(eno number(3),name varchar(15))"
        cur.execute(aq)
        print("table altered --verify")
    except orc.DatabaseError as db:
        print(db)

#Main Program
altertablecolsizes()