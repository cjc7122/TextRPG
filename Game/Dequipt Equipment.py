import json

with open('UserData.json', 'r') as f:
    UserData = json.load(f)

Task = "Dequipt 1000"
ItemID = Task.split(' ')[1]

ItemIDFile = ItemID + ".json"

with open(ItemIDFile, 'r') as f:
    ItemIDData = json.load(f)

#if slot is full, replace and return original item to inv
if ItemIDData[ItemID][0] == "Helm":
    UserData['Equipment'][0] = ""
elif ItemIDData[ItemID][0] == "Chest Plate":
    UserData['Equipment'][1] = ""
elif ItemIDData[ItemID][0] == "Leggings":
    UserData['Equipment'][2] = ""
elif ItemIDData[ItemID][0] == "Boots":
    UserData['Equipment'][3] = ""
elif ItemIDData[ItemID][0] == "Necklace":
    UserData['Equipment'][4] = ""
elif ItemIDData[ItemID][0] == "Ring":
    if UserData['Equipment'][5] == "":
        UserData['Equipment'][5] = ""
    elif UserData['Equipment'][6] == "":
        UserData['Equipment'][6] = ""
    else:
        replacering = input("Which ring slot would you like to replace?")
        if repalcering == "1":
            UserData['Equipment'][5] = ""
        elif replacering == "2":
            UserData['Equipment'][6] = ""
elif ItemIDData[ItemID][0] == "Weapon":
    if ItemIDData[ItemID][1] == "1H":
        UserData['Equipment'][7] = ""
    else:
        UserData['Equipment'][7] = ""
        UserData['Equipment'][8] = ""
elif ItemIDData[ItemID][0] == "Shield":
    if ItemIDData[ItemID][1] == "1H":
        UserData['Equipment'][8] = ""
    else:
        UserData['Equipment'][7] = ""
        UserData['Equipment'][8] = ""

with open('UserData.json', 'w') as json_file:
    json.dump(UserData, json_file)
    



