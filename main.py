from classes.user import User
from classes.employee import Employee
from classes.manager import Manager
from classes.project import Project
from tabulate import tabulate
import sqlite3
DATABASE_URL = 'app.db'


## employee crud functions begin

def manager_add_employee_main():
    new_employee_attributes = ['name', 'email', 'phone', 'password', 'title', 'tenure']
    inputs = {}
    for attribute in new_employee_attributes:
        inputs[attribute] = input(f'Please enter employee {attribute}: ')
    Manager.add_employee(**inputs)
    print('\n\nAn Employee has been added to the database!\n\nHere is the employee you entered\n\n')
    print_added_employee()
    # Manager.add_employee("Goofy the Dog", "goof.goofy@company.com", "123-456-7890", "Password!1", "Head Goof", 23)
    
##function to output the last employee that was just entered
def print_added_employee():
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    query = """
            select * from employees order by id desc limit 1; 
            """
            
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    
    if result: 
        employee_id, name, email, phone, password, title, tenure, *_ = result
        last_employee = [
            ["Employee ID: ", employee_id],
            ["Name: ", name],
            ["Email: ", email],
            ["Phone: ", phone],
            ["Title: ", title],
            ["Tenure: ", tenure]
        ]
        table = tabulate(last_employee, headers=["Attribute", "Employee"], tablefmt="grid")
    else: 
        table = ('Employee entered not in database')
        
    print(table, '\n\n')
    
def print_all_employees_main():
    Manager.print_all_employees()
    
def update_employee_info_main(): 
    employee_id = int(input("Enter the ID of the employee you want to update: "))
    
    new_attributes = {}
    print('\n\n')
    new_attributes['name'] = input("Enter the new Name: ")
    new_attributes['email'] = input("Enter the new email: ")
    new_attributes['phone'] = input("Enter the new Phone: ")
    new_attributes['password'] = input("Enter the new Password: ")
    new_attributes['title'] = input("Enter the new Title: ")
    new_attributes['tenure'] = (input("Enter the new Tenure: "))
    new_attributes['is_assigned_project'] = (input("Assign or Unassign from a project: "))
    new_attributes['category'] = input("Enter the new category (demote or promote): ")

    Manager.update_employee_attributes(employee_id, new_attributes)




def remove_employee_main():
    employee_id = int(input("Enter the ID of the employee you want to delete: "))
    Manager.remove_employee(employee_id)
  
## employee crud functions end 




## manager crud functions begin
def manager_add_manager_main():
    new_manager_attributes = ['name', 'email', 'phone', 'password', 'title', 'tenure']
    inputs = {}
    for attribute in new_manager_attributes:
        inputs[attribute] = input(f'Please enter manager {attribute}: ')
    Manager.add_manager(**inputs)
    print('\n\nA Manager has been added to the database!\n\nHere is the manager you entered\n\n')
    print_added_manager()
    
def print_added_manager():
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    query = """
            select * from managers order by id desc limit 1; 
            """
            
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    
    if result: 
        employee_id, name, email, phone, password, title, tenure, *_ = result
        last_manager = [
            ["Manager ID: ", employee_id],
            ["Name: ", name],
            ["Email: ", email],
            ["Phone: ", phone],
            ["Title: ", title],
            ["Tenure: ", tenure]
        ]
        table = tabulate(last_manager, headers=["Attribute", "Manager"], tablefmt="grid")
    else: 
        table = ('Manager entered not in database')
        
    print(table, '\n\n')
    
    
def print_all_managers_main():
    Manager.print_all_managers()

def update_manager_info_main():
    manager_id = int(input("Enter the ID of the manager you want to update: "))
    
    new_attributes = {}
    print('\n\n')
    new_attributes['name'] = input("Enter the new Name: ")
    new_attributes['email'] = input("Enter the new email: ")
    new_attributes['phone'] = input("Enter the new Phone: ")
    new_attributes['password'] = input("Enter the new Password: ")
    new_attributes['title'] = input("Enter the new Title: ")
    new_attributes['tenure'] = (input("Enter the new Tenure: "))
    new_attributes['is_assigned_project'] = (input("Assign or Unassign from a project: "))
    new_attributes['category'] = input("Enter the new category (demote or promote): ")

    Manager.update_manager_attributes(manager_id, new_attributes)
    

def remove_manager_main():
    manager_id = int(input("Enter the ID of the manager you want to delete: "))
    Manager.remove_manager(manager_id)


## manager crud functions end 



## project crud functions triggered by manager 
    
def manager_add_projects_to_db_main(): 
    new_project_attributes = ['name', 'description', 'date_started']
    inputs = {}
    for attribute in new_project_attributes: 
        inputs[attribute] = input(f'Please enter project {attribute}: ')
    Manager.add_project(**inputs)
    print_add_project()
    
def print_add_project():
    query = """
            select * from projects order by id desc;
        """       
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()

    if result:
        project_id, name, description, date_started =result
        table_data = [
            ["Name", name],
            ["id", project_id],
            ["Description", description],
            ["Date Started", date_started],
        ]
        print('\n\n', tabulate(table_data, headers=["Attribute", "Project"], tablefmt="grid"), '\n\n')
    else:
        print("This project was not entered in the database")
        
def print_all_projects_main():
    Manager.print_all_projects()   
    
def manager_assign_project_to_employee_main():
    employee_id = int(input('Please enter Employee ID: '))  # Convert input to int if employee_id is an integer
    project_id = int(input('Please enter Project ID: '))  # Convert input to int if project_id is an integer
    
    # Find the employee instance based on the provided ID'
    employee_instance = None
    for employee in Employee.all:
        if employee.id == employee_id:
            employee_instance = employee

    if employee_instance:
        employee_instance.assign_a_project_to_employee(project_id)
        print(f"Project assigned to Employee {employee_instance.name} successfully!")
    else:
        print(f"Employee with ID {employee_id} not found.")

    query="""
            SELECT employees.name, projects.name as project_name
            FROM employees
            INNER JOIN employees_projects ON employees.id = employees_projects.employee_id
            INNER JOIN projects ON employees_projects.project_id = projects.id;
        """
    conn=sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    #conn.commit()
    conn.close()

    if result:
        name, project_name, *_ = result
    
        table_data = [
            ["name", name],
            ["project", project_name]
        ]
        for row in result:
            name, project_name = row
            table_data.append([name, project_name])
        table = tabulate(table_data, headers=["Employee Name", "Project"], tablefmt="grid")
    else:
        table = "There are no projects assigned"
    print(table)
    
    
def update_project_info_main(): 
    project_id = int(input("Enter the ID of the project you want to update: "))
    
    new_attributes = {}
    print('\n\n')
    new_attributes['name'] = input("Enter the new Name: ")
    new_attributes['description'] = input("Enter the new Description: ")
    new_attributes['date_started'] = input("Enter the new Start Date: ")
    

    Manager.update_project_attributes(project_id, new_attributes)
    
def remove_project_main():
    project_id = int(input("Enter the ID of the project you want to delete: "))
    Manager.remove_project(project_id)

## user interface begins    
def intro(): 
    print("\nWelcome to the Project Management App!\n\nHere's what you can do:\n\n")
    
def options():
    print("Press 1 to add an Employee:\nPress 2 to add a Manager:\nPress 3 to add a Project:\nPress 4 to assign a Manager to a Project:\nPress 5 to assign an Employee to a Project:\nPress 6 to Print all employees:\nPress 7 to Print all managers:\nPress 8 to Print all projects:\nPress 9 to Update Employee Details:\nPress 10 to Remove an Employee:\nPress 11 to Update Manager Details:\nPress 12 to Remove a Manager:\nPress 13 to Update Project Details:\nPress 14 to Remove a Project:\n\nType Exit to Exit:\n\n")

def continue_app():
    print('Enter Exit to Exit or Select an Option Above to Continue\n\n')  
                 
def main():
    intro()
    options() 
    while True: 
        option = input()
        if option.lower() == 'exit': exit()
        elif option == '1':
            print("\n*****Please Input new Employee's Info*****\n")
            try:
                manager_add_employee_main()
            except Exception as e:
                print(f"\n\nAn error occurred: {e}\n\n")
            options()
            continue_app()
        elif option == '2':
            print("\n*****Please Input new Manager's Info*****\n\n")
            try:
                manager_add_manager_main()
            except Exception as e:
                print(f"\n\nAn error occurred: {e}\n\n")
            options()
            continue_app()
        elif option == '3':
            print("\n*****Please Input new Project Info*****\n\n")
            try:
                manager_add_projects_to_db_main()
            except Exception as e:
                print(f"\n\nAn error occurred: {e}\n\n")
            options()
            continue_app()
        elif option =='5':
            print("\n*****Assign Employee to a Project*****\n\n")
            try:
                manager_assign_project_to_employee_main()
            except Exception as e:
                print(f"\n\nAn error occurred: {e}\n\n")
            options()
            continue_app()
        elif option == '6':
            print("\nHere's a list of all employees\n\n")
            try:
                print_all_employees_main()
            except Exception as e:
                print(f"\n\nAn error occurred: {e}\n\n")
            options()
            continue_app()
        elif option == '7':
            print("\nHere's a list of all managers\n\n")
            try:
                print_all_managers_main()
            except Exception as e:
                print(f"\n\nAn error occurred: {e}\n\n")
            options()
            continue_app()
        elif option == '8':
            print("\nHere's a list of all Projects\n\n")
            try:
                print_all_projects_main()
            except Exception as e:
                print(f"\n\nAn error occurred: {e}\n\n")
            options()
            continue_app()
        elif option == '9':
            print("\n*****Update Employee Info*****\n\n")
            try:
                update_employee_info_main()
            except Exception as e:
                print(f"\n\nAn error occurred: {e}\n\n")
            options()
            continue_app()
        elif option == '10':
            print("\n*****Remove an Employee*****\n\n")
            try:
                remove_employee_main()
            except Exception as e:
                print(f"\n\nAn error occurred: {e}\n\n")
            options()
            continue_app()
        elif option == '11':
            print("\n*****Update Manager Info*****\n\n")
            try:
                update_manager_info_main()
            except Exception as e:
                print(f"\n\nAn error occurred: {e}\n\n")
            options()
            continue_app()
        elif option == '12':
            print("\n*****Remove a Manager*****\n\n")
            try:
                remove_manager_main()
            except Exception as e:
                print(f"\n\nAn error occurred: {e}\n\n")
            options()
            continue_app()
        elif option == '13':
            print("\n*****Update Project Info*****\n\n")
            try:
                update_project_info_main()
            except Exception as e:
                print(f"\n\nAn error occurred: {e}\n\n")
            options()
            continue_app()
        elif option == '14':
            print("\n*****Remove a Project*****\n\n")
            try:
                remove_project_main()
            except Exception as e:
                print(f"\n\nAn error occurred: {e}\n\n")
            options()
            continue_app()   
        else:
            print(f'\n\n{option} is not a valid option!\nPlease select a valid option from below\n\n')
            options()
            continue_app()
            
            
main()



    
    






    
    