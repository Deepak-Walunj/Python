# class Person:
#     def __init__(self, name, age, city):
#         self.name=name
#         self.age=age
#         self.city=city
        
#     def showPerson(self):
#         print(f"Person Details:\nName: {self.name}\nAge: {self.age}\nCity: {self.city}")

# class Tester(Person):
#     def __init__(self, name, age, city, position):
#         super().__init__(name, age, city)
#         self.position=position
        
#     def showTester(self):
#         print(f"Tester Details:\nName: {self.name}\nAge: {self.age}\n Position: {self.position}")

# class Programmer(Person):
#     def __init__(self, name, age, city, lang):
#         super().__init__(name, age, city)
#         self.lang=lang
        
#     def showProgrammer(self):
#         print(f"Programmer Details:\nName: {self.name}\nAge: {self.age}\n Language: {self.lang}")

# class Emp(Tester, Programmer):
#     def __init__(self, name, age, city,emp_id,role,position=None,lang=None):
#         super().__init__(name,age,city)
#         self.emp_id=emp_id
#         self.role=role
#         if role.lower()=="programmer":
#             Programmer.__init__(self, name, age, city, lang)
#         elif role.lower()=="tester":
#             Tester.__init__(self, name, age, city, position)
        
#     def showEmp(self):
#         print(f"Employee Details:\nName: {self.name}\nAge: {self.age}\nField: {self.role}") 
#         if self.role.lower()=="programmer":
#             print(f"Language: {self.lang}")
#         elif self.role.lower()=="tester":
#             print(f"Position: {self.position}")
            
# e1=Emp("abc",20,"pune",234,"Tester",position="QA")
# e1.showEmp()

# e2=Emp("xyz",30,"Bombay",567,"programmer",lang="py")
# e2.showEmp()
# e2.showPerson()
# e2.showTester()

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        
    def showPerson(self):
        print(f"Person Details:\nName: {self.name}\nAge: {self.age}\nCity: {self.city}")

class Tester(Person):
    def __init__(self, name, age, city, position):
        super().__init__(name, age, city)
        self.position = position
        
    def showTester(self):
        print(f"Tester Details:\nName: {self.name}\nAge: {self.age}\nPosition: {self.position}")

class Programmer(Person):
    def __init__(self, name, age, city, lang):
        super().__init__(name, age, city)
        self.lang = lang
        
    def showProgrammer(self):
        print(f"Programmer Details:\nName: {self.name}\nAge: {self.age}\nLanguage: {self.lang}")

class Emp(Person):
    def __init__(self, name, age, city, emp_id, role, position=None, lang=None):
        super().__init__(name, age, city)
        self.emp_id = emp_id
        self.role = role
        if role.lower() == "programmer":
            Programmer.__init__(self, name, age, city, lang)
        elif role.lower() == "tester":
            Tester.__init__(self, name, age, city, position)
        
    def showEmp(self):
        print(f"Employee Details:\nName: {self.name}\nAge: {self.age}\nRole: {self.role}\nEmp ID: {self.emp_id}") 
        if self.role.lower() == "programmer":
            self.showProgrammer()
        elif self.role.lower() == "tester":
            self.showTester()

# Example usage
e1 = Emp("abc", 20, "Pune", 234, "Tester", position="QA")
e1.showEmp()

e2 = Emp("xyz", 30, "Bombay", 567, "programmer", lang="Python")
e2.showEmp()
e2.showPerson()
