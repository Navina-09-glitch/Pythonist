#OracleConnTestEx2.py
import oracledb as orc # Step-1
try:
    conobj=orc.connect("system/password@127.0.0.1:1522/orcl") # Step-2
    print("Python Program Got Commucation from Oracle DB")
    print("Type of conobj=",type(conobj))
except orc.DatabaseError as db:
    print("Problem in Oracle db: ",db)