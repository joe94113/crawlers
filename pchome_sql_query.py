import datetime
import mysql.connector

cnx = mysql.connector.connect(user='root',password='joe94113', database='pchome', host='127.0.0.1')
cursor = cnx.cursor()

query = ("SELECT * FROM products "
         "WHERE price > 5000")

cursor.execute(query)

for row in cursor:
    print(row)

cursor.close()
cnx.close()
