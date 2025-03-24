from pathlib import Path
import json


path = Path('Numbers.json')
content = path.read_text()
number = json.loads(content)

print(content,number)

