import json

with open('RevisedItemID.json', 'r') as f:
    ItemID_Dict = json.load(f)

i = 0

ReverseItemID_Dict = "{'Stone': '1', "
while i <= 1800:
    try:
        Object = ItemID_Dict[str(i)]
        ItemID = str(i)

        ReverseItemID_Dict = ReverseItemID_Dict + "'" + Object + "': '" + ItemID + "', "
        
        i = i + 1
    except:
        i = i + 1


print(ReverseItemID_Dict)

with open('ReverseItemID.json', 'w') as json_file:
    json.dump(ReverseItemID_Dict, json_file)
    

