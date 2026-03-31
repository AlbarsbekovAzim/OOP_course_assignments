import sqlite3
from employee import Employee

class EmployeeDAO:
    def __init__(self, db_name="employee_db.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS employee (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            position TEXT,
            salary REAL,
            hire_date TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    # CREATE
    def insert(self, employee: Employee):
        query = "INSERT INTO employee (name, position, salary, hire_date) VALUES (?, ?, ?, ?)"
        cursor = self.conn.cursor()
        cursor.execute(query, (employee.name, employee.position, employee.salary, employee.hire_date))
        self.conn.commit()
        employee.id = cursor.lastrowid
        return employee.id

    # READ by ID
    def get_by_id(self, id: int):
        query = "SELECT * FROM employee WHERE id=?"
        cursor = self.conn.cursor()
        cursor.execute(query, (id,))
        row = cursor.fetchone()

        if row:
            return Employee(*row)
        return None

    # READ ALL
    def get_all(self):
        query = "SELECT * FROM employee"
        cursor = self.conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()

        return [Employee(*row) for row in rows]

    # UPDATE
    def update(self, employee: Employee):
        query = """
        UPDATE employee
        SET name=?, position=?, salary=?, hire_date=?
        WHERE id=?
        """
        self.conn.execute(query, (employee.name, employee.position, employee.salary, employee.hire_date, employee.id))
        self.conn.commit()

    # DELETE
    def delete(self, id: int):
        query = "DELETE FROM employee WHERE id=?"
        self.conn.execute(query, (id,))
        self.conn.commit()