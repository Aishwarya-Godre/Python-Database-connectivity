
CREATE DATABASE college;

USE college;

C:\Users\hp>mysql -u root -p
Enter password: **************
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 42
Server version: 8.0.45 MySQL Community Server - GPL

Copyright (c) 2000, 2026, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> create database collage;
ERROR 1007 (HY000): Can't create database 'collage'; database exists
mysql> CREATE DATABASE college;
Query OK, 1 row affected (0.08 sec)

mysql> use college
Database changed
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
