
from classes.user import User
from classes.employee import Employee

##test user class 
avi = User("Avi Kaul", "email.email@company.com", "111-222-3333", 'Password1!')
print(avi)

## test employee class

#def __init__(self, name, email, 
# phone, password, title, 
# tenure, manager, project, 
# id=None, is_assigned_project=1):

employee1 = Employee("Mordechai Bronfin", "email.email@company.com", "111-222-3333", 'Password1!', 'Software Engineer', 2, 'Manager', 'This Project')

employee2 = Employee("Mordechai Bronfin", "email.email@company.com", "111-222-3333", 'Password1!', 'Software Engineer', 2, 'Manager', 'This Project')

#print(list([e for e in Employee.all]))

print(employee1, employee2)

def main():
    pass



    
    