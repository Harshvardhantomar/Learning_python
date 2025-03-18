from pathlib import Path
path = Path('Chapter_10/learning_python.txt')
content = path.read_text()

contents = content.splitlines()
file = []
for line in contents:
    print(line.strip())

for line in contents:
    file.append((line.strip()).removesuffix('.'))
print(file)