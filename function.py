
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_MYSQL_PASSWORD",
    database="college"
)

cursor = con.cursor()

query = """
SELECT
    COUNT(*),
    SUM(marks),
    AVG(marks),
    MIN(marks),
    MAX(marks)
FROM student
"""

cursor.execute(query)

result = cursor.fetchone()

print("Total students:", result[0])
print("Total marks:", result[1])
print("Average marks:", result[2])
print("Minimum marks:", result[3])
print("Maximum marks:", result[4])

cursor.close()
con.close()
