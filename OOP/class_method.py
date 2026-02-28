class emp:
    c_name="apple"
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def show(self):
        print(f"{self.name}, {self.age}")
        
    @classmethod
    def changeC_name(cls,new_c_name):
        emp.c_name=new_c_name
        
    @classmethod
    def tostr(cls, string): 
        name,age=string.split("-")
        return cls(name, int(age))
e1=emp("abc",25)
print(emp.c_name)
# e1.changeC_name("tesla")
emp.changeC_name("tesla")
print(emp.c_name)
#class method as alternate constructor
s="XYZ-20"
e2=emp.tostr(s)
e1.show()
e2.show()
print(type(e1.age))