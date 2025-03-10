class User:
    def __init__(self,fname,lname,gender,age,country):
        self.first_name = fname
        self.last_name = lname
        self.gender = gender
        self.age = age
        self.country = country
        self.login_attempt = 0

    def describe_user(self):
            print("Hey, These are your details:")
            print(f"\tFirst Name:{self.first_name}")
            print(f"\tLast Name:{self.last_name}")
            print(f"\tAge:{self.age}")
            print(f"\tGender:{self.gender}")
            print(f"\tCountry:{self.country}")

    def greet_user(self):
         print(f"Hey! {self.first_name.title()} {self.last_name.title()}, Nice to meet you.")
    def number_of_login_attempts(self):
         print(f"You have tried to login {self.login_attempt} times.")
    def increment_login_attempts(self):
         self.login_attempt+=1
    def reset_login_attempts(self):
         self.login_attempt=0

user1=User('Harshvardhan','Tomar','Male',24,'India')
user2=User('ashmit','dubey','male',25,'India')
user3=User('simon','miniter','male',32,'England')


user1.number_of_login_attempts()
user2.number_of_login_attempts()
user3.number_of_login_attempts()

user1.increment_login_attempts()
user2.increment_login_attempts()

user1.number_of_login_attempts()
user2.number_of_login_attempts()
user3.number_of_login_attempts()

user1.reset_login_attempts()
user2.increment_login_attempts()

user1.number_of_login_attempts()
user2.number_of_login_attempts()
user3.number_of_login_attempts()