#
from pathlib import Path
import json
path = Path('number.json')
try:
    contexts = path.read_text()
    numbers = json.loads(contexts)
    print(numbers)

except FileNotFoundError:
    print(f"The file {path} does not exist")
