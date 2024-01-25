import json

with open('../Game/UserData/UserData.json', 'r') as f:
    UserData = json.load(f)

print("Username:", UserData['Username'])
print("Stat Points:", UserData['StatPoints'][0], "\n")

print("HP: ", UserData['CurrentStats'][0], "/", UserData['TotalStats'][0])
print("MP: ", UserData['CurrentStats'][1], "/", UserData['TotalStats'][1])
print("Atk: ", UserData['TotalStats'][4])
print("S.Atk: ", UserData['TotalStats'][5])
print("Def: ", UserData['TotalStats'][2])
print("S.Def: ", UserData['TotalStats'][3], "\n")

print("Main Level: ", UserData['Main'][0], "(", UserData['Main'][1], "/", UserData['Main'][2], ")\n")
print("Mining Level: ", UserData['Mining'][0], "(", UserData['Mining'][1], "/", UserData['Mining'][2], ")")
print("Chopping Level: ", UserData['Chopping'][0], "(", UserData['Chopping'][1], "/", UserData['Chopping'][2], ")")
