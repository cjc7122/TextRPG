import json

Buddy2Task = ""
Buddy2Object = ""

with open('Buddy2Data.json', 'r') as f:
    Buddy2 = json.load(f)
with open('UserData.json', 'r') as f:
    UserData = json.load(f)

    if Buddy2['Task'] == "Mine" or Buddy2['Task'] == "mine":
        Buddy2['Task'] = "Mining"
    elif Buddy2['Task'] == "Chop" or Buddy2['Task'] == "chop":
        Buddy2['Task'] = "Chopping"
        
    if Buddy2['Task'] == "Mining":
        if Buddy2['Object'] == "Stone" or Buddy2['Object'] == "stone":
            Buddy2['ObjectValue'] = 0
            Buddy2['exp'] = 1
        elif Buddy2['Object'] == "Coal" or Buddy2['Object'] == "coal":
            if UserData['Mining'][0] >= 5:
                Buddy2['ObjectValue'] = 1
                Buddy2['exp'] = 5
        elif Buddy2['Object'] == "Tin" or Buddy2['Object'] == "tin":
            if UserData['Mining'][0] >= 10:
                Buddy2['ObjectValue'] = 2
                Buddy2['exp'] = 10
        elif Buddy2['Object'] == "Copper" or Buddy2['Object'] == "copper":
            if UserData['Mining'][0] >= 15:
                Buddy2['ObjectValue'] = 3
                Buddy2['exp'] = 25
            else:
                print("Buddy can only mine what you can! Mining stone instead :)")
                Buddy2['ObjectValue'] = 0
                Buddy2['exp'] = 1
    elif Buddy2['Task'] == "Chopping":
        if Buddy2['Object'] == "Oak" or Buddy2['Object'] == "oak":
            Buddy2['ObjectValue'] = 0
            Buddy2['exp'] = 1
        elif Buddy2['Object'] == "Birch" or Buddy2['Object'] == "Birch":
            if UserData['Chopping'][0] >= 5:
                Buddy2['ObjectValue'] = 1
                Buddy2['exp'] = 5

with open('Buddy2Data.json', 'w') as json_file:
    json.dump(Buddy2, json_file)
    

