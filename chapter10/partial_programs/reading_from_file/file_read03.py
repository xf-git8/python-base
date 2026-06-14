# read a file and if path not exist,use try except
# count the number of lines then continue executing the program
from pathlib import Path
path = Path('pi_million_digits.txt')
try:
    contents = path.read_text()
    pi_string = ''
    str = 'cc'
    for line in contents.splitlines():
        pi_string += line.strip()
    str += pi_string[:44]
    print(pi_string[:52] + "...")
    print(f"{len(str)} number in {str}")
except FileNotFoundError:
    print(f'Sorry,the file {path} does not exist')
else:
    print(f'Please continue executing the program....')
