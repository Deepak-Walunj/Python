person1={
    "Name":"Sahil",
    "Age":20,
    "Studying in":"VIIT"
}
print(person1)
print(person1["Age"])
person1['Pursuing']="Btech CSE"
print(person1)
del person1['Age']
print(person1)

foods=("pizza","Burger","Hotdog")
for food in foods:
    print(food)
    
set={1,2,"I3"}
print(set)
set.add(4.4)
print(set)
set.remove(1)
print(set)