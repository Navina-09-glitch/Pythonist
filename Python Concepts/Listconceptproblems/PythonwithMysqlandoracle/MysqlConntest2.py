import mysql.connector
con = mysql.connector.connect(
    host='127.0.0.1',user="root",password="password")
print("Python program got connection from mysql DB")