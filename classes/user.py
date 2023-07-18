import re #regex for password validation 
class User:
    all = []
    def __init__(self, name, email, phone, password, id = None):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
        self.all.append(self)
        self.id = id
        
    @property 
    def name(self): 
        return self._name 
    
    @name.setter 
    def name(self, name): 
        if type(name) == str and 1 < len(name) < 50:
            self._name = name
        else: 
            raise ValueError('Name must be a string and between 1 and 50 characters')

    @property 
    def email(self): 
        return self._email 
    
    @email.setter 
    def email(self, email):
        if (isinstance(email, str)) and ('.' in email) and ('@' in email) and ('company.com' in email):
            self._email = email
        else:
            raise ValueError('email must be a string and be in the format of lname.fname@company.com')
        
    @property
    def phone(self): 
        return self._phone 
    
    @phone.setter 
    def phone(self, phone): 
        if type(phone) == str and (phone.count('-') == 2) and phone.replace('-', '').isdigit():
            self._phone = phone
        else:
            raise ValueError('Phone must be a string in the format of 111-222-3333')
        
    @property
    def password(self): 
        return self._password
    
    @password.setter 
    def password(self, password):
        if type(password) == str and 8 <= len(password) <= 20 and re.search(r"\d", password) and re.search(r"[!@#$%^&*]", password) and re.search(r"[a-z]", password) and re.search(r"[A-Z]", password): 
            self._password = password 
        else:
            raise ValueError('Password must be a string and have 8-15 characters, 1 number and 1 special character, and 1 lowercase and 1 uppercase letter')
             
        
    # @property
    # def id(self): 
    #     return self._id 
    
    # @id.setter
    # def id(self, id): 
        
    def __str__(self):

        return f"\n\n********************\n\nName: {self.name}\n\nEmail: {self.email}\n\nPhone: {self.phone}\n\nPassword: {self.password}\n\n********************\n\n"
        



