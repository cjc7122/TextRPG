import json
 
x = 0
xstr = str(x)
newJSON =  "{"


while x < 50:
    try:
        xstr = str(x)

        file = xstr + '.json'
            
        with open(file, 'r') as f:
            ItemParams = json.load(f)

        newJSON =  newJSON + "'" + xstr + "':" + "['" + ItemParams[xstr][0] + "', " + str(ItemParams[xstr][2]) + "], "   
                
        x = x + 1
    except:
        x = x + 1
            
            
with open('LevelList.json', 'w') as json_file:
    json.dump(newJSON, json_file)

with open('LevelList.json', 'r') as f:
    Test = json.load(f)

print(Test['0'])
