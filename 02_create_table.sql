
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    city VARCHAR(30)
);
se changed
mysql> create table student(ID int PRIMARY KEY,
    -> Name Varchar(50) Not Null,
    -> City Varchar(50));
Query OK, 0 rows affected (0.21 sec)

mysql> show tables;
+-------------------+
| Tables_in_college |
+-------------------+
| student           |
+-------------------+
1 row in set (0.04 sec)
