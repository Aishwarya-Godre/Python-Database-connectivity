
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_MYSQL_PASSWORD",
    database="college"
)

cursor = con.cursor()

query = "SELECT * FROM student ORDER BY id DESC LIMIT 3"

cursor.execute(query)

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
con.close()
