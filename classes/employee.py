from classes.user import User
class Employee(User):
    all = []
    
    def __init__(self, name, email, phone, password, title, tenure, manager, project, id=None, is_assigned_project=1):
        super().__init__(name, email, phone, password, id)
        self.title = title 
        self.tenure = tenure 
        self.manager = manager
        self.project = project
        self.is_assigned_project = is_assigned_project
        Employee.all.append(self)
        
        
    @property 
    def title(self): 
        return self._title 
    
    @title.setter
    def title(self, title): 
        if type(title) == str:
            self._title = title 
        else: 
            raise ValueError('Title must be be a string')
        
    @property 
    def tenure(self): 
        return self._tenure
    
    @tenure.setter
    def tenure(self, tenure):
        if type(tenure) == int and 1 <= tenure <= 100:
            self._tenure = tenure 
        else: 
            raise ValueError('Tenure must be an integer between 1 and 100')
    
    ## implement when Manager is implemented
    
    # @property
    # def manager(self): 
    #     return self._manager
    
    # @manager.setter 
    # def manager(self, manager):
    #     from classes.manager import Manager
    #     if type(manager) == Manager: 
    #         self._manager = manager 
    #     else: 
    #         raise ValueError('manager must be of type Manager')
    
    ## implement when Manager is implemented
    
    
    
    
    ## implement when Project is implemented
    # @property
    # def project(self): 
    #     return self._project
    
    # @project.setter 
    # def project(self, project):
    #     from classes.project import Project
    #     if type(project) == Project: 
    #         self._project = project 
    #     else: 
    #         raise ValueError('project must be of type Project') 
    
    ## implement when Project is implemented
        
    def __str__(self):
        return f"\n\n********************\n\nName: {self.name}\n\nEmail: {self.email}\n\nPhone: {self.phone}\n\nPassword: {self.password}\n\nTitle: {self.title}\n\nTenure: {self.tenure}\n\nManager: {self.manager}\n\nProject: {self.project}\n\n********************\n\n"
        
    
    
             
            
    
    
    
    
    