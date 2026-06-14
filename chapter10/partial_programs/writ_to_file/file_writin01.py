# write to a file and tru print the contents
from pathlib import Path

contents = "I love programming. I love creating new games.I also love working with data.\n"
path = Path('programming.txt')
try:
    path.write_text(contents)
except FileNotFoundError:
    print(f"Sorry,the file {path} does not exist")
else:
    print(contents)
    print(f"Please continue executing the program....")
