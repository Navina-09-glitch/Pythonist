#Program for creating the database on the name of "batch11am"
#MySQLDatabaseCreateEx.py
import mysql.connector
def createdb():
    try:
        con = mysql.connector.connect(host="localhost",user="root",password="password")
        cur=con.cursor()
        #create a Database on the name of "batch7pm"
        dc="create database batch11am"
        cur.execute(dc)
        print("database created in mysql--verify")
    except mysql.connector.DatabaseError as db:
        print("Problem in MYSQL",db)

#Main Program
createdb()