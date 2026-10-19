
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_MYSQL_PASSWORD",
    database="college"
)

cursor = con.cursor()

query = "UPDATE student SET city = %s WHERE id = %s"
values = ("Mumbai", 1)

cursor.execute(query, values)

con.commit()

print("Records updated:", cursor.rowcount)

cursor.close()
con.close()
