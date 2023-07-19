

from classes.user import User
from classes.employee import Employee
from classes.manager import Manager
from classes.project import Project

project1 = Project('Project 1', 'Description 1', '2023-01-01')
project1.save()


employee1 = Employee('MB', 'employee.1@company.com', '123-456-7890', 'Password!1', 'Title 1', 2)

    
employee1.save()


employee1.assign_to_project(10)
    
    






    
    