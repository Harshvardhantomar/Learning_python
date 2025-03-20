from pathlib import Path

cpath = Path('cats.txt')
dpath = Path('dogs.txt')

try:
   contents=  cpath.read_text()
   print('Name of your cats are:')
   for content in contents.splitlines():
    print(f"\t{content}")
   print("\n")
except FileNotFoundError:
   print("There is no such file.")


try:
   contents=  dpath.read_text()
   print('Name of your dogs are:')
   for content in contents.splitlines():
    print(f"\t{content}")
   print("\n")
except FileNotFoundError:
   print("There is no such file.")