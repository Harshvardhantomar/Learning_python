prompt = "What is your age:"
prompt += "\nEnter '0' if no viewers left."

flag = True
while flag:
    viewer_age = int(input(prompt))
    if(viewer_age==0):
        print("Thanks! for coming. Bye!")
        break
    elif (viewer_age<3):
        print("Your ticket is free.")
    elif(viewer_age<=12):
        print("Your ticket is $10 dollars")
    else:
        print('Your ticket is $15 dollars.')