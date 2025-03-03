current_user = ["akshay","john","toby","harry","simon","obama","donald"]    

new_user = ["John","Akshat","Josh","aman","Simon","Toby","Karan"]

for user in new_user:
    if(user.lower() in current_user):
        print("This username is not available. Try other username.\n")
    else:
        print("This username is available.\n")