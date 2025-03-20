def addition ():
    while(True):
        print("Enter two numbers to add:")
        a = input("First number: ")
        b = input("Second number: ")

        try:
            a = int(a)
            b = int(b)
            break
        except ValueError:
            print("Plz enter a numerical value")
        
    return a+b

print(addition())