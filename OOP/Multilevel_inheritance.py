class Person:
    def __init__(self,name,age,addr):
        self.name=name
        self.age=age
        self.addr=addr
    def showPerson(self):
        print(f"person details:\nName:{self.name}\nAge:{self.age}\nAddress:{self.addr}")
        
class Emp(Person):
    def __init__(self,name,age,cmpny):
        Person.__init__(self,name,age,addr="Pune")
        self.cmpny=cmpny
    def showEmp(self):
        print(f"Employee details:\nName:{self.name}\nAge:{self.age}\nAddress:{self.addr}\nCompany:{self.cmpny}")
        
class Programmer(Emp):
    def __init__(self,name,age,lang):
        Emp.__init__(self,name,age,cmpny="Apple")
        self.lang=lang
    def showProgrammer(self):
        print(f"Programmer details:\nName:{self.name}\nAge:{self.age}\nAddress:{self.addr}\nCompany:{self.cmpny}\nlanguage:{self.lang}")
        
p=Programmer("abc",20,"Java")
p.showEmp()
p.showPerson()
p.showProgrammer()

per=Person("zxc",30,"Mumbai")
per.showPerson()
