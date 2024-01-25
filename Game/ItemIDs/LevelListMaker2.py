import json

with open('LevelList.json', 'r') as f:
    ItemParams = json.load(f)
 

leveltest = 5
x = 1
xstr = str(x)
newJSON =  "{"

while leveltest < 100:
    x = 1
    newJSON = newJSON + "'" + str(leveltest) + "': ["
    while x < 25:
        try:
            xstr = str(x)

            if ItemParams[xstr][1] == leveltest:
                newJSON =  newJSON + "'" + xstr + "', " + ItemParams[xstr][0] + "], "   
                    
            x = x + 1
        except:
            x = x + 1
    leveltest = leveltest + 5
            
with open('LevelList.json', 'w') as json_file:
    json.dump(newJSON, json_file)

with open('LevelList.json', 'r') as f:
    Test = json.load(f)

print(Test)

