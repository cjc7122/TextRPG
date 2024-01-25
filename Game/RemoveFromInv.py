import json

with open('../Game/UserData/Inv.json', 'r') as f:
    Inv = json.load(f)
with open('../Game/Tasks/Task.json', 'r') as f:
    Task = json.load(f)

Slot = Task['Object']

Inv[Slot][0] = ""
Inv[Slot][1] = 0

with open('../Game/UserData/Inv.json', 'w') as json_file:
    json.dump(Inv, json_file)
    



