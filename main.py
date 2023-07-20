from classes.user import User
from classes.employee import Employee
from classes.manager import Manager
from classes.project import Project

def intro(): 
    print("\nWelcome to the Project Management App!\n\nHere's what you can do:\n\n")
    
def options():
    print("Press 1 to add an Employee:\nPress 2 to add a Manager:\nPress 3 to add a Project:\nPress 4 to assign a Manager to a Project:\nPress 5 to assign an Employee to a Project:\n\nType Exit to Exit:\n\n")

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
    #Manager.add_project(**inputs)
        
def manager_assign_project_to_employee_main():
    assign_project_emp_attributes = ['employee_id', 'project_id']
    employee_id = input('Please enter Employee ID: ')
    project_id = input('Please enter Project ID: ')
    assign_a_project_to_employee(employee_id, project_id)
               
def main():
    intro()
    options() 
    while True: 
        option = input()
        if option.lower() == 'exit': exit()
        #elif option == '1': 
        else:
            manager_add_employee_main()
            print('An Employee has been added to the database!\n\n')
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


    
    






    
    