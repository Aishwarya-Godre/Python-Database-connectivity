
import mysql.connector
from mysql.connector import Error

con = None
cursor = None

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_MYSQL_PASSWORD",
        database="college"
    )

    cursor = con.cursor()

    query = """
    INSERT INTO student_demo (id, name, email, marks)
    VALUES (%s, %s, %s, %s)
    """

    values = (1, "Aishwarya", "aishwarya@example.com", 85)

    cursor.execute(query, values)
    con.commit()

    print("Record inserted successfully")

except Error as e:
    if con is not None and con.is_connected():
        con.rollback()
    print("Database error:", e)

finally:
    if cursor is not None:
        cursor.close()

    if con is not None and con.is_connected():
        con.close()
