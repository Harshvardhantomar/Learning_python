from pathlib import Path
import json

def check_fav_num(path):
    if path.exists():
        number = path.read_text()
        fav_number = json.loads(number)
        return fav_number
    else:
        return None
    
def store_fav_num(path):
    fav_num = int(input("What is your favorite number?"))
    num = json.dumps(fav_num)
    path.write_text(num)
    return num

def favorite_number():
    path = Path('favnum.json')
    
    fav_num = check_fav_num(path)
    if fav_num:
         print(f"I know your favorite number! It's {fav_num}")
    else:
        fav_num = store_fav_num(path)

favorite_number()
