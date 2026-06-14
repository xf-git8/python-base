# read a file and if path not exist,use try except
# then continue executing the program
from pathlib import Path
path = Path('pi_digits.txt')
try:
    contents = path.read_text()
    lines = contents.splitlines()
    for line in lines:
        print(line)
except FileNotFoundError:
    print(f"Sorry,the file {path} does not exist")
else:
    print(f"Please continue executing the program....")

