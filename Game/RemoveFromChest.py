import json

with open('../Game/UserData/Chest.json', 'r') as f:
    Chest = json.load(f)
with open('../Game/Tasks/Task.json', 'r') as f:
    Task = json.load(f)

Slot = Task['Object']

Chest[Slot][0] = ""
Chest[Slot][1] = 0

with open('../Game/UserData/Chest.json', 'w') as json_file:
    json.dump(Chest, json_file)
    



