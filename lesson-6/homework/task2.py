import os

if not os.path.exists('employees.txt'):
    open('employees.txt', 'w').close()

def add_new_record(employee_id, name, position, salary):
    with open('employees.txt', 'a') as file:
        file.write(f'{employee_id}, {name}, {position}, {salary}\n')
    print("Record added successfully.")

def view_records():
    if not os.path.exists('employees.txt') or os.stat('employees.txt').st_size == 0:
        print("No employee records found.")
        return

    with open('employees.txt', 'r') as file:
        records = file.readlines()
        print("\nEmployee Records:")
        for record in records:
            print(record.strip())

def search_by_employee_id(employee_id):
    found = False
    with open('employees.txt', 'r') as file:
        records = file.readlines()
        for record in records:
            fields = [f.strip() for f in record.strip().split(',')]
            if fields[0] == str(employee_id):
                print("\nEmployee Found:")
                print(record.strip())
                found = True
                break
    if not found:
        print("Employee ID not found.")

def update_information(employee_id, name=None, position=None, salary=None):
    updated = False
    with open('employees.txt', 'r') as file:
        records = file.readlines()

    with open('employees.txt', 'w') as file:
        for record in records:
            fields = [field.strip() for field in record.strip().split(',')]
            if fields[0] == str(employee_id):
                if name:
                    fields[1] = name
                if position:
                    fields[2] = position
                if salary:
                    fields[3] = str(salary)
                updated = True
                record = ', '.join(fields) + '\n'
            else:
                record = ', '.join(fields) + '\n'
            file.write(record)

    if updated:
        print(f"Employee {employee_id} updated successfully.")
    else:
        print("Employee ID not found.")

def delete_record(employee_id):
    deleted = False
    with open('employees.txt', 'r') as file:
        records = file.readlines()

    with open('employees.txt', 'w') as file:
        for record in records:
            fields = [field.strip() for field in record.strip().split(',')]
            if fields[0] != str(employee_id):
                file.write(', '.join(fields) + '\n')
            else:
                deleted = True

    if deleted:
        print(f"Employee {employee_id} deleted successfully.")
    else:
        print("Employee ID not found.")

def exit_program():
    print("Exiting the program.")
    exit()

def main():
    while True:
        print("\n--- Employee Records Manager ---")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            eid = input("Enter Employee ID: ").strip()
            name = input("Enter Name: ").strip()
            position = input("Enter Position: ").strip()
            salary = input("Enter Salary: ").strip()
            add_new_record(eid, name, position, salary)

        elif choice == '2':
            view_records()

        elif choice == '3':
            eid = input("Enter Employee ID to search: ").strip()
            search_by_employee_id(eid)

        elif choice == '4':
            eid = input("Enter Employee ID to update: ").strip()
            name = input("Enter new Name (leave blank to skip): ").strip()
            position = input("Enter new Position (leave blank to skip): ").strip()
            salary = input("Enter new Salary (leave blank to skip): ").strip()
            update_information(
                eid,
                name if name else None,
                position if position else None,
                salary if salary else None
            )

        elif choice == '5':
            eid = input("Enter Employee ID to delete: ").strip()
            delete_record(eid)

        elif choice == '6':
            exit_program()

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

main()
