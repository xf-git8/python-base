# 加载输出user_info.json文件中的内容
import json
from pathlib import Path

path = Path('user_info.json')
try:
    contexts = path.read_text()
    user_info = json.loads(contexts)
    print(f"Welcome back, {user_info}")
except FileNotFoundError:
    print(f"Sorry,the file {path} does not exist")