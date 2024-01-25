import json

with open('../Game/UserData/UserData.json', 'r') as f:
    UserData = json.load(f)
with open('../Game/ItemIDs/ItemID.json', 'r') as f:
    ItemID_Dict = json.load(f)    
with open('../Game/UserData/Inv.json', 'r') as f:
    Inv = json.load(f)
with open('../Game/UserData/Chest.json', 'r') as f:
    Chest = json.load(f)
with open('../Game/Tasks/Task.json', 'r') as f:
    Task = json.load(f)


ItemID = Inv[Task['Object']][0]
ItemCount = Inv[Task['Object']][1]

MaxChest = 30
i = 1

while i <= MaxChest:
    Slot = "Slot " + str(i)
    if Chest[Slot][1] == 0:
        x = i + 1
        while x <= MaxChest:
            Slot2 = "Slot " + str(x)
            if Chest[Slot2][1] == 0:
                x = x + 1
            elif ItemID == Chest[Slot2][0]:
                Chest[Slot2][1] = Chest[Slot2][1] + int(ItemCount)
                i = 31
                break
            else:
                x = x + 1
        if x == 31:
            Chest[Slot][0] = ItemID
            Chest[Slot][1] = int(ItemCount)
            break
    elif Chest[Slot][1] > 0:
        if Chest[Slot][0] == ItemID:
            Chest[Slot][1] = Chest[Slot][1] + int(ItemCount)
            break
        else:
            i = i + 1
            if i > MaxChest:
                print("Chest is full, please get rid on an item!")
       

with open('../Game/UserData/Chest.json', 'w') as json_file:
    json.dump(Chest, json_file)
    



