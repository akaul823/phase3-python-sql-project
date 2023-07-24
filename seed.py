from classes.employee import Employee
from classes.manager import Manager
from classes.project import Project
from faker import Faker
import sqlite3
from random import randint

DATABASE_URL = 'app.db'
faker = Faker()

def main(): 
    #load employee table
    for i in range(100): 
        name = faker.name()
        email = f'{name.replace(" ", "").lower()}@company.com'
        employees=Employee(name, email, faker.phone_number(), 'password', 'swe', randint(1,100))
        employees.save()
        
    #load manager table 
    for j in range(100): 
        name = faker.name()
        email = f'{name.replace(" ", "").lower()}@company.com'
        managers=Manager(name, email, faker.phone_number(), 'password', 'swe', randint(1,100))
        managers.save()
        
    #load projects table
    for x in range(100): 
        # projects = Project((f'project {x}'), 'python cli app', 'today')
        project_name = faker.word()
        description = f'A python project for {project_name}'
        start_date = faker.date_between(start_date='-5y', end_date='today')
        projects = Project(project_name, description, start_date)
        projects.save()
        
main()

        
    