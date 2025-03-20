from pathlib import Path
path = Path('guest_book.txt')

guest = ''
while (True):
    prompt = 'Enter the name of guest\n'
    prompt += "Enter 'quit' for ending"
    name = input(prompt)
    if(name == 'quit'):
        break
    guest += f'{name} \n'

path.write_text(guest)


