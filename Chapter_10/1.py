from pathlib import Path
path = Path('Chapter_10/learning_python.txt')
content = path.read_text()

file = []
for line in content.splitlines():
    print(line.strip())

for line in content.splitlines():
    file.append((line.strip()).removesuffix('.'))
print(file)