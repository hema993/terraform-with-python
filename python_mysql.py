import pymysql
import time
from prettytable import PrettyTable

# Wait for MySQL container to be ready
print("Waiting for MySQL to be ready...")
time.sleep(10)

# Connect to MySQL (update host if different)
connection = pymysql.connect(
    host="43.204.22.247",  # use '127.0.0.1' if Python is inside EC2 with MySQL container
    user="root",
    password="root",
    port=3306
)

cursor = connection.cursor()

# Create database and table
cursor.execute("CREATE DATABASE IF NOT EXISTS company;")
cursor.execute("USE company;")
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    role VARCHAR(50),
    salary INT
);
""")

# Insert dummy data
data = [
    ("Pavan", "DevOps Engineer", 60000),
    ("Vini", "Python Developer", 55000),
    ("Eswari", "Tester", 50000)
]
cursor.executemany("INSERT INTO employees (name, role, salary) VALUES (%s, %s, %s)", data)
connection.commit()

# Fetch data
cursor.execute("SELECT * FROM employees;")
rows = cursor.fetchall()

# Display data as table
table = PrettyTable()
table.field_names = ["ID", "Name", "Role", "Salary"]

for row in rows:
    table.add_row(row)

print("\nEmployee Table Data:\n----------------------")
print(table)

# Close connection
connection.close()
