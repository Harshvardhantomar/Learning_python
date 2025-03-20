from pathlib import Path
path = Path('guest.txt')

name = input("Hey what's your name?")
print('You are invited.')

path.write_text(name)
