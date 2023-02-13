import math
import os
import random
import uuid
from pathlib import Path
import json
import shutil

base = Path('data')

if os.path.exists(base):
    shutil.rmtree(base)
os.mkdir(base)

for i in range(math.floor(random.random() * 100) + 50):
    # customer level
    custID = random.randint(1, 1000)
    pathi = base / str(custID)
    if not os.path.exists(pathi):
        os.mkdir(pathi)
    for j in range(math.floor(random.random() * 500) + 2):
        # transaction level
        year = 2022
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        data = {
            'item': random.randint(1, 100),
            'price': random.randint(1, 1000),
            'quantity': random.randint(1, 100),
        }
        pathj = pathi / f'{year}-{month:02d}-{day:02d}'
        if not os.path.exists(pathj):
            os.mkdir(pathj)
        with open(pathj / f"{uuid.uuid4()}.json", 'w') as f:
            f.write(json.dumps(data))
