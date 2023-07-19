from classes.user import User
import sqlite3

DATABASE_URL = "app.db"
class Manager(User): 
                    # project_id INTEGER,
                # # FOREIGN KEY (project_id) REFERENCES projects(id),
                # employee_id INTEGER
                # # FOREIGN KEY (employee_id) REFERENCES employees(id) 
    #List of managers
    all = []
    #Should I add employee and projects?
    @classmethod
    def create_table(cls):
        query = """
                create table if not exists managers(
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

    def __init__(self, name, email, phone, password, title, tenure, is_assigned_project = 1, id=None):
        super().__init__(name, email, phone, password, id)
        self.is_assigned_project = is_assigned_project
        self.title = title
        self.tenure = tenure
        # self.project = project
        # self.employee = employee
        #Inherited User Id?
        Manager.all.append(self)
    
    def get_category(self):
        return "manager"  # Default category

    def save(self):
        self.create_table()
        super().save()
        query = """
                insert into managers(name, email, phone, password, title, tenure, is_assigned_project, category) values(?,?,?,?, ?, ?, ?, ?);
                """
        conn = sqlite3.connect(DATABASE_URL)
        cursor = conn.cursor()
        try:
            cursor.execute(query, (self.name, self.email, self.phone, self.password, self.title, self.tenure, self.is_assigned_project, self.get_category()))
            conn.commit()
            print("Manager inserted successfully!")
        except sqlite3.Error as e:
            print("Error inserting user into database:", str(e))
        finally:
            conn.close()       

    #Python Constraints on the uninherited manager keys
    @property
    def is_assigned_project(self):
        return self._is_assigned_project
    
    @is_assigned_project.setter
    def is_assigned_project(self, is_assigned_project):
        if (type(is_assigned_project) == int) and is_assigned_project== 0 or is_assigned_project == 1:
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

    # @property
    # def employee(self): 
    #     return self._employee
    
    # @employee.setter 
    # def employee(self, employee):
    #     from employee import Employee
    #     if type(employee) == Employee: 
    #         self._employee = employee
    #     else: 
    #         raise ValueError('Must be type manager')

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

        
    

#Test Area
    def __str__(self):
        return f"|||You have selected: {self.name}|||Email: {self.email}|||Phone: {self.phone}|||Assigned Project: {self.is_assigned_project}|||Title: {self.title}|||Tenure: {self.tenure}"

# goofy = Manager("Goofy the Dog", "goof.goofy@company.com","123-456-7890","Password!1", "Head Goof", 23)
# goofy.save()
# print(goofy)
# # print(goofy.id)