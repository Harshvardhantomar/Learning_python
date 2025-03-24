from pathlib import Path
import json

def check_user_info(path):
    if path.exists():
        contents = path.read_text()
        user_details = json.loads(contents)
        print('Your details are:')
        for key,value in user_details.items():
            print(f'\t{key.title()} : {value}')
        return False
    else:
        return True

def store_details(path):
    name = input("Enter your name")
    gender = input("Your gender?")
    age = input("Enter your age")
    
    user_details = {'name':name,'gender':gender,'age':age}
    contents = json.dumps(user_details)
    path.write_text(contents)
    print(f'Hey, {name.title()} your details are now stored.')

def user_details():
    user_name = input("Enter your name")
    userfile = user_name.lower()
    path = Path(f'{userfile}.json')
    
    status = check_user_info(path)
    
    if(status):
        store_details(path)
        
user_details()
   