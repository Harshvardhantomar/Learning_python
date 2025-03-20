from pathlib import Path

cpath = Path('cat.txt')
dpath = Path('dogs.txt')

try:
   contents=  cpath.read_text()
   print('Name of your cats are:')
   for content in contents.splitlines():
    print(f"\t{content}")
   print("\n")
except FileNotFoundError:
   pass


try:
   contents=  dpath.read_text()
   print('Name of your dogs are:')
   for content in contents.splitlines():
    print(f"\t{content}")
   print("\n")
except FileNotFoundError:
   pass