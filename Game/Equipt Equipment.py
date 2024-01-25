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

Task1 = Task['Task']
ItemID = Inv[Task['Object']][0]

MaxInv = 10
i = 1

while i <= MaxInv:
    if Inv['Slot ' + str(i)][0] == ItemID:
        #Add Object to Equipt Items
        ItemIDFile = ItemID + ".json"
        with open('../Game/ItemIDs/' + ItemIDFile, 'r') as f:
            ItemIDData = json.load(f)
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
        else:
            print("This item is not equiptable.")
        break
    else:
        i = i + 1

if i == 11:
    print("You do not have this item in your inventory!")



#if slot is full, replace and return original item to inv


with open('../Game/UserData/UserData.json', 'w') as json_file:
    json.dump(UserData, json_file)
    



