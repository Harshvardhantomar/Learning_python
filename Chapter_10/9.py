from pathlib import Path
path = Path('words_count.txt')

try:
    contents = path.read_text(encoding='utf-8')
    count = 0
    for content in contents.splitlines():
        count += content.count('Simon:')
    print(count)
except FileNotFoundError:
    print('womp womp')