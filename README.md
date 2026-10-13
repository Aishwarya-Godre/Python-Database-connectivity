 <div align="center">

# 🐍 Python Database Connectivity (PDBC)

### Connecting Python with Databases

A hands-on repository dedicated to learning and practicing Python database connectivity, SQL queries, and database-driven applications.

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" />
</p>

</div>

---

## 📌 About This Repository

This repository contains my daily practice and hands-on work with Python Database Connectivity (PDBC).

The goal is to understand how Python applications communicate with databases, execute SQL queries, and manage database records efficiently.

## 🎯 Objectives

- Understand database connectivity using Python.
- Connect Python programs to a MySQL database.
- Execute SQL queries from Python.
- Perform CRUD operations.
- Handle database errors and exceptions.
- Build a strong foundation for database-driven applications.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application programming |
| MySQL | Relational database |
| SQL | Querying and managing data |
| MySQL Connector | Connecting Python to MySQL |
| VS Code | Development environment |
| Git & GitHub | Version control and code sharing |

## 📚 Topics Covered

- Database connectivity and configuration
- Establishing a database connection
- Creating cursors and executing queries
- `INSERT`, `SELECT`, `UPDATE`, and `DELETE`
- Fetching records using `fetchone()` and `fetchall()`
- Using parameterized queries
- Transaction management with `commit()` and `rollback()`
- Exception handling
- Closing database connections safely

## 💻 Sample Code

```python
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="practice_db"
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM employee")

for row in cursor.fetchall():
    print(row)

cursor.close()
connection.close()
```

> **Note:** Replace the database credentials with your own local configuration. Never upload real passwords or secret credentials to GitHub.

## ⚙️ Installation

Install the MySQL connector package:

```bash
pip install mysql-connector-python
```

Make sure MySQL Server is installed and running, and the database specified in your connection settings exists.

## 📂 Repository Structure

```text
PDBC-Daily-Practice/
│
├── README.md
├── connection.py
├── create_database.py
├── insert_records.py
├── fetch_records.py
├── update_records.py
├── delete_records.py
└── requirements.txt
```

*This is a suggested structure; add files as you create them.*

## 🚀 Learning by Building

The aim is to progress from basic database connections to small Python applications that store, retrieve, and update information in a database.

## 👩‍💻 Author

**Aishwarya Godre**

- GitHub: [Aishwarya-Godre](https://github.com/Aishwarya-Godre)
- LinkedIn: [Connect with me](https://www.linkedin.com/in/aishwarya-godre-0b9553334/)

---

<div align="center">

**Learn • Practice • Connect • Build**

⭐ Thank you for visiting this repository!

</div>
