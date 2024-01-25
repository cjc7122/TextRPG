import json

Buddy1Task = ""
Buddy1Object = ""

with open('Buddy1Data.json', 'r') as f:
    Buddy1 = json.load(f)
with open('UserData.json', 'r') as f:
    UserData = json.load(f)

    if Buddy1['Task'] == "Mine" or Buddy1['Task'] == "mine":
        Buddy1['Task'] = "Mining"
    elif Buddy1['Task'] == "Chop" or Buddy1['Task'] == "chop":
        Buddy1['Task'] = "Chopping"
        
    if Buddy1['Task'] == "Mining":
        if Buddy1['Object'] == "Stone" or Buddy1['Object'] == "stone":
            Buddy1['ObjectValue'] = 0
            Buddy1['exp'] = 1
        elif Buddy1['Object'] == "Coal" or Buddy1['Object'] == "coal":
            if UserData['Mining'][0] >= 5:
                Buddy1['ObjectValue'] = 1
                Buddy1['exp'] = 5
        elif Buddy1['Object'] == "Tin" or Buddy1['Object'] == "tin":
            if UserData['Mining'][0] >= 10:
                Buddy1['ObjectValue'] = 2
                Buddy1['exp'] = 10
        elif Buddy1['Object'] == "Copper" or Buddy1['Object'] == "copper":
            if UserData['Mining'][0] >= 15:
                Buddy1['ObjectValue'] = 3
                Buddy1['exp'] = 25
            else:
                print("Buddy can only mine what you can! Mining stone instead :)")
                Buddy1['ObjectValue'] = 0
                Buddy1['exp'] = 1
    elif Buddy1['Task'] == "Chopping":
        if Buddy1['Object'] == "Oak" or Buddy1['Object'] == "oak":
            Buddy1['ObjectValue'] = 0
            Buddy1['exp'] = 1
        elif Buddy1['Object'] == "Birch" or Buddy1['Object'] == "Birch":
            if UserData['Chopping'][0] >= 5:
                Buddy1['ObjectValue'] = 1
                Buddy1['exp'] = 5

with open('Buddy1Data.json', 'w') as json_file:
    json.dump(Buddy1, json_file)
    

