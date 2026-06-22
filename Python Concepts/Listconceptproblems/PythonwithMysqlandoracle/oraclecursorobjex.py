#OracleCursorObjEx.py
import oracledb as orc # Step-1
try:
    conobj=orc.connect("system/password@localhost:1522/orcl") # Step-2
    print("Python Program Got Commucation from Oracle DB")
    print("Type of conobj=", type(conobj))
    print("----------------------------------------")
    curobj=conobj.cursor() # Step-3
    print("Python Program Created Cursor Object")
    print("Type of curobj=",type(curobj))
    print("----------------------------------------")
except orc.DatabaseError as db:
    print("Problem in Oracle DB: ",db)