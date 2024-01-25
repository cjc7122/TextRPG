import json

Username = "Colin"
MiningLevel = 7
MiningExp = 0
MiningExp_LevelUp = 100

Data = {'Username': Username,
        'Mining': [MiningLevel, MiningExp, MiningExp_LevelUp]}

with open('Data.json', 'w') as json_file:
    json.dump(Data, json_file)

