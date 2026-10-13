import mysql.connector
con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "college"
)

if con.is_connected():
    print("successfully Connected")
con.close()    