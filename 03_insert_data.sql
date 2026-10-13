
INSERT INTO students (id, name, city)
VALUES
(1, 'Aishwarya', 'Pune'),
(2, 'Rahul', 'Mumbai'),
(3, 'Priya', 'Nashik');
1146 (42S02): Table 'college.students' doesn't exist
mysql> Insert into student(id,name,city)
    -> values
    -> (1,'Aishwarya','Pune'),
    -> (2,'Rahul','Mumbai'),
    -> (3,'Priya','Nashik');
Query OK, 3 rows affected (0.07 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> select * from student;
+----+-----------+--------+
| ID | Name      | City   |
+----+-----------+--------+
|  1 | Aishwarya | Pune   |
|  2 | Rahul     | Mumbai |
|  3 | Priya     | Nashik |
+----+-----------+--------+
3 rows in set (0.00 sec)

mysql>
