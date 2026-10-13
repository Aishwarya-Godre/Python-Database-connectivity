import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="college"
)

cursor = con.cursor()

cursor.execute("SELECT * FROM student")

rows = cursor.fetchmany(2)


print(rows)
cursor.fetchall()

cursor.close()
con.close()



output = [(1, 'Aishwarya', 'Pune'), (2, 'Rahul', 'Mumbai')]
