class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def showDetails(self):
        print(f"{self.name} has age: {self.age}")
        
class programmer(person):
    def __init__(self,name,age, lan):
        super().__init__(name,age)
        self.lan=lan
        
    def showPerson(self):
        super().showDetails()
        print(f"{self.name} aged {self.age} speaks language {self.lan}")
        
    
        
a=person("Deepak",20)
a.showDetails()
b=programmer("abc",21,"marathi")
b.showPerson()
b.showDetails()