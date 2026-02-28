class Coder:
    def __init__(self,name,lang,company):
        self.name=name
        self.lang=lang
        self.company=company
    def showCoder(self):
        print(f"{self.name} is a programmer and have mastered {self.lang} language and works in {self.company}")
        
class Teacher:
    def __init__(self,name,lang,sch):
        self.name=name
        self.lang=lang
        self.sch=sch
    def showTeacher(self):
        print(f"{self.name} is a teacher and have mastered {self.lang} language and teaches in {self.sch} school")
        
class Person(Coder, Teacher):
    def __init__(self,name,lang,school,age,compny):
        Coder.__init__(self,name,lang,compny)
        Teacher.__init__(self,name,lang,school)
        self.age=age
    def showPerson(self):
        print(f"{self.name} has age {self.age} and studies in {self.sch}")
        
p=Person("abc","python","kv cme",20,"amazon")
c=Person("xyz","english","kv bombay",21,"flipcart")
p.showPerson()
p.showCoder()
c.showTeacher()
# print(Person.mro())