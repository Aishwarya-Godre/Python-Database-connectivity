
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_MYSQL_PASSWORD",
    database="college"
)

cursor = con.cursor()

query = """
SELECT city, COUNT(*)
FROM student
GROUP BY city
HAVING COUNT(*) > 2
"""

cursor.execute(query)

rows = cursor.fetchall()

for row in rows:
    print("City:", row[0], "| Students:", row[1])

cursor.close()
con.close()
