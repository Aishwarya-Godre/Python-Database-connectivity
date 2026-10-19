
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_MYSQL_PASSWORD",
    database="college"
)

cursor = con.cursor()

query = "SELECT * FROM student WHERE city = %s"
values = ("Pune",)

cursor.execute(query, values)

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
con.close()
