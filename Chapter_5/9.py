username = []

if not username:
    print("We need to find some users!")
else:
    for user in username:
        if(user.lower()=='admin'):
            print(f"Hello {user}, would you like a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging again.")