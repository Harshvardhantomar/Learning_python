from pathlib import Path
path = Path('Chapter_10/learning_python.txt')
content = path.read_text()

file = []
for line in content.splitlines():
    a = line.strip()
    print(a.replace('python','C++'))
