from user import User
class Manager(User): 
    
    #List of managers
    all = []
    #Should I add employee and projects?
    def __init__(self, name, email, phone, title, tenure,is_assigned_project = 0, id=None):
        super().__init__(name, email, phone, id)
        self.is_assigned_project = is_assigned_project
        self.title = title
        self.tenure = tenure
        #Inherited User Id?
        Manager.all.append(self)

    #Python Constraints on the uninherited manager keys
    @property
    def is_assigned_project(self):
        return self._is_assigned_project
    
    @is_assigned_project.setter
    def is_assigned_project(self, is_assigned_project):
        if (type(is_assigned_project) == int):
            self._is_assigned_project = is_assigned_project
        else:
            raise Exception("A Manager is either assigned (1) or not assigned (0). ")
    
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        if not (type(title) == str):
            raise Exception("Please enter a title of string format")
        self._title = title
    
    @property
    def tenure(self):
        return self._tenure
    @tenure.setter
    def tenure(self, tenure):
         if not (type(tenure) == int) and tenure > 0:
            raise Exception("Tenure must be a valid integer greater than 0.")
         self._tenure = tenure

        
    

#Test Area
    def __str__(self):
        return f"|||You have selected: {self.name}|||Email: {self.email}|||Phone: {self.phone}|||Assigned Project: {self.is_assigned_project}|||Title: {self.title}|||Tenure: {self.tenure}"

# goofy = Manager("Goofy the Dog", "goofy@gmail.com","123-456-7890", "Head Goof", 23)
# print(goofy)
# print(goofy.id)