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
    
ItemID = Task['Object']
ItemCount = Task['Amount']
ItemLocation = Task['Location']

MaxInv = 10
i = 1

while i <= MaxInv:
    Slot = "Slot " + str(i)
    if ItemLocation == "ground":
        if Inv[Slot][1] == 0:
            x = i + 1
            while x <= MaxInv:
                Slot2 = "Slot " + str(x)
                if Inv[Slot2][1] == 0:
                    x = x + 1
                elif ItemID == Inv[Slot2][0]:
                    Inv[Slot2][1] = Inv[Slot2][1] + int(ItemCount)
                    i = 11
                    break
                else:
                    x = x + 1
            if x == 11:
                Inv[Slot][0] = ItemID
                Inv[Slot][1] = int(ItemCount)
                break
        elif Inv[Slot][1] > 0:
            if Inv[Slot][0] == ItemID:
                Inv[Slot][1] = Inv[Slot][1] + int(ItemCount)
                break
            else:
                i = i + 1
                if i > MaxInv:
                    print("Inventory is full, please get rid on an item!")
    elif ItemLocation == "chest":
        ItemID = Chest[Task['Object']][0]
        ItemCount = Chest[Task['Object']][1]
        if Inv[Slot][1] == 0:
            x = i + 1
            while x <= MaxInv:
                Slot2 = "Slot " + str(x)
                if Inv[Slot2][1] == 0:
                    x = x + 1
                elif ItemID == Inv[Slot2][0]:
                    Inv[Slot2][1] = Inv[Slot2][1] + int(ItemCount)
                    i = 11
                    break
                else:
                    x = x + 1
            if x == 11:
                Inv[Slot][0] = ItemID
                Inv[Slot][1] = int(ItemCount)
                break
        elif Inv[Slot][1] > 0:
            if Inv[Slot][0] == ItemID:
                Inv[Slot][1] = Inv[Slot][1] + int(ItemCount)
                break
            else:
                i = i + 1
                if i > MaxInv:
                    print("Inventory is full, please get rid on an item!")
       

with open('../Game/UserData/Inv.json', 'w') as json_file:
    json.dump(Inv, json_file)
    



