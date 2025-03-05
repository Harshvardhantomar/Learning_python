glossary = {
    'break':'This is a reserved keyword in python and it is used to skip or jump out of the loop, when our condition is met.\n',
    'input':'This is a reserved keyword in python and it is used to make user-friendly programs, it allows user to input a value for the program\n',
    'continue':'This is a reserved keyword in python and it is used to jump to the top of the loop and start the loop with next iteration and skipping the current iteration.'
    }

for key,value in glossary.items():
    print(f"{key.title()}:{value}")