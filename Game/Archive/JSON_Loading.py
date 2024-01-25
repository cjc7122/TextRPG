import json

with open('GameData.json', 'r') as f:
    data_dict = json.load(f)

data_dict['Username'] = "Joe"
Mining = data_dict['Mining'][0]
print(data_dict['Username'])
print(Mining)
