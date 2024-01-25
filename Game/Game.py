import json, time

with open('../Game/ItemIDs/ItemID.json', 'r') as f:
    ItemID_Dict = json.load(f)

with open('../Game/ItemIDs/RevisedItemID.json', 'r') as f:
    RevisedItemID_Dict = json.load(f)

with open('../Game/Tasks/Task.json', 'r') as f:
    Task = json.load(f)

Task['Task'] = ""

with open('../Game/Tasks/Task.json', 'w') as json_file:
    json.dump(Task, json_file)

print("Welcome to ConsoleRPG!")

newgameloop = 1
while newgameloop == 1:
    newgame = input("Do you want to start a new game?(y/n)\n")
    if newgame == "y":
        newgame = input("Are you sure? This will reset any current save data.\n")
        if newgame == "y":
            with open('../Game/UserData/NewUserData.json', 'r') as f:
                UserData = json.load(f)
            with open('../Game/UserData/NewInvData.json', 'r') as f:
                Inv = json.load(f)
            with open('../Game/UserData/NewChestData.json', 'r') as f:
                Chest = json.load(f)
            UserData['Username'] = input("Ok! Whats your name?\n")
            with open('../Game/UserData/Inv.json', 'w') as json_file:
                json.dump(Inv, json_file)
            with open('../Game/UserData/Chest.json', 'w') as json_file:
                json.dump(Chest, json_file)
            newgameloop = 0
            Game = 1
        else:
            newgameloop = 1
    elif newgame == "n":
        with open('../Game/UserData/UserData.json', 'r') as f:
            UserData = json.load(f)
        with open('../Game/UserData/Inv.json', 'r') as f:
            Inv = json.load(f)
        with open('../Game/UserData/Chest.json', 'r') as f:
            Chest = json.load(f)
        Game = 1
        newgameloop = 0
    
print("Hi", UserData['Username'], "! type 'List' for a list of commands.\n")
while(Game == 1):
    with open('../Game/UserData/UserData.json', 'w') as json_file:
        json.dump(UserData, json_file)
    with open('../Game/UserData/Inv.json', 'r') as f:
        Inv = json.load(f)
    with open('../Game/UserData/Chest.json', 'r') as f:
        Chest = json.load(f)
        

    Task['Task'] = ""
    Task['Task'] = input("What would you like to do?\n")
    TaskArray = Task['Task'].split(' ')
    with open('../Game/Tasks/Task.json', 'w') as json_file:
        json.dump(Task, json_file)
    try:
        #opens task list
        if Task['Task'] == "List":
            print("Stats\nInv\nDrop <Slot #>\nChest\nMine <Object>\nChop <Object>\n")
        #opens mine list
        elif Task['Task'] == "Mine":
            print("You can mine the following:\nStone(Level 1)\nCoal(Level 5)\nTin Ore (Level 10)\nCopper Ore (Level 15)\nIron Ore (Level 25)\nGold Ore(Level 35)\nTitanium Ore (Level 45)\nDiamond (Level 55)\nTungsten (Level 75)\nMeteorite (Level 85)")
        #opens chop list
        elif Task['Task'] == "Chop":
            print("You can chop the following:\nOak (Level 1)\nBirch (Level 5)\nMaple (Level 10)\nPine (Level 15)\nIron Wood (Level 25)\nElder (Level 35)")
        #shows user stats
        elif Task['Task'] == "Stats":
            exec(open("Stats.py").read())
        elif Task['Task'] == "Equipment":
            exec(open("Equipment.py").read())
        #shows inventory
        elif Task['Task'] == "Inv":
            i = 1
            while i <= 10:
                if Inv['Slot ' + str(i)][0] != "":
                    print("Slot ", str(i), ":", Inv['Slot ' + str(i)][1], ItemID_Dict[Inv['Slot ' + str(i)][0]])
                    i = i + 1
                else:
                    i = i + 1
        elif Task['Task'] == "Chest":
            i = 1
            while i <= 30:
                if Chest['Slot ' + str(i)][0] != "":
                    print("Slot ", str(i), ":", Chest['Slot ' + str(i)][1], ItemID_Dict[Chest['Slot ' + str(i)][0]])
                    i = i + 1
                else:
                    i = i + 1
        elif TaskArray[0] == "Equip":
            Task['Object'] = TaskArray[1] + " " + TaskArray[2]
            with open('../Game/Tasks/Task.json', 'w') as json_file:
                json.dump(Task, json_file)
            exec(open("Equipt Equipment.py").read())
            exec(open("RemoveFromInv.py").read())
            exec(open("UpdateStats.py").read())
        elif TaskArray[0] == "Drop":
            Task['Object'] = TaskArray[1] + " " + TaskArray[2]
            with open('../Game/Tasks/Task.json', 'w') as json_file:
                json.dump(Task, json_file)
            exec(open("RemoveFromInv.py").read())
        elif TaskArray[0] == "ToChest":
            Task['Object'] = TaskArray[1] + " " + TaskArray[2]
            Task['Task'] = TaskArray[0]
            with open('../Game/Tasks/Task.json', 'w') as json_file:
                json.dump(Task, json_file)
            exec(open("AddToChest.py").read())
            exec(open("RemoveFromInv.py").read())
        elif TaskArray[0] == "FromChest":
            Task['Object'] = TaskArray[1] + " " + TaskArray[2]
            Task['Task'] = TaskArray[0]
            Task['Location'] = "chest"
            with open('../Game/Tasks/Task.json', 'w') as json_file:
                json.dump(Task, json_file)
            exec(open("AddToInv.py").read())
            exec(open("RemoveFromChest.py").read())
        #sets buddy tsk
        #elif Task['Task'] == "SetBuddy":
        #    exec(open("RunBuddies.py").read())
        elif TaskArray[0] == "Mine" or TaskArray[0] == "Chop":
            Task['Object'] = TaskArray[1]
            Task['Task'] = TaskArray[0]
            with open('../Game/Tasks/Task.json', 'w') as json_file:
                json.dump(Task, json_file)
            exec(open("ResourceTask.py").read())
            exec(open("AddToInv.py").read())
        else:
            print("Probably not a task yet")

        exec(open("LevelUp.py").read())
    except:
        print("Not a valid command")


