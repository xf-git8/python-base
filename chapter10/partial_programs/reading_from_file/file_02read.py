# read a file and if path not exist,use try except
# then continue executing the program with if-else
from pathlib import Path
path = Path('pi_million_digits.txt')
try:
    contents = path.read_text()
    lines = contents.splitlines()
    pi_string = ''
    for line in lines:
        pi_string += line.strip()
    print(pi_string[:52] + "...")
except FileNotFoundError:
    print(f"Sorry,the file {path} does not exist")
else:
    birthday = input("Enter your birthday, in the form mmddyy: ")
    if birthday in pi_string:
        print("Your birthday appears in the first million digits of pi!")
    else:
        print("Your birthday does not appear in the first million digits of pi.")
