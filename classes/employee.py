from classes.user import User
import sqlite3

DATABASE_URL = "app.db"


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

        query = """
                CREATE TABLE IF NOT EXISTS employees_projects(
                id INTEGER PRIMARY KEY,
                employee_id INTEGER,
                project_id INTEGER,
                FOREIGN KEY (employee_id) REFERENCES employees(id),
                FOREIGN KEY (project_id) REFERENCES projects(id)
                );
                """
        cursor.execute(query)
        conn.commit()

        conn.close()

    def __init__(self, name, email, phone, password, title, tenure,  id=None, is_assigned_project=None):
        super().__init__(name, email, phone, password, id)
        self.title = title
        self.tenure = tenure
        # self.manager = manager
        # self.project = project
        self.projects = []
        self.id = id
        self.is_assigned_project = is_assigned_project
        self.all.append(self)

    def get_category(self):
        return "employee"  # Default category

    # adds a project to db

    def assign_a_project_to_employee(self, project_id):
        conn = sqlite3.connect(DATABASE_URL)
        cursor = conn.cursor()

        self.projects.append(project_id)
        query = "UPDATE employees SET is_assigned_project = ? WHERE id = ?;"
        cursor.execute(query, (project_id, self.id))
        conn.commit()

        query = "SELECT * FROM employees_projects WHERE employee_id = ? AND project_id = ?;"
        result = cursor.execute(query, (self.id, project_id)).fetchone()

        if result:
            query = "UPDATE employees_projects SET employee_id = ?, project_id = ? WHERE employee_id = ? AND project_id = ?;"
            cursor.execute(query, (self.id, project_id, self.id, project_id))
        else:
            query = "INSERT INTO employees_projects (employee_id, project_id) VALUES (?, ?);"
            cursor.execute(query, (self.id, project_id))

        self.is_assigned_project = project_id
        conn.commit()
        conn.close()


    def save(self):
        conn = sqlite3.connect(DATABASE_URL)
        cursor = conn.cursor()

        # Check if the users table exists, if not create it
        query = "SELECT name FROM sqlite_master WHERE type='table' AND name='users';"
        cursor.execute(query)
        table_exists = cursor.fetchone()

        if not table_exists:
            super().create_table()

        # Insert the employee into the users table
        super().save()

        # Insert the employee into the employees table
        query = """
                INSERT INTO employees(name, email, phone, password, title, tenure, is_assigned_project, category)
                VALUES(?,?,?,?,?,?,?,?);
                """

        try:
            cursor.execute(query, (self.name, self.email, self.phone, self.password,
                           self.title, self.tenure, self.is_assigned_project, self.get_category()))
            conn.commit()
            self.id = cursor.lastrowid  # Get the auto-generated employee_id

            # Insert associations into the employees_projects table

            if self.is_assigned_project:
                if self.projects:
                    association_query = "INSERT INTO employees_projects (employee_id, project_id) VALUES (?, ?)"
                for project_id in self.projects:
                    cursor.execute(association_query, (self.id, project_id))
                conn.commit()

            # print("Employee inserted successfully!")
        except sqlite3.Error as e:
            print("Error inserting user into database:", str(e))
        finally:
            conn.close()

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title
        # if type(title) == str:
        #     self._title = title
        # else:
        #     raise ValueError('Title must be be a string')

    @property
    def tenure(self):
        return self._tenure

    @tenure.setter
    def tenure(self, tenure):
        self._tenure = tenure
        # if type(tenure) == str:
        #     self._tenure = tenure
        # else:
        #     raise ValueError('Tenure must be an integer between 1 and 100')

    @property
    def is_assigned_project(self):
        return self._is_assigned_project

    @is_assigned_project.setter
    def is_assigned_project(self, is_assigned_project):
        self._is_assigned_project = is_assigned_project

        # if (type(is_assigned_project) == int) and is_assigned_project== 0 or is_assigned_project == 1:
        #     self._is_assigned_project = is_assigned_project
        # else:
        #     raise Exception("A Manager is either assigned (1) or not assigned (0). ")

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

    def __str__(self):
        return f"\n\n********************\n\nName: {self.name}\n\nEmail: {self.email}\n\nPhone: {self.phone}\n\nPassword: {self.password}\n\nTitle: {self.title}\n\nTenure: {self.tenure}\n\nManager:  \n\nProject: \n\n********************\n\n "
