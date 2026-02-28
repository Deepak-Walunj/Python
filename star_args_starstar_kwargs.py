# def thing(*name):
#     return [letter for word in name for letter in word]

        
# s=thing('abc','pqr','xyz')
# print(s)

def person(**identity):
    print(identity)
    for key in identity:
        print(key)
    for key in identity:
        for letter in key:
            print(letter)
    for value in identity.values():
        print(value)
    
person(name='xyz',age=21,address='abc')