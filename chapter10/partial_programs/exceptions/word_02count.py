# define function and count txt words with list
from  pathlib import  Path

def count_words(path):
    """
    count txt words
    :param path:
    :return: str total words
    """
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the {path} does not exist")
    else:
        words = len(contents.split())
        print(f"The {path} has about {words} words")
filenames = ['alice.txt','little_women.txt','moby_dick.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)