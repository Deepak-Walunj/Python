class person:
#     name="Deepak"
#     age=20
#     occupation="Student"
#     def info(self):
#         print(f"{self.name} is {self.age} yrs old and currently is a {self.occupation}")

    def __init__(self,name,age,occupation):
        self.name=name
        self.age=age
        self.occupation=occupation
        
    def info(self):
        print(f"{self.name} is {self.age} yrs old and currently is a {self.occupation}")

        
a=person("Deepak",20,"Student")
print(a.name)
a.info()
b=person(20,"Deepak","xyz")
b.info()