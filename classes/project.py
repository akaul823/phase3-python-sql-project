class Project: 
    
    #every instance of a project will be appended into this list called all
    all = []
    def __init__(self, name, description, date_started, manager, employee, id = None):
        self.name = name
        self.description=description
        self.date_started = date_started
        self.manager= manager
        self.employee = employee
        self.all.append(self)
        self.id = id

    #Python Constraints on the project keys
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not(type(name)== str) and isinstance(name, "name"):
            raise Exception("Please enter a valid project name")
        self._name = name

    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, description):
        if not(type(description)==str):
            raise Exception("Please enter a valid project description")
        self._description = description
    
    @property
    def date_started(self):
        return self._date_started 
    @date_started.setter
    def date_started(self, date_started):
        if not(type(date_started)==str):
            raise Exception("Please enter the date as a string")
        self._date_started = date_started

    @property
    def manager(self):
        return self._manager
    @manager.setter
    def manager(self, manager):
        from manager import Manager
        if not(type(manager)== Manager):
            raise Exception("Make sure manager is an instance of manager")
        self._manager = manager

    @property
    def employee(self):
        return self._employee
    @employee.setter
    def employee(self, employee):
        from employee import Employee
        if not(type(employee)== Employee):
            raise Exception("Make sure employee is an instance of employee")
        self._employee = employee

#Test Area
    def __str__(self):
        return f"|||You have selected: {self.name}|||Description: {self.description}|||Start Date: {self.date_started}|||Manager ID: {self.manager_id}|||Employee ID: {self.employee_id}"

    

    