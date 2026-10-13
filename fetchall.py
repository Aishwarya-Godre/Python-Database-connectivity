import mysql.connector
con = mysql.connector.connect (
    host= "localhost",
    user = "root",
    password = "",
    database = "college"
)

Cursor = con.cursor()
Cursor.execute("Select* from student")
rows  =  Cursor.fetchall()
for row in rows:
    print(row)
Cursor.close()
con.close()    





C:\Users\hp\Desktop\ NOTES>C:\Users\hp\AppData\Local\Programs\Python\Python314\python.exe "c:/Users/hp/Desktop/ NOTES/programmning/html/connected.py"
(1, 'Aishwarya', 'Pune')
(2, 'Rahul', 'Mumbai')
(3, 'Priya', 'Nashik')

C:\Users\hp\Desktop\ NOTES>  
