from user import User
import sqlite3

DATABASE_URL = "db/app.db"
class Employee(User):
    all = []

    @classmethod
    def create_table(cls):
        query = """
                create table if not exists employees(
                id integer primary key,
                name text, 
                email text, 
                phone text,
                password text,
                title text, 
                tenure integer,
                is_assigned_project integer,
                category text            
                );
                """

        conn = sqlite3.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()

        conn.close()
    
    def __init__(self, name, email, phone, password, title, tenure,  id=None, is_assigned_project=1):
        super().__init__(name, email, phone, password, id)
        self.title = title 
        self.tenure = tenure 
        # self.manager = manager
        # self.project = project
        self.is_assigned_project = is_assigned_project
        Employee.all.append(self)
    
    def get_category(self):
        return "employee"  # Default category

    def save(self):
        self.create_table()
        super().save()
        query = """
                insert into employees(name, email, phone, password, title, tenure, is_assigned_project, category) values(?,?,?,?, ?, ?, ?, ?);
                """
        conn = sqlite3.connect(DATABASE_URL)
        cursor = conn.cursor()
        try:
            cursor.execute(query, (self.name, self.email, self.phone, self.password, self.title, self.tenure, self.is_assigned_project, self.get_category()))
            conn.commit()
            print("Employee inserted successfully!")
        except sqlite3.Error as e:
            print("Error inserting user into database:", str(e))
        finally:
            conn.close()    
        
        
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

    
    # @property
    # def manager(self): 
    #     return self._manager
    
    # @manager.setter 
    # def manager(self, manager):
    #     from manager import Manager
    #     if type(manager) == Manager: 
    #         self._manager = manager 
    #     else: 
    #         raise ValueError('manager must be of type Manager')
    
    @property
    def is_assigned_project(self):
        return self._is_assigned_project
    
    @is_assigned_project.setter
    def is_assigned_project(self, is_assigned_project):
        if (type(is_assigned_project) == int) and is_assigned_project== 0 or is_assigned_project == 1:
            self._is_assigned_project = is_assigned_project
        else:
            raise Exception("A Manager is either assigned (1) or not assigned (0). ")
        
    # @property
    # def project(self): 
    #     return self._project
    
    # @project.setter 
    # def project(self, project):
    #     from project import Project
    #     if type(project) == Project: 
    #         self._project = project 
    #     else: 
    #         raise ValueError('project must be of type Project') 
    
    ## implement when Project is implemented
        
    def __str__(self):
        return f"\n\n********************\n\nName: {self.name}\n\nEmail: {self.email}\n\nPhone: {self.phone}\n\nPassword: {self.password}\n\nTitle: {self.title}\n\nTenure: {self.tenure}\n\nManager:  \n\nProject: \n\n********************\n\n "
        
    
    
employee1 = Employee("EMployee","goof.goofy@company.com","123-456-7890","Password!1", "Head Goof", 23)   
employee1.save()
print(employee1) 


   
    
    