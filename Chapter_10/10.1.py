from pathlib import Path
import json

fav_num = int(input("What is your favorite number?"))

path = Path('favnum.json')
num = json.dumps(fav_num)
path.write_text(num)

