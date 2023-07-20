from classes.user import User
from classes.employee import Employee
from classes.manager import Manager
from classes.project import Project
import sqlite3
from tabulate import tabulate
DATABASE_URL = "app.db"

def intro(): 
    print("\nWelcome to the Project Management App!\n\nHere's what you can do:\n\n")
    
def options():
    print("Press 1 to add an Employee:\nPress 2 to add a Manager:\nPress 3 to add a Project:\nPress 4 to assign a Manager to a Project:\nPress 5 to assign an Employee to a Project:\n\nType Exit to Exit:\n\n")
    print("Type Below: ")

def manager_add_employee_main():
    new_employee_attributes = ['name', 'email', 'phone', 'password', 'title', 'tenure']
    inputs = {}
    for attribute in new_employee_attributes:
        inputs[attribute] = input(f'Please enter employee {attribute}: ')
    Manager.add_employee(**inputs)
    # Manager.add_employee("Goofy the Dog", "goof.goofy@company.com", "123-456-7890", "Password!1", "Head Goof", 23) 

def manager_add_manager_main():
    new_manager_attributes = ['name', 'email', 'phone', 'password', 'title', 'tenure']
    inputs = {}
    for attribute in new_manager_attributes:
        inputs[attribute] = input(f'Please enter manager {attribute}: ')
    #Manager.add_manager(**inputs)
    
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
        print(tabulate(table_data, headers=["Attribute", "Project"], tablefmt="grid"))
    else:
        print("This project was not entered in the database")


def manager_assign_project_to_employee_main():
    assign_project_emp_attributes = ['employee_id', 'project_id']
    employee_id = input('Please enter Employee ID: ')
    project_id = input('Please enter Project ID: ')
    Employee.assign_a_project_to_employee(int(employee_id), int(project_id))


               
def main():
    intro()
    options() 
    while True: 
        option = input()
        if option.lower() == 'exit': exit()
        elif option == '1': 
            manager_add_employee_main()
            print('An Employee has been added to the database!\n\n')
            options()
        elif option =='3':
            manager_add_projects_to_db_main()
            print("")
            options()
        elif option =='5':
            manager_assign_project_to_employee_main()
            print("")
            options()
main()



# project1 = Project('Project 1', 'Description 1', '2023-01-01')
# project1.save()


# employee1 = Employee('MB', 'employee.1@company.com', '123-456-7890', 'Password!1', 'Title 1', 2)
# manager1 = Manager("Goofy the Dog", "goof.goofy@company.com","123-456-7890","Password!1", "Head Goof", 23)
# employee1.save()
# manager1.save()

# manager1.assign_a_project_to_manager(project1.id)

# Manager.add_employee('MwweweewewewewB', 'employee.1@company.com', '123-456-7890', 'Password!1', 'Title 1', '2000', 00)
# Manager.add_employee("Goofy the Dog", "goof.goofy@company.com","123-456-7890","Password!1", "Head Goof", 23)


# print(Employee.all[1])

# self, name, email, phone, password, title, tenure,  id=None, is_assigned_project=None
# manager1.assign_a_project_to_manager(25)


# employee1.assign_a_project_to_employee(project1.id)
# employee1.assign_a_project_to_employee(20)
# employee1.assign_a_project_to_employee(57)


    
    






    
    