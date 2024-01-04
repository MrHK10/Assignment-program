def emp_asdd(em_name, emp_num, emp_salary, emp_add, emp_mar):
    dic = {'employee_name': em_name, 'employee_number': emp_num, "employee salary": emp_salary,
           "employee address": emp_add, "employee married": emp_mar}
    ep1.append(dic)
    print(f"Added new employee: {em_name}")
def save_to_file(file_name):
    with open(file_name, 'w') as file:
        for employee in ep1:
            file.write(f"Employee Name: {employee['employee_name']}\n")
            file.write(f"Employee Number: {employee['employee_number']}\n")
            file.write(f"Employee Salary: {employee['employee salary']}\n")
            file.write(f"Employee Address: {employee['employee address']}\n")
            file.write(f"Employee Married: {employee['employee married']}\n")
            file.write("\n")
print('Enter your choice')
ep1 = []
while True:
    print('Enter 1 to add an employee')
    print('Enter 2 to display employee list')
    print('Enter 3 to save employee list to file and exit')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        while True:
            em_name = input('Enter employee name: ')
            emp_num = int(input('Enter employee number: '))
            emp_salary = float(input('Enter employee salary: '))
            emp_add = input('Enter employee address: ')
            emp_mar = input("Is the employee married? (True or False): ")
            
            # Convert input to boolean
            emp_mar = True if emp_mar.lower() == 'true' else False
            
            emp_asdd(em_name, emp_num, emp_salary, emp_add, emp_mar)

            add_another = input("Do you want to add another user? (yes/y or no/n): ").lower()
            if add_another in ('no', 'n'):
                break
            elif add_another not in ('yes', 'y'):
                print("Invalid input. Please enter 'yes' or 'no'.")

    elif choice == 2:
        if not ep1:
            print("Employee list is empty.")
        else:
            print("Employee List:")
            for employee in ep1:
                print(employee['employee_name'])

    elif choice == 3:
        if not ep1:
            print("Employee list is empty.")
        else:
            file_name = input("Enter the file name to save employee details (e.g., employees.txt): ")
            save_to_file(file_name)
            print(f"Employee details saved to {file_name}")
            print(ep1)
        print("Exiting...")
        break

    else:
        print('Invalid choice. Please enter 1, 2, or 3')
