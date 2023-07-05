import sqlite3
con=sqlite3.connect("employee.db")
print("database openend successfully")
con.execute("create table EmployeeDetails(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL,email TEXT UNIQUE NOT NULL, department TEXT NOT NULL, phone INTEGER)")
print("Table created successfully")

con.close()