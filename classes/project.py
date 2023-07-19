import sqlite3


DATABASE_URL = 'app.db'

class Project:

    # every instance of a project will be appended into this list called all
    all = []
     
    @classmethod
    def create_table(cls):
        query = """ 
                create table if not exists projects(
                    id integer primary key, 
                    name text,
                    description text, 
                    date_started text  
                );
                """

        conn = sqlite3.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()

    def __init__(self, name, description, date_started, id=None):
        self.name = name
        self.description = description
        self.date_started = date_started
        
        ###try out
        self.managers = []
        self.employees = []
        ###try out
        
        
        self.all.append(self)
        self.id = id

    def save(self):
        self.create_table()
        query = """ 
                insert into projects(name, description, date_started) values(?, ?, ?); 
        
        
                """
        conn = sqlite3.connect(DATABASE_URL)
        cursor = conn.cursor()
        try:
            cursor.execute(
                query, (self.name, self.description, self.date_started))
            conn.commit()
            print('Project inserted successfully!')
        except sqlite3.Error as e:
            print('Error inserting into database (projects table)', str(e))
        finally:
            conn.close()

    # Python Constraints on the project keys

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not (type(name) == str) and isinstance(name, "name"):
            raise Exception("Please enter a valid project name")
        self._name = name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if not (type(description) == str):
            raise Exception("Please enter a valid project description")
        self._description = description

    @property
    def date_started(self):
        return self._date_started

    @date_started.setter
    def date_started(self, date_started):
        if not (type(date_started) == str):
            raise Exception("Please enter the date as a string")
        self._date_started = date_started


    # get and set employee and manager of a project 
    
    ###try out
    # @property
    # def manager(self):
    #     return self._manager

    # @manager.setter
    # def manager(self, manager):
    #     from classes.manager import Manager
    #     if not (type(manager) == Manager):
    #         raise Exception("Make sure manager is an instance of manager")
    #     self._manager = manager

    # @property
    # def employee(self):
    #     return self._employee

    # @employee.setter
    # def employee(self, employee):
    #     from classes.employee import Employee
    #     if not (type(employee) == Employee):
    #         raise Exception("Make sure employee is an instance of employee")
    #     self._employee = employee
        
        
    def get_employees(self):
        return self.employees
    ###try out

# Test Area
    def __str__(self):
        return f"|||You have selected: {self.name}|||Description: {self.description}|||Start Date: {self.date_started}|||Manager: |||Employee: "


# project1 = Project('Project Manager Project', 'CRUD App', '07-18-23')
# project1.save()
# print(project1)
