import json, time, Buddy1, Buddy2, Buddy3

with open('UserData.json', 'r') as f:
    UserData = json.load(f)

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
            if Buddy1['Task'] == "Mine":
                Buddy1['Task'] = "Mining"
            elif Buddy1['Task'] == "Chop":
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
                    if Buddy1['Task'] == "Mine":
                        Buddy1['Task'] = "Mining"
                    elif Buddy1['Task'] == "Chop":
                        Buddy1['Task'] = "Chopping"
                    Buddy1['Object'] = BuddyTaskArray[1]
                    with open('Buddy1Data.json', 'w') as json_file:
                        json.dump(Buddy1, json_file)
                    exec(open("Buddy1.py").read())
                elif BuddyNumber == "2":
                    Buddy2['Task'] = BuddyTaskArray[0]
                    if Buddy2['Task'] == "Mine":
                        Buddy2['Task'] = "Mining"
                    elif Buddy2['Task'] == "Chop":
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
                    if Buddy1['Task'] == "Mine":
                        Buddy1['Task'] = "Mining"
                    elif Buddy1['Task'] == "Chop":
                        Buddy1['Task'] = "Chopping"
                    Buddy1['Object'] = BuddyTaskArray[1]
                    with open('Buddy1Data.json', 'w') as json_file:
                        json.dump(Buddy1, json_file)
                    exec(open("Buddy1.py").read())
                elif BuddyNumber == "2":
                    Buddy2['Task'] = BuddyTaskArray[0]
                    if Buddy2['Task'] == "Mine":
                        Buddy2['Task'] = "Mining"
                    elif Buddy2['Task'] == "Chop":
                        Buddy2['Task'] = "Chopping"
                    Buddy2['Object'] = BuddyTaskArray[1]
                    with open('Buddy2Data.json', 'w') as json_file:
                        json.dump(Buddy2, json_file)
                    exec(open("Buddy2.py").read())
                elif BuddyNumber == "3":
                    Buddy3['Task'] = BuddyTaskArray[0]
                    if Buddy3['Task'] == "Mine":
                        Buddy3['Task'] = "Mining"
                    elif Buddy3['Task'] == "Chop":
                        Buddy3['Task'] = "Chopping"
                    Buddy3['Object'] = BuddyTaskArray[1]
                    with open('Buddy3Data.json', 'w') as json_file:
                        json.dump(Buddy3, json_file)
                    exec(open("Buddy3.py").read())
    else:
        print("You unlock buddies at Level 10!")
