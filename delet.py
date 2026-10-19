
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_MYSQL_PASSWORD",
    database="college"
)

cursor = con.cursor()

query = "DELETE FROM student WHERE id = %s"
values = (2,)

cursor.execute(query, values)

con.commit()

print("Records deleted:", cursor.rowcount)

cursor.close()
con.close()
