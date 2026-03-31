from employee import Employee
from employee_dao import EmployeeDAO

def main():
    dao = EmployeeDAO()

    # print("=== INSERT ===")
    # emp = Employee(name="Ezmi", position="Warwar_rabbit", salary=100, hire_date="2020-01-01")
    # emp_id = dao.insert(emp)
    # print(f"Inserted Employee ID: {emp_id}")

    print("=== INSERT ===")
    emp = Employee(name="John Doe", position="Developer", salary=1200.5, hire_date="2025-01-10")
    emp_id = dao.insert(emp)
    print(f"Inserted Employee ID: {emp_id}")

    print("\n=== GET BY ID ===")
    emp = dao.get_by_id(emp_id)
    print(emp)

    print("\n=== GET ALL ===")
    employees = dao.get_all()
    for e in employees:
        print(e)

    print("\n=== UPDATE ===")
    emp.set_salary(2000)
    emp.set_position("Senior Developer")
    dao.update(emp)
    print("Updated:", dao.get_by_id(emp.id))

    print("\n=== DELETE ===")
    dao.delete(emp.id)
    print("After deletion:", dao.get_by_id(emp.id))


if __name__ == "__main__":
    main()