import oracledb as orc #Step-1
try:
    con=orc.connect("system/password@localhost:1522/orcl") #Step-2
    cur=con.cursor() #Step-3
    #Step-4: Design the query and Execute
    q="create table temp1 (tno number(2) primary key,tname varchar2(10) not null,sal number(5,2) not null)"
    cur.execute(q)
    print("Table created successfully")
except orc.DatabaseError as db:
    print("Problem on oracle database:",db)

