class User:
    all = []
    def __init__(self, name, email, phone, id = None):
        self.name = name
        self.email = email
        self.phone = phone
        self.all.append(self)
        self.id = id

    

    def __str__(self):
        return f"{self.name}, {self.email}, {self.phone}"
        



