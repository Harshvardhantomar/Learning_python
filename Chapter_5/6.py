user_age = int(input("Enter your age:"))

if(user_age<2):
    print("Hey Baby")
elif(user_age>2 and user_age<4):
    print("Hey Toddler")
elif(user_age>=4 and user_age<13):
    print("Hey Kid")
elif(user_age>=13 and user_age<20):
    print("Hey Teenager")
elif(20<=user_age<65):
    print("Hey Adult")
elif(user_age>=65):
    print("Hey Elder")
