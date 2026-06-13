# read a file and if path not exist,use try except
from pathlib import Path

path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
    print(f"读取{path.name}成功")
    print(contents)
except FileNotFoundError:
    print(f"Sorry,the first {path} does not exist")
else:
    print("cc")
