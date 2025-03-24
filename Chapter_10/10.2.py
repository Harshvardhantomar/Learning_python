from pathlib import Path
import json

path = Path('favnum.json')
number = path.read_text()
fav_number = json.loads(number)

print(f"I know your favorite number! It's {fav_number}")