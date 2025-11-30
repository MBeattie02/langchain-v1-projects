"""
Create sample employees database for SQL agent testing
"""
import sqlite3
from datetime import datetime, timedelta
import random

# Connect to database (creates it if it doesn't exist)
conn = sqlite3.connect('db/employees.db')
cursor = conn.cursor()

# Create tables
print("Creating tables...")

# Departments table
cursor.execute('''
CREATE TABLE IF NOT EXISTS departments (
    department_id INTEGER PRIMARY KEY,
    department_name TEXT NOT NULL,
    location TEXT
)
''')

# Employees table
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    employee_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE,
    hire_date DATE,
    department_id INTEGER,
    job_title TEXT,
    manager_id INTEGER,
    FOREIGN KEY (department_id) REFERENCES departments(department_id),
    FOREIGN KEY (manager_id) REFERENCES employees(employee_id)
)
''')

# Salaries table
cursor.execute('''
CREATE TABLE IF NOT EXISTS salaries (
    salary_id INTEGER PRIMARY KEY,
    employee_id INTEGER,
    salary REAL,
    effective_date DATE,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
)
''')

# Projects table
cursor.execute('''
CREATE TABLE IF NOT EXISTS projects (
    project_id INTEGER PRIMARY KEY,
    project_name TEXT NOT NULL,
    department_id INTEGER,
    start_date DATE,
    end_date DATE,
    budget REAL,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
)
''')

# Employee_Projects junction table
cursor.execute('''
CREATE TABLE IF NOT EXISTS employee_projects (
    employee_id INTEGER,
    project_id INTEGER,
    role TEXT,
    hours_allocated INTEGER,
    PRIMARY KEY (employee_id, project_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
)
''')

print("✓ Tables created")

# Insert sample data
print("\nInserting sample data...")

# Departments
departments = [
    (1, 'Engineering', 'San Francisco'),
    (2, 'Sales', 'New York'),
    (3, 'Marketing', 'Los Angeles'),
    (4, 'Human Resources', 'Chicago'),
    (5, 'Finance', 'Boston'),
    (6, 'Customer Support', 'Austin')
]
cursor.executemany('INSERT OR REPLACE INTO departments VALUES (?, ?, ?)', departments)
print(f"✓ Inserted {len(departments)} departments")

# Employees
employees = [
    # Engineering
    (1, 'John', 'Smith', 'john.smith@company.com', '2020-01-15', 1, 'Engineering Manager', None),
    (2, 'Sarah', 'Johnson', 'sarah.johnson@company.com', '2020-03-20', 1, 'Senior Software Engineer', 1),
    (3, 'Michael', 'Williams', 'michael.williams@company.com', '2021-06-10', 1, 'Software Engineer', 1),
    (4, 'Emily', 'Brown', 'emily.brown@company.com', '2021-09-05', 1, 'Software Engineer', 1),
    (5, 'David', 'Jones', 'david.jones@company.com', '2022-02-14', 1, 'Junior Software Engineer', 2),

    # Sales
    (6, 'Jennifer', 'Garcia', 'jennifer.garcia@company.com', '2019-11-01', 2, 'Sales Director', None),
    (7, 'Robert', 'Miller', 'robert.miller@company.com', '2020-05-18', 2, 'Senior Sales Rep', 6),
    (8, 'Lisa', 'Davis', 'lisa.davis@company.com', '2021-01-22', 2, 'Sales Rep', 6),
    (9, 'James', 'Rodriguez', 'james.rodriguez@company.com', '2021-08-30', 2, 'Sales Rep', 6),

    # Marketing
    (10, 'Maria', 'Martinez', 'maria.martinez@company.com', '2020-07-12', 3, 'Marketing Manager', None),
    (11, 'Christopher', 'Hernandez', 'chris.hernandez@company.com', '2021-03-08', 3, 'Marketing Specialist', 10),
    (12, 'Amanda', 'Lopez', 'amanda.lopez@company.com', '2022-01-17', 3, 'Social Media Manager', 10),

    # HR
    (13, 'Daniel', 'Gonzalez', 'daniel.gonzalez@company.com', '2019-08-20', 4, 'HR Director', None),
    (14, 'Jessica', 'Wilson', 'jessica.wilson@company.com', '2020-10-05', 4, 'HR Specialist', 13),

    # Finance
    (15, 'Matthew', 'Anderson', 'matthew.anderson@company.com', '2019-12-10', 5, 'Finance Director', None),
    (16, 'Ashley', 'Thomas', 'ashley.thomas@company.com', '2020-09-14', 5, 'Financial Analyst', 15),
    (17, 'Joshua', 'Taylor', 'joshua.taylor@company.com', '2021-11-29', 5, 'Accountant', 15),

    # Customer Support
    (18, 'Nicole', 'Moore', 'nicole.moore@company.com', '2020-04-23', 6, 'Support Manager', None),
    (19, 'Andrew', 'Jackson', 'andrew.jackson@company.com', '2021-07-19', 6, 'Support Specialist', 18),
    (20, 'Stephanie', 'Martin', 'stephanie.martin@company.com', '2022-03-11', 6, 'Support Specialist', 18),
]
cursor.executemany('INSERT OR REPLACE INTO employees VALUES (?, ?, ?, ?, ?, ?, ?, ?)', employees)
print(f"✓ Inserted {len(employees)} employees")

# Salaries
salaries = [
    # Engineering (higher salaries)
    (1, 1, 145000, '2020-01-15'),
    (2, 2, 125000, '2020-03-20'),
    (3, 3, 95000, '2021-06-10'),
    (4, 4, 92000, '2021-09-05'),
    (5, 5, 75000, '2022-02-14'),

    # Sales
    (6, 6, 135000, '2019-11-01'),
    (7, 7, 95000, '2020-05-18'),
    (8, 8, 72000, '2021-01-22'),
    (9, 9, 70000, '2021-08-30'),

    # Marketing
    (10, 10, 105000, '2020-07-12'),
    (11, 11, 68000, '2021-03-08'),
    (12, 12, 65000, '2022-01-17'),

    # HR
    (13, 13, 115000, '2019-08-20'),
    (14, 14, 62000, '2020-10-05'),

    # Finance
    (15, 15, 140000, '2019-12-10'),
    (16, 16, 78000, '2020-09-14'),
    (17, 17, 68000, '2021-11-29'),

    # Customer Support
    (18, 18, 85000, '2020-04-23'),
    (19, 19, 52000, '2021-07-19'),
    (20, 20, 50000, '2022-03-11'),
]
cursor.executemany('INSERT OR REPLACE INTO salaries VALUES (?, ?, ?, ?)', salaries)
print(f"✓ Inserted {len(salaries)} salary records")

# Projects
projects = [
    (1, 'Cloud Migration', 1, '2023-01-01', '2023-12-31', 500000),
    (2, 'Mobile App Development', 1, '2023-03-15', '2024-03-15', 350000),
    (3, 'Q4 Sales Campaign', 2, '2023-10-01', '2023-12-31', 150000),
    (4, 'Brand Refresh', 3, '2023-06-01', '2024-01-31', 200000),
    (5, 'Employee Wellness Program', 4, '2023-01-01', '2023-12-31', 75000),
    (6, 'Financial Systems Upgrade', 5, '2023-04-01', '2023-10-31', 180000),
    (7, 'Customer Portal Redesign', 6, '2023-05-01', '2023-11-30', 120000),
]
cursor.executemany('INSERT OR REPLACE INTO projects VALUES (?, ?, ?, ?, ?, ?)', projects)
print(f"✓ Inserted {len(projects)} projects")

# Employee-Projects assignments
employee_projects = [
    # Cloud Migration
    (1, 1, 'Project Lead', 160),
    (2, 1, 'Senior Developer', 200),
    (3, 1, 'Developer', 200),

    # Mobile App
    (2, 2, 'Tech Lead', 180),
    (4, 2, 'Developer', 200),
    (5, 2, 'Junior Developer', 200),

    # Sales Campaign
    (6, 3, 'Campaign Director', 120),
    (7, 3, 'Sales Lead', 160),
    (8, 3, 'Sales Support', 160),

    # Brand Refresh
    (10, 4, 'Project Manager', 140),
    (11, 4, 'Marketing Specialist', 180),
    (12, 4, 'Social Media Lead', 160),

    # Wellness Program
    (13, 5, 'Program Director', 100),
    (14, 5, 'HR Coordinator', 150),

    # Financial Systems
    (15, 6, 'Finance Lead', 120),
    (16, 6, 'Systems Analyst', 180),
    (17, 6, 'Accountant', 160),

    # Customer Portal
    (18, 7, 'Product Owner', 140),
    (19, 7, 'Support Specialist', 120),
    (3, 7, 'Developer', 100),
]
cursor.executemany('INSERT OR REPLACE INTO employee_projects VALUES (?, ?, ?, ?)', employee_projects)
print(f"✓ Inserted {len(employee_projects)} project assignments")

# Commit and close
conn.commit()
print("\n✓ Database created successfully!")

# Display summary
cursor.execute("SELECT COUNT(*) FROM departments")
dept_count = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM employees")
emp_count = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM projects")
proj_count = cursor.fetchone()[0]

print(f"\nDatabase Summary:")
print(f"- {dept_count} departments")
print(f"- {emp_count} employees")
print(f"- {proj_count} projects")
print(f"- Location: db/employees.db")

conn.close()
