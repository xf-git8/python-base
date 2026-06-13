# define function and use count words
from pathlib import Path

def count_words(path):
    """
    count txt words
    :param path:
    :return: str
    """
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print("Sorry, the file {path} does not exist")
    else:
        words =  len(contents.split())
        print(f"The file {path} has {words} words")
path = Path('alice.txt')
count_words(path)
