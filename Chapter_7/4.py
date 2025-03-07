prompt = "Enter your toppings:"
prompt += "\nEnter 'quit' when you are finished."

flag = True
while flag:
    message = input(prompt)
    if(message=='quit'):
        flag=False
    else:
        print(f"Adding {message.title()} to your Pizza.")