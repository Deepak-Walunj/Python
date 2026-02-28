class Emp:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __len__(self):
        return len(self.name)
    
    def __str__(self):
        return f"The object has '{self.name}' and '{self.age}' attributes."
    
    def __repr__(self):
        return f"Emp(name='{self.name}', age={self.age})"
    
    def __call__(self):
        print("The object is called.")
    
e = Emp("abc", 20)
print(len(e))  # Output: 3
print(e)  # Output: The object has 'abc' and '20' attributes.
print(repr(e))  # Output: Emp(name='abc', age=20)
e()  # Output: The object is called.
