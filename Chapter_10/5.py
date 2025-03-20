def addition ():
    print("Enter two numbers to add:")
    a = input("First number: ")
    b = input("Second number: ")

    try:
        a = int(a)
        b = int(b)
        return a+b
    except ValueError:
        return "Plz enter a numerical value"

print(addition())