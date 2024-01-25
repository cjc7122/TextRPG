import json, time

with open('../Game/UserData/UserData.json', 'r') as f:
    UserData = json.load(f)
with open('../Game/UserData/Inv.json', 'r') as f:
    Inv = json.load(f)
with open('../Game/Tasks/Task.json', 'r') as f:
    Task = json.load(f)
with open('../Game/ItemIDs/ReverseItemID.json', 'r') as f:
    ReverseItemID = json.load(f)

#def BuddySystem(BuddyNumber):
##    with open('../Game/Buddies/Buddy1Data.json', 'r') as f:
#        Buddy1 = json.load(f)
#    with open('../Game/Buddies/Buddy2Data.json', 'r') as f:
#        Buddy2 = json.load(f)
#    with open('../Game/Buddies/Buddy3Data.json', 'r') as f:
#        Buddy3 = json.load(f)
#        
#    if BuddyNumber == 0:
#        if UserData['Main'][0] >= 10:
#            if Buddy1['Task'] != "" and Buddy1['Object'] != "":
#                UserData[Buddy1['Task']][1] = UserData[Buddy1['Task']][1] + Buddy1['exp']
#                UserData['Main'][1] = UserData['Main'][1] + Buddy1['exp']
#                Inv['Mining'][Buddy1['ObjectValue']] = Inv['Mining'][Buddy1['ObjectValue']] + 1
#                print("Buddy 1 is also " + Buddy1['Task'] + " " + Buddy1['Object'] + ".")
#        if UserData['Main'][0] >= 20:
#            if Buddy2['Task'] != "" and Buddy2['Object'] != "":
#                UserData[Buddy2['Task']][1] = UserData[Buddy2['Task']][1] + Buddy2['exp']
#                UserData['Main'][1] = UserData['Main'][1] + Buddy2['exp']
#                Inv['Mining'][Buddy2['ObjectValue']] = Inv['Mining'][Buddy2['ObjectValue']] + 1
#                print("Buddy 2 is also " + Buddy2['Task'] + " " + Buddy2['Object'] + ".")
#        if UserData['Main'][0] >= 30:
#            if Buddy3['Task'] != "" and Buddy3['Object'] != "":
#                UserData[Buddy3['Task']][1] = UserData[Buddy3['Task']][1] + Buddy3['exp']
#                UserData['Main'][1] = UserData['Main'][1] + Buddy3['exp']
#                Inv['Mining'][Buddy3['ObjectValue']] = Inv['Mining'][Buddy3['ObjectValue']] + 1
#                print("Buddy 3 is also " + Buddy3['Task'] + " " + Buddy3['Object'] + ".")

#User Data: [0] = Level, [1] = Exp, [2] = LevelUp,
            
#Mining Items: [0] = Stone(1), [1] = Coal(5), [2] = Tin (10), [3] = Copper (15), [4] = Iron(25) 
#[5] Gold(35), [6] = Titanium(45), [7] Diamond(55), [8] = Tungsten (75), [9] = Meteorite (85)

ItemFile = ReverseItemID[Task['Object']] + ".json"

with open('../Game/ItemIDs/' + ItemFile, 'r') as f:
    ItemFile = json.load(f)

wait = range(5)
if Task['Task'] == "Mine":
    if ItemFile[ReverseItemID[Task['Object']]][1] == "Mine":
        if ItemFile[ReverseItemID[Task['Object']]][2] <= UserData['Mining'][0]:
            Task['Object'] = ReverseItemID[Task['Object']]
            for n in wait:
                print("...")
                time.sleep(ItemFile[str(Task['Object'])][3]/(2*UserData['Mining'][0]))
            UserData['Mining'][1] = UserData['Mining'][1] + (ItemFile[str(Task['Object'])][3]/5)
            UserData['Main'][1] = UserData['Main'][1] + (ItemFile[str(Task['Object'])][3]/5)
            Task['Amount'] = 1
            Task['Location'] = "ground"
        else:
            print("Not a high enough level!")
            Task['Amount'] = 0
            Task['Location'] = "ground"
elif Task['Task'] == "Chop":
    if ItemFile[ReverseItemID[Task['Object']]][1] == "Chop":
        if ItemFile[ReverseItemID[Task['Object']]][2] <= UserData['Chopping'][0]:
            Task['Object'] = ReverseItemID[Task['Object']]
            for n in wait:
                print("...")
                time.sleep(ItemFile[str(Task['Object'])][3]/(2*UserData['Chopping'][0]))
            UserData['Chopping'][1] = UserData['Chopping'][1] + 1
            UserData['Main'][1] = UserData['Main'][1] + 1
            Task['Amount'] = 1
            Task['Location'] = "ground"
        else:
            print("Not a high enough level!")
            Task['Amount'] = 0
            Task['Location'] = "ground"
    #BuddySystem(0)


            
#User Data: [0] = Level, [1] = Exp, [2] = LevelUp
#Chopping Items: [0] = Oak, [1] = Birch, [2] = Maple
#[3] = Pine, [4] = Ironwood, [5] = Elder


#[0] = Level, [1] = Exp, [2] = LevelUp, [3] = Bass, [4] = Catfish, [5] = Carp
#[6] = Trout, [7] = Salmon, [8] = Tuna ,[9] = Sword Fish, [10] = Shark


        
    

with open('../Game/UserData/UserData.json', 'w') as json_file:
    json.dump(UserData, json_file)
with open('../Game/UserData/Inv.json', 'w') as json_file:
    json.dump(Inv, json_file)
with open('../Game/Tasks/Task.json', 'w') as json_file:
    json.dump(Task, json_file)
