import mysql.connector
def dropdb():
    try:
        con = mysql.connector.connect(host="localhost",user="root",password="password")
        cur=con.cursor()
        #drop a database from MYSQL"
        cur.execute("drop database batch4pm")
        print("database dropped from mysql--verify")
    except mysql.connector.DatabaseError as db:
        print("Problem in MYSQL:",db)

#Main Program
dropdb()