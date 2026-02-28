class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def show(self):
        print(f"{self.name} has age {self.age}")
        
    @property
    def something(self):
        return f"if we multiplied {self.name} age with 10 we get {10*self.age}"
    
    @something.setter
    def something(self,value):
        new_name,new_age=value
        self.name=new_name
        self.age=new_age/10
    
o=person("Deepak",20)
o.show()
print(o.something)
o.something=("name",23)
print(o.something)
o.show()