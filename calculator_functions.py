# # 


# def add(num1, num2):
#     return num1 + num2

# def sub(num1, num2):
#     return num1 - num2

# def mul(num1, num2):
#     return num1 * num2

# def div(num1, num2):
#     try:
#         return num1 / num2
#     except ZeroDivisionError:
#         return "Error: Division by zero is not allowed."

# # Dictionary mapping operation numbers to functions and their descriptions
# operations = {
#     1: ('Addition', add),
#     2: ('Subtraction', sub),
#     3: ('Multiplication', mul),
#     4: ('Division', div),
#     5: ('Exit', None)
# }

# name = input("Enter your name: ")
# print(f"Welcome {name}")
# print("You want to perform which operation:")
# for num, (desc, _) in operations.items():
#     print(f"{num}) {desc}")

# while True:
#     try:
#         ch = int(input("Enter operation number: "))
#         if ch == 5:
#             print("Exiting the program. Goodbye!")
#             break
#         if ch not in operations:
#             print("Invalid operation number. Please try again.")
#             continue

#         a = int(input("Enter 1st number: "))
#         b = int(input("Enter 2nd number: "))
#         desc, func = operations[ch]

#         result = func(a, b)
#         print(f"{desc} result is: {result}")
#     except ValueError:
#         print("Invalid input. Please enter numeric values.")


def calc(num1, num2, op):
    return{
            "+":num1+num2,
            "-":num1-num2,
            "*":num1*num2,
            "/":num1/num2 if num2 != 0 else "Error: Division by zero"
    }[op]
    
ops={
    1:"+",
    2:"-",
    3:"*",
    4:"/"
}

name=input("Enter yo name ")
print(f"Hello {name}\nThe operations performed on this calc are\n1)Addition\n2)Subtraction\n3)Multiplication\n4)Division\n5)Exit")
while True:
    ch=int(input("Enter the operation number "))
    if(ch==5):
        print(f"Goodbye {name}")
        break
    if ch not in ops:
        print(f"Invalid operation {name}, try again!")
        continue
    try:
        a,b=int(input("Enter 1st number ")), int(input("Enter 2nd number "))
        print(f"Result is: {calc(a,b,ops[ch])}")
    except ValueError:
        print("Invalid input {name}")