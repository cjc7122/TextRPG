import json

with open('../Game/UserData/UserData.json', 'r') as f:
    UserData = json.load(f)
with open('../Game/ItemIDs/ItemID.json', 'r') as f:
    ItemID_Dict = json.load(f)

if UserData['Equipment'][0] != "":
    print("Helmet: " + ItemID_Dict[UserData['Equipment'][0]])
else:
    print("Helmet: None")
          
if UserData['Equipment'][1] != "":    
    print("Chestplate: " + ItemID_Dict[UserData['Equipment'][1]])
else:
    print("Chestplate: None")
          
if UserData['Equipment'][2] != "":
    print("Leggings: " + ItemID_Dict[UserData['Equipment'][2]])
else:
    print("Leggings: None")
          
if UserData['Equipment'][3] != "":
    print("Boots: " + ItemID_Dict[UserData['Equipment'][3]])
else:
    print("Boots: None")
    
if UserData['Equipment'][4] != "":
    print("Necklace: " + ItemID_Dict[UserData['Equipment'][4]])
else:
    print("Necklace: None")
    
if UserData['Equipment'][5] != "":
    print("Ring 1: " + ItemID_Dict[UserData['Equipment'][5]])
else:
    print("Ring 1: None")
    
if UserData['Equipment'][6] != "":
    print("Ring 2: " + ItemID_Dict[UserData['Equipment'][6]])
else:
    print("Ring 2: None")
    
if UserData['Equipment'][7] != "":
    print("Hand 1: " + ItemID_Dict[UserData['Equipment'][7]])
else:
    print("Hand 1: None")
    
if UserData['Equipment'][8] != "":
    print("Hand 2: " + ItemID_Dict[UserData['Equipment'][8]])
else:
    print("Hand 2: None")



