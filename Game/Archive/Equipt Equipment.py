import json

with open('../Game/UserData/UserData.json', 'r') as f:
    UserData = json.load(f)
with open('../Game/ItemIDs/ItemID.json', 'r') as f:
    ItemID_Dict = json.load(f)
with open('../Game/ItemIDs/ReverseItemID.json', 'r') as f:
    ReverseItemID_Dict = json.load(f)
with open('../Game/UserData/Inv.json', 'r') as f:
    Inv = json.load(f)
with open ('../Game/Tasks/Task.json', 'r') as f:
    Task = json.load(f)

print(Task)

Task = "Equipt 1600"
ItemID = Task.split(' ')[1]

ItemIDFile = ItemID + ".json"

with open(ItemIDFile, 'r') as f:
    ItemIDData = json.load(f)

#if slot is full, replace and return original item to inv
if ItemIDData[ItemID][0] == "Helm":
    UserData['Equipment'][0] = ItemID
elif ItemIDData[ItemID][0] == "Chest Plate":
    UserData['Equipment'][1] = ItemID
elif ItemIDData[ItemID][0] == "Leggings":
    UserData['Equipment'][2] = ItemID
elif ItemIDData[ItemID][0] == "Boots":
    UserData['Equipment'][3] = ItemID
elif ItemIDData[ItemID][0] == "Necklace":
    UserData['Equipment'][4] = ItemID
elif ItemIDData[ItemID][0] == "Ring":
    if UserData['Equipment'][5] == "":
        UserData['Equipment'][5] = ItemID
    elif UserData['Equipment'][6] == "":
        UserData['Equipment'][6] = ItemID
    else:
        replacering = input("Which ring slot would you like to replace?")
        if repalcering == "1":
            UserData['Equipment'][5] = ItemID
        elif replacering == "2":
            UserData['Equipment'][6] = ItemID
elif ItemIDData[ItemID][0] == "Weapon":
    if ItemIDData[ItemID][1] == "1H":
        UserData['Equipment'][7] = ItemID
    else:
        UserData['Equipment'][7] = ItemID
        UserData['Equipment'][8] = ItemID
elif ItemIDData[ItemID][0] == "Shield":
    if ItemIDData[ItemID][1] == "1H":
        UserData['Equipment'][8] = ItemID
    else:
        UserData['Equipment'][7] = ItemID
        UserData['Equipment'][8] = ItemID

with open('UserData.json', 'w') as json_file:
    json.dump(UserData, json_file)
    



