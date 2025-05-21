import os

file_name = "employees.txt"

class Employee:
    """Class to represent an employee"""
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name    
        self.position = position    
        self.salary = float(salary)

    def __str__(self):
        return (f"Employee ID: {self.employee_id}, Name: {self.name}, "
                f"Position: {self.position}, Salary: {self.salary:.2f}")

    def to_file_string(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary:.2f}"


class EmployeeManager:
    """Class to manage employee operations"""
    def __init__(self, file_name):
        self.file_name = file_name
        self.employees = []
        self.load_from_file()

    def load_from_file(self):
        """Load employees from file"""
        if not os.path.exists(self.file_name):
            return

        try:
            with open(self.file_name, "r") as file:
                for line in file:
                    if line.strip():
                        eid, name, position, salary = line.strip().split(", ")
                        self.employees.append(Employee(eid, name, position, salary))
        except Exception as e:
            print(f"Error loading file: {e}")

    def save_to_file(self):
        """Save all employees to file"""
        try:
            with open(self.file_name, "w") as file:
                for emp in self.employees:
                    file.write(emp.to_file_string() + "\n")
        except Exception as e:
            print(f"Error saving to file: {e}")

    def add_employee(self, employee):
        """Add new employee with unique ID check"""
        if any(emp.employee_id == employee.employee_id for emp in self.employees):
            raise ValueError(f"Employee ID {employee.employee_id} already exists.")
        self.employees.append(employee)

    def view_all_employees(self, sort_key=None):
        """Return list of all employees, optionally sorted"""
        if sort_key == "name":
            return sorted(self.employees, key=lambda e: e.name.lower())
        elif sort_key == "salary":
            return sorted(self.employees, key=lambda e: e.salary)
        return self.employees

    def search_employee(self, employee_id):
        """Search for an employee by ID"""
        for emp in self.employees:
            if emp.employee_id == employee_id:
                return emp
        raise ValueError(f"Employee with ID {employee_id} not found.")

    def update_employee(self, employee_id, name=None, position=None, salary=None):
        """Update employee details"""
        emp = self.search_employee(employee_id)
        if name:
            emp.name = name
        if position:
            emp.position = position
        if salary:
            emp.salary = float(salary)

    def remove_employee(self, employee_id):
        """Remove employee by ID"""
        emp = self.search_employee(employee_id)
        self.employees.remove(emp)


def main():
    manager = EmployeeManager(file_name)

    menu = """
----------------------------------
1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Sort and view employee records
7. Exit
"""
    while True:
        print(menu)
        try:
            choice = int(input("Enter your choice (1-7): ").strip())
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")
            continue

        if choice == 1:
            try:
                eid = input("Enter Employee ID: ").strip()
                name = input("Enter Name: ").strip()
                position = input("Enter Position: ").strip()
                salary = float(input("Enter Salary: ").strip())
                emp = Employee(eid, name, position, salary)
                manager.add_employee(emp)
                print("Employee added successfully.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == 2:
            employees = manager.view_all_employees()
            if not employees:
                print("No employee records found.")
            else:
                for emp in employees:
                    print(emp)

        elif choice == 3:
            eid = input("Enter Employee ID to search: ").strip()
            try:
                emp = manager.search_employee(eid)
                print(emp)
            except ValueError as e:
                print(e)

        elif choice == 4:
            eid = input("Enter Employee ID to update: ").strip()
            try:
                emp = manager.search_employee(eid)
                print(f"Current details: {emp}")
                name = input("Enter new name (leave blank to keep current): ").strip()
                position = input("Enter new position (leave blank to keep current): ").strip()
                salary = input("Enter new salary (leave blank to keep current): ").strip()
                manager.update_employee(
                    eid,
                    name if name else None,
                    position if position else None,
                    salary if salary else None
                )
                print("Employee updated successfully.")
            except ValueError as e:
                print(e)

        elif choice == 5:
            eid = input("Enter Employee ID to delete: ").strip()
            try:
                manager.remove_employee(eid)
                print("Employee deleted successfully.")
            except ValueError as e:
                print(e)

        elif choice == 6:
            sort_key = input("Sort by 'name' or 'salary': ").strip().lower()
            if sort_key not in ("name", "salary"):
                print("Invalid sort key.")
                continue
            employees = manager.view_all_employees(sort_key=sort_key)
            for emp in employees:
                print(emp)

        elif choice == 7:
            manager.save_to_file()
            print("All records saved. Exiting.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
