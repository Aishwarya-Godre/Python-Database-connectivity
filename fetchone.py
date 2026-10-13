import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="college"
)

cursor = con.cursor()

cursor.execute("SELECT * FROM student")

row = cursor.fetchone()

print(row)
cursor.fetchall()

cursor.close()
con.close()



Output = (1, 'Aishwarya', 'Pune')
