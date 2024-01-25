#pip install keyboard on cmd
import json, keyboard, time, Buddy1, Buddy2, Buddy3, Levels

afk = "off"

with open('Task.json', 'r') as f:
    Task = json.load(f)

print("Welcome to ConsoleRPG!")

newgame = input("Do you want to start a new game?(y/n)\n")
if newgame == "y":
    with open('NewUserData.json', 'r') as f:
        UserData = json.load(f)
    with open('NewInvData.json', 'r') as f:
        Inv = json.load(f)
    UserData['Username'] = input("Ok! Whats your name?\n")
    Game = 1
elif newgame == "n":
    with open('UserData.json', 'r') as f:
        UserData = json.load(f)
    with open('InvData.json', 'r') as f:
        Inv = json.load(f)
    Game = 1

def BuddySystem(BuddyNumber):
    with open('Buddy1Data.json', 'r') as f:
        Buddy1 = json.load(f)
    with open('Buddy2Data.json', 'r') as f:
        Buddy2 = json.load(f)
    with open('Buddy3Data.json', 'r') as f:
        Buddy3 = json.load(f)
        
    if BuddyNumber == 0:
        if Buddy1['Task'] != "" and Buddy1['Object'] != "":
            UserData[Buddy1['Task']][1] = UserData[Buddy1['Task']][1] + Buddy1['exp']
            UserData['Main'][1] = UserData['Main'][1] + Buddy1['exp']
            Inv['Mining'][Buddy1['ObjectValue']] = Inv['Mining'][Buddy1['ObjectValue']] + 1
            print("Buddy 1 is also " + Buddy1['Task'] + " " + Buddy1['Object'] + ".")
        if Buddy2['Task'] != "" and Buddy2['Object'] != "":
            UserData[Buddy2['Task']][1] = UserData[Buddy2['Task']][1] + Buddy2['exp']
            UserData['Main'][1] = UserData['Main'][1] + Buddy2['exp']
            Inv['Mining'][Buddy2['ObjectValue']] = Inv['Mining'][Buddy2['ObjectValue']] + 1
            print("Buddy 2 is also " + Buddy2['Task'] + " " + Buddy2['Object'] + ".")
        if Buddy3['Task'] != "" and Buddy3['Object'] != "":
            UserData[Buddy3['Task']][1] = UserData[Buddy3['Task']][1] + Buddy3['exp']
            UserData['Main'][1] = UserData['Main'][1] + Buddy3['exp']
            Inv['Mining'][Buddy3['ObjectValue']] = Inv['Mining'][Buddy3['ObjectValue']] + 1
            print("Buddy 3 is also " + Buddy3['Task'] + " " + Buddy3['Object'] + ".")
    
print("Hi", UserData['Username'], "! type 'List' for a list of commands.\n")
while(Game == 1):
    #afk off
    if afk == "off":
        Task['Task'] = input("What would you like to do?\n")
        with open('Task.json', 'w') as json_file:
            json.dump(Task, json_file)

    #opens task list
    if Task['Task'] == "List" or Task['Task'] == "list":
        print("Levels\nInv\nSave\nMine\nChop")
    #opens mine list
    elif Task['Task'] == "Mine" or Task['Task'] == "mine":
        print("You can mine the following:\nStone(Level 1)\nCoal(Level 5)\nTin Ore (Level 10)\nCopper Ore (Level 15)\nIron Ore (Level 25)\nGold Ore(Level 35)\nTitanium Ore (Level 45)\nDiamond (Level 55)\nTungsten (Level 75)\nMeteorite (Level 85)")
    #opens chop list
    elif Task['Task'] == "Chop" or Task['Task'] == "chop":
        print("You can chop the following:\nOak (Level 1)\nBirch (Level 5)\nMaple (Level 10)\nPine (Level 15)\nIron Wood (Level 25)\nElder (Level 35)")
    #shows user stats
    elif Task['Task'] == "Levels" or Task['Task'] == "levels":
        exec(open("Levels.py").read())
    #shows inventory
    elif Task['Task'] == "Inv" or Task['Task'] == "inv" or Task['Task'] == "Inventory" or Task['Task'] == "inventory":
        print("Stone: ", Inv['Mining'][0], "\nCoal: ", Inv['Mining'][1], "\nTin: ", Inv['Mining'][2], "\nCopper: ", Inv['Mining'][3], "\nOak: ", Inv['Chopping'][0], "\nBirch: ", Inv['Chopping'][1])
    #turns on afk mode
    elif Task['Task'] == "afk":
        Task['Task'] = input("What task would you like to afk: ")
        afk = "on"
    #sets buddy task
    elif Task['Task'] == "SetBuddy" or Task['Task'] == "Setbuddy" or Task['Task'] == "setBuddy" or Task['Task'] == "setbuddy":
        with open('Buddy1Data.json', 'r') as f:
            Buddy1 = json.load(f)
        with open('Buddy2Data.json', 'r') as f:
            Buddy2 = json.load(f)
        with open('Buddy3Data.json', 'r') as f:
            Buddy3 = json.load(f)
            
        if UserData['Main'][0] >= 10:
            if UserData['Main'][0] < 20:
                BuddyNumber = 1
                print("What would you like Buddy 1 to do?")
                BuddyTask = input()
                BuddyTaskArray = BuddyTask.split(' ')
                Buddy1['Task'] = BuddyTaskArray[0]
                if Buddy1['Task'] == "Mine" or Buddy1['Task'] == "mine":
                    Buddy1['Task'] = "Mining"
                elif Buddy1['Task'] == "Chop" or Buddy1['Task'] == "chop":
                    Buddy1['Task'] = "Chopping"
                Buddy1['Object'] = BuddyTaskArray[1]
                with open('Buddy1Data.json', 'w') as json_file:
                    json.dump(Buddy1, json_file)
                exec(open("Buddy1.py").read())
            elif UserData['Main'][0] >= 20 and UserData['Main'][0] < 30:
                BuddyNumber = input("Which Buddy?\n")
                if BuddyNumber != "1" and BuddyNumber != "2":
                    print("You haven't found anymore buddies yet :')")
                else:
                    print("What would you like Buddy ", BuddyNumber, " to do?")
                    BuddyTask = input()
                    BuddyTaskArray = BuddyTask.split(' ')
                    if BuddyNumber == "1":
                        Buddy1['Task'] = BuddyTaskArray[0]
                        if Buddy1['Task'] == "Mine" or Buddy1['Task'] == "mine":
                            Buddy1['Task'] = "Mining"
                        elif Buddy1['Task'] == "Chop" or Buddy1['Task'] == "chop":
                            Buddy1['Task'] = "Chopping"
                        Buddy1['Object'] = BuddyTaskArray[1]
                        with open('Buddy1Data.json', 'w') as json_file:
                            json.dump(Buddy1, json_file)
                        exec(open("Buddy1.py").read())
                    elif BuddyNumber == "2":
                        Buddy2['Task'] = BuddyTaskArray[0]
                        if Buddy2['Task'] == "Mine" or Buddy2['Task'] == "mine":
                            Buddy2['Task'] = "Mining"
                        elif Buddy2['Task'] == "Chop" or Buddy2['Task'] == "chop":
                            Buddy2['Task'] = "Chopping"
                        Buddy2['Object'] = BuddyTaskArray[1]
                        with open('Buddy2Data.json', 'w') as json_file:
                            json.dump(Buddy2, json_file)
                        exec(open("Buddy2.py").read())
            elif UserData['Main'][0] >= 30:
                BuddyNumber = input("Which Buddy?")
                if BuddyNumber != "1" and BuddyNumber != "2" and BuddyNumber != "3":
                    print("There's only 3 Buddies, the rest of the buddies are dead :'(")
                else:
                    print("What would you like Buddy ", BuddyNumber, " to do?")
                    BuddyTask = input()
                    BuddyTaskArray = BuddyTask.split(' ')
                    if BuddyNumber == "1":
                        Buddy1['Task'] = BuddyTaskArray[0]
                        if Buddy1['Task'] == "Mine" or Buddy1['Task'] == "mine":
                            Buddy1['Task'] = "Mining"
                        elif Buddy1['Task'] == "Chop" or Buddy1['Task'] == "chop":
                            Buddy1['Task'] = "Chopping"
                        Buddy1['Object'] = BuddyTaskArray[1]
                        with open('Buddy1Data.json', 'w') as json_file:
                            json.dump(Buddy1, json_file)
                        exec(open("Buddy1.py").read())
                    elif BuddyNumber == "2":
                        Buddy2['Task'] = BuddyTaskArray[0]
                        if Buddy2['Task'] == "Mine" or Buddy2['Task'] == "mine":
                            Buddy2['Task'] = "Mining"
                        elif Buddy2['Task'] == "Chop" or Buddy2['Task'] == "chop":
                            Buddy2['Task'] = "Chopping"
                        Buddy2['Object'] = BuddyTaskArray[1]
                        with open('Buddy2Data.json', 'w') as json_file:
                            json.dump(Buddy2, json_file)
                        exec(open("Buddy2.py").read())
                    elif BuddyNumber == "3":
                        Buddy3['Task'] = BuddyTaskArray[0]
                        if Buddy3['Task'] == "Mine" or Buddy3['Task'] == "mine":
                            Buddy3['Task'] = "Mining"
                        elif Buddy3['Task'] == "Chop" or Buddy3['Task'] == "chop":
                            Buddy3['Task'] = "Chopping"
                        Buddy3['Object'] = BuddyTaskArray[1]
                        with open('Buddy3Data.json', 'w') as json_file:
                            json.dump(Buddy3, json_file)
                        exec(open("Buddy3.py").read())
    elif Task['Task'] == "Save" or Task['Task'] == "save":
        print("Saving...")
        with open('UserData.json', 'w') as json_file:
            json.dump(UserData, json_file)
        with open('InvData.json', 'w') as json_file:
            json.dump(Inv, json_file)
        print("Saved!")
        Exit = input("Would you like to exit the game? (y/n)\n")
        if Exit == 'y':
            Game = 0
            exit()

    #User Data: [0] = Level, [1] = Exp, [2] = LevelUp,
            
    #Mining Items: [0] = Stone(1), [1] = Coal(5), [2] = Tin (10), [3] = Copper (15), [4] = Iron(25) 
    #[5] Gold(35), [6] = Titanium(45), [7] Diamond(55), [8] = Tungsten (75), [9] = Meteorite (85)
    if Task['Task'] == "Mine Stone" or Task['Task'] == "Mine stone" or Task['Task'] == "mine Stone" or Task['Task'] == "mine stone":
        wait = range(5)
        for n in wait:
            print("...")
            time.sleep(1/UserData['Mining'][0])
        UserData['Mining'][1] = UserData['Mining'][1] + 1
        UserData['Main'][1] = UserData['Main'][1] + 1
        Inv['Mining'][0] = Inv['Mining'][0] + 1
        BuddySystem(0)
        print("Got 1 Stone!")
        print("Gained 1 Exp!\nMain Exp: (", UserData['Main'][1], "/", UserData['Main'][2], ")\nMining Exp: (", UserData['Mining'][1], "/", UserData['Mining'][2], ")\nStone: ", Inv['Mining'][0])
    elif Task['Task'] == "Mine Coal" or Task['Task'] == "Mine coal" or Task['Task'] == "mine Coal" or Task['Task'] == "mine coal":
        if UserData['Mining'][0] >= 5:
            wait = range(5)
            for n in wait:
                print("...")
                time.sleep(5/UserData['Mining'][0])
            UserData['Mining'][1] = UserData['Mining'][1] + 5
            UserData['Main'][1] = UserData['Main'][1] + 5
            Inv['Mining'][1] = Inv['Mining'][1] + 1
            BuddySystem(0)
            print("Got 1 Coal!")
            print("Gained 5 Exp!\nMain Exp: (", UserData['Main'][1], "/", UserData['Main'][2], ")\nMining Exp: (", UserData['Mining'][1], "/", UserData['Mining'][2], ")\nCoal: ", Inv['Mining'][1])
        else:
            print("Must be Mining Level 5 or greater.")
            afk = "off"
    elif Task['Task'] == "Mine Tin" or Task['Task'] == "Mine tin" or Task['Task'] == "mine Tin" or Task['Task'] == "mine tin":
        if UserData['Mining'][0] >= 10:
            wait = range(5)
            for n in wait:
                print("...")
                time.sleep(10/UserData['Mining'][0])
            UserData['Mining'][1] = UserData['Mining'][1] + 10
            UserData['Main'][1] = UserData['Main'][1] + 10
            Inv['Mining'][2] = Inv['Mining'][2] + 1
            BuddySystem(0)
            print("Got 1 Tin Ore!")
            print("Gained 10 Exp!\nMain Exp: (", UserData['Main'][1], "/", UserData['Main'][2], ")\nMining Exp: (", UserData['Mining'][1], "/", UserData['Mining'][2], ")\nTin Ore: ", Inv['Mining'][2])
        else:
            print("Must be Mining Level 10 or greater.")
            afk = "off"
    elif Task['Task'] == "Mine Copper" or Task['Task'] == "Mine copper" or Task['Task'] == "mine Copper" or Task['Task'] == "mine copper":
        if UserData['Mining'][0] >= 15:
            wait = range(5)
            for n in wait:
                print("...")
                time.sleep(15/UserData['Mining'][0])
            UserData['Mining'][1] = UserData['Mining'][1] + 25
            UserData['Main'][1] = UserData['Main'][1] + 25
            Inv['Mining'][3] = Inv['Mining'][3] + 1
            BuddySystem(0)
            print("Got 1 Copper Ore!")
            print("Gained 25 Exp!\nMain Exp: (", UserData['Main'][1], "/", UserData['Main'][2], ")\nMining Exp: (", UserData['Mining'][1], "/", UserData['Mining'][2], ")\nCopper Ore: ", Inv['Mining'][3])
        else:
            print("Must be Mining Level 15 or greater.")
            afk = "off"

            
    #User Data: [0] = Level, [1] = Exp, [2] = LevelUp
    #Chopping Items: [0] = Oak, [1] = Birch, [2] = Maple
    #[3] = Pine, [4] = Ironwood, [5] = Elder
    if Task['Task'] == "Chop Oak" or Task['Task'] == "chop Oak" or Task['Task'] == "Chop oak" or Task['Task'] == "chop oak":
        wait = range(5)
        for n in wait:
            print("...")
            time.sleep(1/UserData['Chopping'][0])
        UserData['Chopping'][1] = UserData['Chopping'][1] + 1
        UserData['Main'][1] = UserData['Main'][1] + 1
        Inv['Chopping'][0] = Inv['Chopping'][0] + 1
        BuddySystem(0)
        print("Got 1 Oak!")
        print("Gained 1 Exp!\nMain Exp: (", UserData['Main'][1], "/", UserData['Main'][2], ")\nChopping Exp: (", UserData['Chopping'][1], "/", UserData['Chopping'][2], ")\nOak: ", Inv['Chopping'][0])
    elif Task['Task'] == "Chop Birch" or Task['Task'] == "chop Birch" or Task['Task'] == "Chop birch" or Task['Task'] == "chop birch":
        if UserData['Chopping'][0] >= 5:
            wait = range(5)
            for n in wait:
                print("...")
                time.sleep(5/UserData['Chopping'][0])
            UserData['Chopping'][1] = UserData['Chopping'][1] + 5
            UserData['Main'][1] = UserData['Main'][1] + 5
            Inv['Chopping'][1] = Inv['Chopping'][1] + 1
            BuddySystem(0)
            print("Got 1 Birch!")
            print("Gained 1 Exp!\nMain Exp: (", UserData['Main'][1], "/", UserData['Main'][2], ")\nChopping Exp: (", UserData['Chopping'][1], "/", UserData['Chopping'][2], ")\nBirch: ", Inv['Chopping'][1])
        else:
            print("Must be Chopping Level 5 or greater.")
            afk = "off"

    #[0] = Level, [1] = Exp, [2] = LevelUp, [3] = Bass, [4] = Catfish, [5] = Carp
    #[6] = Trout, [7] = Salmon, [8] = Tuna ,[9] = Sword Fish, [10] = Shark
        
    if(UserData['Main'][1] >= UserData['Main'][2]):
        UserData['Main'][1] = 0
        UserData['Main'][0] = UserData['Main'][0] + 1
        UserData['Main'][2] = pow(2.71828183, UserData['Main'][0])
        UserData['StatPoints'][0] = UserData['StatPoints'][0] + 3
        
    if(UserData['Mining'][1] >= UserData['Mining'][2]):
        UserData['Mining'][1] = 0
        UserData['Mining'][0] = UserData['Mining'][0] + 1
        UserData['Mining'][2] = pow(2.71828183, UserData['Mining'][0])
        UserData['StatPoints'][0] = UserData['StatPoints'][0] + 1
        print("Mining leveled up to level: ", UserData['Mining'][0])
        if UserData['Mining'][0] == 5:
            print("You can now mine for coal!")
        elif UserData['Mining'][0] == 10:
            print("You can now mine for tin ore!")
        elif UserData['Mining'][0] == 15:
            print("You can now mine for copper ore!")
            
    if(UserData['Chopping'][1] >= UserData['Chopping'][2]):
        UserData['Chopping'][1] = 0
        UserData['Chopping'][0] = UserData['Chopping'][0] + 1
        UserData['Chopping'][2] = pow(2.71828183, UserData['Chopping'][0])
        UserData['StatPoints'][0] = UserData['StatPoints'][0] + 1
        print("Chopping leveled up to level: ", UserData['Chopping'][0])
        if UserData['Chopping'][0] == 5:
            print("You can now chop birch trees!")

    if keyboard.is_pressed("esc"):
        afk = "off"
        
    


