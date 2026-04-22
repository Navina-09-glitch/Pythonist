import oracledb as orc
def altertablecol():
    try:
        con=orc.connect("system/password@localhost:1522/orcl")
        cur=con.cursor()
        aq="alter table employee add(compname varchar2(10) not null)"
        cur.execute(aq)
        print("table altered --verify")
    except orc.DatabaseError as db:
        print("Problem on oracle Database:",db)

#Main Program
altertablecol()