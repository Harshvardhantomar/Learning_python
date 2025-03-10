class User:
    def __init__(self,fname,lname,gender,age,country):
        self.first_name = fname
        self.last_name = lname
        self.gender = gender
        self.age = age
        self.country = country

    def describe_user(self):
            print("Hey, These are your details:")
            print(f"\tFirst Name:{self.first_name}")
            print(f"\tLast Name:{self.last_name}")
            print(f"\tAge:{self.age}")
            print(f"\tGender:{self.gender}")
            print(f"\tCountry:{self.country}")

    def greet_user(self):
         print(f"Hey! {self.first_name.title()} {self.last_name.title()}, Nice to meet you.")


user1=User('Harshvardhan','Tomar','Male',24,'India')
user2=User('ashmit','dubey','male',25,'India')
user3=User('simon','miniter','male',32,'England')

user1.describe_user()
user3.describe_user()
user2.describe_user()
           
user2.greet_user()
user1.greet_user()
user3.greet_user()