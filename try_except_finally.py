def hey():
    try:
        n=int(input("Enter a number "))
        print(n)
        return 1
    except ValueError:
        print("Enter a number not a string ")
        return 0
    finally:
        print("I will get executed regardless the return statement")
    print("I am in the function but outside finally and try/except")
    
x=hey()
print(x)
