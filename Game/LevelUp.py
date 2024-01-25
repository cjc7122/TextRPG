import json, time

with open('../Game/ItemIDs/ItemID.json', 'r') as f:
    ItemID_Dict = json.load(f)
with open('../Game/ItemIDs/RevisedItemID.json', 'r') as f:
    RevisedItemID_Dict = json.load(f)
with open('../Game/UserData/UserData.json', 'r') as f:
    UserData = json.load(f)
with open('../Game/UserData/Inv.json', 'r') as f:
    Inv = json.load(f)
with open('../Game/Tasks/Task.json', 'r') as f:
    Task = json.load(f)
with open('../Game/ItemIDs/MiningLevelList.json', 'r') as f:
    LevelUp = json.load(f)


if(UserData['Main'][1] >= UserData['Main'][2]):
    UserData['Main'][1] = UserData['Main'][1] - UserData['Main'][2]
    UserData['Main'][0] = UserData['Main'][0] + 1
    UserData['Main'][2] = pow(1.25, UserData['Main'][0]) #fucked
    UserData['StatPoints'][0] = UserData['StatPoints'][0] + 3

	
if(UserData['Mining'][1] >= UserData['Mining'][2]):
    UserData['Mining'][1] = UserData['Mining'][1] - UserData['Mining'][2]
    UserData['Mining'][0] = UserData['Mining'][0] + 1
    UserData['Mining'][2] = pow(1.25, UserData['Mining'][0])
    UserData['StatPoints'][0] = UserData['StatPoints'][0] + 1
    print("Mining leveled up to level: ", UserData['Mining'][0])
    try:
        if LevelUp[str(UserData['Mining'][0])][0] !=  "":
            print("You can now mine " + LevelUp[str(UserData['Mining'][0])][1])
            try:
                print("You can now mine " + LevelUp[str(UserData['Mining'][0])][3])
            except:
                x = 1
    except:
        x = 1	
if(UserData['Chopping'][1] >= UserData['Chopping'][2]):
    UserData['Chopping'][1] = UserData['Chopping'][1] - UserData['Chopping'][2]
    UserData['Chopping'][0] = UserData['Chopping'][0] + 1
    UserData['Chopping'][2] = pow(1.25, UserData['Chopping'][0])
    UserData['StatPoints'][0] = UserData['StatPoints'][0] + 1
    print("Chopping leveled up to level: ", UserData['Chopping'][0])
    if UserData['Chopping'][0] == 5:
    	print("You can now chop birch trees!")
        
        
    


