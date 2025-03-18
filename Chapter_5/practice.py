from pathlib import Path
path = Path('Chapter_5/pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()

pi_count = ''
for line in lines:
    pi_count += line.lstrip()
print(pi_count)
print(len(pi_count))