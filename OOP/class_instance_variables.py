class emp:
    emp_id=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.c_name="Apple main"
        emp.emp_id +=1
        
    def showEmp(self):
        print(f"{self.name} has age {self.age} working in {self.c_name} has ID {self.emp_id}")
        
e1=emp("abc",20)
e1.c_name="Apple India"
e1.showEmp()

e2=emp("xyz",21)
e2.showEmp()

e3=emp("pqr",30)
e3.emp_id=40
e3.c_name="Apple USA"
e3.showEmp()