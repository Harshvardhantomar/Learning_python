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

class Admin(User):
    def __init__(self,fname,lname,gender,age,country):
          super().__init__(fname,lname,gender,age,country)
          privileges= ['Can add user','Can ban user','Can add post','Can delete post']
          self.privileges = Privileges()
    
    

class Privileges:
     
    def __init__(self):
         self.privileges= ['Can add user','Can ban user','Can add post','Can delete post']

    def show_privileges(self):
         print("An admin has following privileges:")
         for privilege in self.privileges:
              print(f"\t{privilege}")

admin = Admin('Harsh','Tomar','male',24,'India')


admin.privileges.show_privileges()
     

        