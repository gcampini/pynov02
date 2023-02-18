import datetime
import glob
import os
import shutil
from pathlib import Path

base = Path('data')

# 1
print(f"No. of clients: {len(os.listdir(base))}")

# 2
clients = os.listdir(base)
c = {}
less_than_50 = []
gold_clients = []
for client in clients:
    path = base / Path(str(client))
    dates = os.listdir(path)
    count = 0
    for date in dates:
        path = base / Path(str(client)) / Path(str(date))
        files = os.listdir(path)
        count += len(files)
    if count < 50:
        less_than_50.append(client)
    if count > 500:
        gold_clients.append(client)
    c[client] = count
print(c)

# 3
dataset_size = 0
for item in glob.glob("data/**/*.json"):
    dataset_size += os.path.getsize(item)
dataset_size = round(dataset_size / 1024, 2)
print(f'The dataset weights {dataset_size} Ko.')

# 4
print(f"Removing {len(less_than_50)} clients...")
for client in less_than_50:
    path = base / Path(str(client))
    shutil.rmtree(path)

# 5
print(f"Copying {len(gold_clients)} clients to gold folder...")
gold_clients_path = Path('gold')
if os.path.exists(gold_clients_path):
    shutil.rmtree(gold_clients_path)
for client in gold_clients:
    path = base / Path(str(client))
    shutil.copytree(path, gold_clients_path / Path(str(client)))

# 6
total = glob.glob("data/**/*/*.json")
print(f"Total number of transactions: {len(total)}")

# 7
december = glob.glob("data/**/2022-12-[0-9][0-9]/*.json")
print(
    f"Total number of transactions in December: {len(december)}. Percentage: {round(len(december) / len(total) * 100, 2)}%")

# 8
# Trouver le nombre total de transactions effectuées le week-end.
# Donner un pourcentage par rapport au nombre de total de transactions.
count = 0
for path in glob.glob("data/*/*"):
    date = path.split('/')[-1]
    year, month, day = date.split('-')
    if datetime.date(int(year), int(month), int(day)).weekday() in [5, 6]:
        count += len(glob.glob(path + "/*.json"))
print(
    f"Total number of transactions on weekends: {count}. Percentage: {round(count / len(total) * 100, 2)}%"
)

# 10
# rearange structure to : date -> client -> transaction
# in NEW folder called "rearranged"
# without opening file, using only os, shutil and glob
rearranged = Path('rearranged')
if os.path.exists(rearranged):
    shutil.rmtree(rearranged)
os.mkdir(rearranged)

clients = os.listdir(base)  # because we removed some clients
for client in clients:
    path = base / Path(str(client))
    dates = os.listdir(path)
    for date in dates:
        path = base / Path(str(client)) / Path(str(date))
        files = os.listdir(path)
        for file in files:
            path = base / Path(str(client)) / Path(str(date)) / Path(str(file))
            dest = rearranged / Path(str(date)) / Path(str(client))
            if not os.path.exists(dest):
                os.makedirs(dest, exist_ok=True)
            shutil.copy(path, dest)
