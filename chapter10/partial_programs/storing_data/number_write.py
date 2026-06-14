#
from pathlib import Path
import  json
user={
    'name':'liuhuan',
    'age':18,
    'numbers':[2,3,5,7,11,13]
}
try:
    with open('user.json','w') as f:
        json.dump(user,f,ensure_ascii=False,indent=4)
    print(f"save user.json success")
except Exception as e:
    print(f"save user.json error:{e}")