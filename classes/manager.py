from classes.user import User
from tabulate import tabulate

import sqlite3

DATABASE_URL = "app.db"


class Manager(User):
    # project_id INTEGER,
    # # FOREIGN KEY (project_id) REFERENCES projects(id),
    # employee_id INTEGER
    # # FOREIGN KEY (employee_id) REFERENCES employees(id)
    # List of managers
    all = []
    # Should I add employee and projects?

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

        query = """ 
                create table if not exists managers_projects(
                id integer primary key, 
                manager_id integer,
                project_id integer, 
                foreign key (manager_id) references managers(id),
                foreign key (project_id) references projects(id)         
                );
                """
        cursor.execute(query)
        conn.commit()
        conn.close()

    def __init__(self, name, email, phone, password, title, tenure, is_assigned_project=None, id=None):
        super().__init__(name, email, phone, password, id)
        self.is_assigned_project = is_assigned_project
        self.title = title
        self.tenure = tenure
        # self.project = project
        # self.employee = employee
        self.id = id
        self.projects = []
        self.all.append(self)

    def get_category(self):
        return "manager"  # Default category

    def assign_a_project_to_manager(self, project_id):
        conn = sqlite3.connect(DATABASE_URL)
        cursor = conn.cursor()
        self.projects.append(project_id)
        # print(self.id)
        # print(project_id)

        query = """ 
                update managers set is_assigned_project = ? where id = ? ; 
                """
        cursor.execute(query, (project_id, self.id))
        conn.commit()

        # self.is_assigned_project = project_id
        # print(self.is_assigned_project)

        query = """
                select * from managers_projects where manager_id = ? and project_id = ?;
                """
        result = cursor.execute(query, (self.id, self.is_assigned_project)).fetchone()

        # print(result)
        if result:
            # print("hi")
            query = """
                    update managers_projects set manager_id = ?, project_id = ? where manager_id = ? and project_id = ?; 
                """
            cursor.execute(query, (self.id, project_id, self.id, self.is_assigned_project))

        else:
            query = """
                    INSERT INTO managers_projects (manager_id, project_id) VALUES (?, ?);
                """
            cursor.execute(query, (self.id, project_id))
        self.is_assigned_project = project_id
        conn.commit()

        conn.close()

    def save(self):
        conn = sqlite3.connect(DATABASE_URL)
        cursor = conn.cursor()

        query = "SELECT name FROM sqlite_master WHERE type='table' AND name='users';"
        cursor.execute(query)
        table_exists = cursor.fetchone()

        if not table_exists:
            super().create_table()

        super().save()
        query = """
                insert into managers(name, email, phone, password, title, tenure, is_assigned_project, category) values(?,?,?,?, ?, ?, ?, ?);
                """

        try:
            cursor.execute(query, (self.name, self.email, self.phone, self.password,
                           self.title, self.tenure, self.is_assigned_project, self.get_category()))
            conn.commit()
            self.id = cursor.lastrowid

            if self.is_assigned_project:
                if self.projects:
                    association_query = "INSERT INTO managers_projects (manager_id, project_id) VALUES (?, ?)"
                for project_id in self.projects:
                    cursor.execute(association_query, (self.id, project_id))
                conn.commit()

            print("Manager inserted successfully!")
        except sqlite3.Error as e:
            print("Error inserting user into database:", str(e))
        finally:
            conn.close()

    # Python Constraints on the uninherited manager keys
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

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title
        # if not (type(title) == str):
        #     raise Exception("Please enter a title of string format")
        # self._title = title

    @property
    def tenure(self):
        return self._tenure

    @tenure.setter
    def tenure(self, tenure):
        self._tenure = tenure
        # if not (type(tenure) == int) and tenure > 0:
        #     raise Exception("Tenure must be a valid integer greater than 0.")
        # self._tenure = tenure

    def add_project(name, description, date_started):
        from classes.project import Project
        new_project = Project(name, description, date_started)
        new_project.save()

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

    # function for manager to add a new employee to db

    def add_employee(name, email, phone, password, title, tenure):
        from classes.employee import Employee
        new_employee = Employee(name, email, phone, password, title, tenure)
        new_employee.save()

    def print_all_employees():
        conn = sqlite3.connect(DATABASE_URL)
        cursor = conn.cursor()
        query = """
                select * from employees order by id asc; 
                """

        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()

        if result:
            all_employees_data = []
            for employee in result:
                employee_id, name, email, phone, password, title, tenure, *_ = employee
                all_employees = [
                    ["Employee ID: ", employee_id],
                    ["Name: ", name],
                    ["Email: ", email],
                    ["Phone: ", phone],
                    ["Title: ", title],
                    ["Tenure: ", tenure]
                ]
                all_employees_data.extend(all_employees)
                all_employees_data.append(['############', '############'])

            table = tabulate(all_employees_data, headers=[
                             "Attribute", "Employee"], tablefmt="grid")
        else:
            table = ('No Employees in the database')

        print(table, '\n\n')

    def add_manager(name, email, phone, password, title, tenure):
        new_manager = Manager(name, email, phone, password, title, tenure)
        new_manager.save()

    def print_all_managers():
        conn = sqlite3.connect(DATABASE_URL)
        cursor = conn.cursor()
        query = """
                select * from managers order by id asc; 
                """

        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()

        if result:
            all_managers_data = []
            for manager in result:
                employee_id, name, email, phone, password, title, tenure, *_ = manager
                all_managers = [
                    ["Manager ID: ", employee_id],
                    ["Name: ", name],
                    ["Email: ", email],
                    ["Phone: ", phone],
                    ["Title: ", title],
                    ["Tenure: ", tenure]
                ]
                all_managers_data.extend(all_managers)
                all_managers_data.append(['############', '############'])

            table = tabulate(all_managers_data, headers=[
                             "Attribute", "Manager"], tablefmt="grid")
        else:
            table = ('No Managers in the database')

        print(table, '\n\n')

    def update_manager_attributes(manager_id, new_attributes):
        conn = sqlite3.connect(DATABASE_URL)
        cursor = conn.cursor()
        query = """ 
                select * from managers where id = ?; 
        
                """
        cursor.execute(query, (manager_id,))
        exists = cursor.fetchone()
        if exists:
            for key, value in new_attributes.items():
                cursor.execute(
                    f'UPDATE managers SET {key} = ? WHERE id = ?', (value, manager_id))

            conn.commit()
            # print(f"Attributes updated for ID {manager_id}:")

            cursor.execute(
                'SELECT * FROM managers WHERE id = ?', (manager_id,))
            updated_manager_data = cursor.fetchone()
            headers = ["ID", "Name", "Email", "Phone", "Password",
                           "Title", "Tenure", "Is Assigned Project", "Category"]
            print("\n\n Here's the Manager you updated\n")
            print(tabulate([updated_manager_data],
                    headers=headers, tablefmt="grid"))
            print('\n\n')
        else:
            print(f"manager with ID {manager_id} not found in the table.")

        conn.close()
        
        
    def update_employee_attributes(employee_id, new_attributes):
            conn = sqlite3.connect(DATABASE_URL)
            cursor = conn.cursor()
            query = """ 
                    select * from employees where id = ?; 
            
                    """
            cursor.execute(query, (employee_id,))
            exists = cursor.fetchone()
            if exists:
                for key, value in new_attributes.items():
                    cursor.execute(
                        f'UPDATE employees SET {key} = ? WHERE id = ?', (value, employee_id))

                conn.commit()
                cursor.execute(
                    'SELECT * FROM employees WHERE id = ?', (employee_id,))
                updated_employee_data = cursor.fetchone()
                headers = ["ID", "Name", "Email", "Phone", "Password",
                            "Title", "Tenure", "Is Assigned Project", "Category"]
                print("\n\n Here's the Employee you updated\n")
                print(tabulate([updated_employee_data],
                        headers=headers, tablefmt="grid"))
                print('\n\n')
            else:
                print(f"employee with ID {employee_id} not found in the table.")

            conn.close()

    def update_project_attributes(project_id, new_attributes):
            conn = sqlite3.connect(DATABASE_URL)
            cursor = conn.cursor()
            query = """ 
                    select * from projects where id = ?; 
            
                    """
            cursor.execute(query, (project_id,))
            exists = cursor.fetchone()
            if exists:
                for key, value in new_attributes.items():
                    cursor.execute(
                        f'UPDATE projects SET {key} = ? WHERE id = ?', (value, project_id))

                conn.commit()
                cursor.execute(
                    'SELECT * FROM projects WHERE id = ?', (project_id,))
                updated_project_data = cursor.fetchone()
                headers = ["ID", "Name", "Description", "Date Started"]
                print("\n\n Here's the Project you updated\n")
                print(tabulate([updated_project_data],
                        headers = headers, tablefmt="grid"))
                print('\n\n')
            else:
                print(f"project with ID {project_id} not found in the table.")

            conn.close()
            
    def remove_employee(employee_id): 
        conn = sqlite3.connect(DATABASE_URL)
        cursor = conn.cursor()
        query = """
                delete from employees where id = ?; 
        
                """
                
        cursor.execute(query, (employee_id,))
        conn.commit()
        print(f'\n\nThe employee with id {employee_id} has been deleted\n\n')
        conn.close()
        
    def remove_manager(manager_id): 
        conn = sqlite3.connect(DATABASE_URL)
        cursor = conn.cursor()
        query = """
                delete from managers where id = ?; 
        
                """
                
        cursor.execute(query, (manager_id,))
        conn.commit()
        print(f'\n\nThe manager with id {manager_id} has been deleted\n\n')
        conn.close()
        
    def remove_project(project_id): 
        conn = sqlite3.connect(DATABASE_URL)
        cursor = conn.cursor()
        query = """
                delete from projects where id = ?; 
        
                """
                
        cursor.execute(query, (project_id,))
        conn.commit()
        print(f'\n\nThe project with id {project_id} has been deleted\n\n')
        conn.close()
        
        
    

    def print_all_projects():
        conn = sqlite3.connect(DATABASE_URL)
        cursor = conn.cursor()
        query = """
                select * from projects order by id asc; 
                """

        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()

        if result:
            all_projects_data = []
            for project in result:
                project_id, name, description, date_started, *_ = project
                all_projects = [
                    ["Project ID: ", project_id],
                    ["Project Name: ", name],
                    ["Description: ", description],
                    ["Date Started: ", date_started],
                ]
                all_projects_data.extend(all_projects)
                all_projects_data.append(['############', '############'])

            table = tabulate(all_projects_data, headers=[
                             "Attribute", "Project"], tablefmt="grid")
        else:
            table = ('No Projects in the database')

        print(table, '\n\n')

    def __str__(self):
        return f"|||You have selected: {self.name}|||Email: {self.email}|||Phone: {self.phone}|||Assigned Project: {self.is_assigned_project}|||Title: {self.title}|||Tenure: {self.tenure}"
