class Project: 
    
    #every instance of a project will be appended into this list called all
    all = []
    def __init__(self, name, description, date_started, manager_id, employee_id, id = None):
        self.name = name
        self.description=description
        self.date_started = date_started
        self.manager_id = manager_id
        self.employee_id = employee_id
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
    def manager_id(self):
        return self._manager_id
    @manager_id.setter
    def manager_id(self, manager_id):
        if not(type(manager_id)==int) or manager_id < 1:
            raise Exception("Make sure you enter the manager id correctly")
        self._manager_id = manager_id

    @property
    def employee_id(self):
        return self._employee_id
    @employee_id.setter
    def employee_id(self, employee_id):
        if not(type(employee_id)==int) or employee_id < 1:
            raise Exception("Make sure you enter the manager id correctly")
        self._employee_id = employee_id

#Test Area
    def __str__(self):
        return f"|||You have selected: {self.name}|||Description: {self.description}|||Start Date: {self.date_started}|||Manager ID: {self.manager_id}|||Employee ID: {self.employee_id}"

    

    