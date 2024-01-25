import json

with open('../Game/UserData/UserData.json', 'r') as f:
    UserData = json.load(f)

ExtraBaseHP = 0
ExtraBaseMP = 0
ExtraBaseDef = 0
ExtraBaseSDef = 0
ExtraBaseAtk = 0
ExtraBaseSAtk = 0
HPPercent = 1
MPPercent = 1
DefPercent = 1
SDefPercent = 1
AtkPercent = 1
SAtkPercent = 1
HPRegen = 1
MPRegen = 1
Block = 1
AtkSpd = 1
MovSpd = 1
MiningSpd = 1
ChoppingSpd = 1

            
if UserData['Equipment'][0] != "":
    ItemID = UserData['Equipment'][0] + ".json"
    with open('../Game/ItemIDs/' + ItemID, 'r') as f:
        ItemData = json.load(f)
        ItemData = ItemData[UserData['Equipment'][0]]
        
        ExtraBaseHP = ExtraBaseHP + ItemData[1]
        ExtraBaseMP = ExtraBaseMP + ItemData[2]
        ExtraBaseDef = ExtraBaseDef + ItemData[3]
        ExtraBaseSDef = ExtraBaseSDef + ItemData[4]
        ExtraBaseAtk = ExtraBaseAtk + ItemData[5]
        ExtraBaseSAtk = ExtraBaseSAtk + ItemData[6]
        HPPercent = HPPercent + ItemData[7]
        MPPercent = MPPercent + ItemData[8]
        DefPercent = DefPercent + ItemData[9]
        SDefPercent = SDefPercent + ItemData[10]
        AtkPercent = AtkPercent + ItemData[11]
        SAtkPercent = SAtkPercent + ItemData[12]
        HPRegen = HPRegen + ItemData[13]
        MPRegen = MPRegen + ItemData[14]
        Block = Block + ItemData[15]
        AtkSpd = AtkSpd + ItemData[16]
        MovSpd = MovSpd + ItemData[17]
        MiningSpd = MiningSpd + ItemData[18]
        ChoppingSpd = ChoppingSpd + ItemData[19]

if UserData['Equipment'][1] != "":
    ItemID = UserData['Equipment'][1] + ".json"
    with open('../Game/ItemIDs/' + ItemID, 'r') as f:
        ItemData = json.load(f)
        ItemData = ItemData[UserData['Equipment'][1]]
        
        ExtraBaseHP = ExtraBaseHP + ItemData[1]
        ExtraBaseMP = ExtraBaseMP + ItemData[2]
        ExtraBaseDef = ExtraBaseDef + ItemData[3]
        ExtraBaseSDef = ExtraBaseSDef + ItemData[4]
        ExtraBaseAtk = ExtraBaseAtk + ItemData[5]
        ExtraBaseSAtk = ExtraBaseSAtk + ItemData[6]
        HPPercent = HPPercent + ItemData[7]
        MPPercent = MPPercent + ItemData[8]
        DefPercent = DefPercent + ItemData[9]
        SDefPercent = SDefPercent + ItemData[10]
        AtkPercent = AtkPercent + ItemData[11]
        SAtkPercent = SAtkPercent + ItemData[12]
        HPRegen = HPRegen + ItemData[13]
        MPRegen = MPRegen + ItemData[14]
        Block = Block + ItemData[15]
        AtkSpd = AtkSpd + ItemData[16]
        MovSpd = MovSpd + ItemData[17]
        MiningSpd = MiningSpd + ItemData[18]
        ChoppingSpd = ChoppingSpd + ItemData[19]

if UserData['Equipment'][2] != "":
    ItemID = UserData['Equipment'][2] + ".json"
    with open('../Game/ItemIDs/' + ItemID, 'r') as f:
        ItemData = json.load(f)
        ItemData = ItemData[UserData['Equipment'][2]]
    
        ExtraBaseHP = ExtraBaseHP + ItemData[1]
        ExtraBaseMP = ExtraBaseMP + ItemData[2]
        ExtraBaseDef = ExtraBaseDef + ItemData[3]
        ExtraBaseSDef = ExtraBaseSDef + ItemData[4]
        ExtraBaseAtk = ExtraBaseAtk + ItemData[5]
        ExtraBaseSAtk = ExtraBaseSAtk + ItemData[6]
        HPPercent = HPPercent + ItemData[7]
        MPPercent = MPPercent + ItemData[8]
        DefPercent = DefPercent + ItemData[9]
        SDefPercent = SDefPercent + ItemData[10]
        AtkPercent = AtkPercent + ItemData[11]
        SAtkPercent = SAtkPercent + ItemData[12]
        HPRegen = HPRegen + ItemData[13]
        MPRegen = MPRegen + ItemData[14]
        Block = Block + ItemData[15]
        AtkSpd = AtkSpd + ItemData[16]
        MovSpd = MovSpd + ItemData[17]
        MiningSpd = MiningSpd + ItemData[18]
        ChoppingSpd = ChoppingSpd + ItemData[19]

if UserData['Equipment'][3] != "":
    ItemID = UserData['Equipment'][3] + ".json"
    with open('../Game/ItemIDs/' + ItemID, 'r') as f:
        ItemData = json.load(f)
        ItemData = ItemData[UserData['Equipment'][3]]
    
        ExtraBaseHP = ExtraBaseHP + ItemData[1]
        ExtraBaseMP = ExtraBaseMP + ItemData[2]
        ExtraBaseDef = ExtraBaseDef + ItemData[3]
        ExtraBaseSDef = ExtraBaseSDef + ItemData[4]
        ExtraBaseAtk = ExtraBaseAtk + ItemData[5]
        ExtraBaseSAtk = ExtraBaseSAtk + ItemData[6]
        HPPercent = HPPercent + ItemData[7]
        MPPercent = MPPercent + ItemData[8]
        DefPercent = DefPercent + ItemData[9]
        SDefPercent = SDefPercent + ItemData[10]
        AtkPercent = AtkPercent + ItemData[11]
        SAtkPercent = SAtkPercent + ItemData[12]
        HPRegen = HPRegen + ItemData[13]
        MPRegen = MPRegen + ItemData[14]
        Block = Block + ItemData[15]
        AtkSpd = AtkSpd + ItemData[16]
        MovSpd = MovSpd + ItemData[17]
        MiningSpd = MiningSpd + ItemData[18]
        ChoppingSpd = ChoppingSpd + ItemData[19]

if UserData['Equipment'][4] != "":
    ItemID = UserData['Equipment'][4] + ".json"
    with open('../Game/ItemIDs/' + ItemID, 'r') as f:
        ItemData = json.load(f)
        ItemData = ItemData[UserData['Equipment'][4]]
    
        ExtraBaseHP = ExtraBaseHP + ItemData[1]
        ExtraBaseMP = ExtraBaseMP + ItemData[2]
        ExtraBaseDef = ExtraBaseDef + ItemData[3]
        ExtraBaseSDef = ExtraBaseSDef + ItemData[4]
        ExtraBaseAtk = ExtraBaseAtk + ItemData[5]
        ExtraBaseSAtk = ExtraBaseSAtk + ItemData[6]
        HPPercent = HPPercent + ItemData[7]
        MPPercent = MPPercent + ItemData[8]
        DefPercent = DefPercent + ItemData[9]
        SDefPercent = SDefPercent + ItemData[10]
        AtkPercent = AtkPercent + ItemData[11]
        SAtkPercent = SAtkPercent + ItemData[12]
        HPRegen = HPRegen + ItemData[13]
        MPRegen = MPRegen + ItemData[14]
        Block = Block + ItemData[15]
        AtkSpd = AtkSpd + ItemData[16]
        MovSpd = MovSpd + ItemData[17]
        MiningSpd = MiningSpd + ItemData[18]
        ChoppingSpd = ChoppingSpd + ItemData[19]

if UserData['Equipment'][5] != "":
    ItemID = UserData['Equipment'][5] + ".json"
    with open('../Game/ItemIDs/' + ItemID, 'r') as f:
        ItemData = json.load(f)
        ItemData = ItemData[UserData['Equipment'][5]]
    
        ExtraBaseHP = ExtraBaseHP + ItemData[1]
        ExtraBaseMP = ExtraBaseMP + ItemData[2]
        ExtraBaseDef = ExtraBaseDef + ItemData[3]
        ExtraBaseSDef = ExtraBaseSDef + ItemData[4]
        ExtraBaseAtk = ExtraBaseAtk + ItemData[5]
        ExtraBaseSAtk = ExtraBaseSAtk + ItemData[6]
        HPPercent = HPPercent + ItemData[7]
        MPPercent = MPPercent + ItemData[8]
        DefPercent = DefPercent + ItemData[9]
        SDefPercent = SDefPercent + ItemData[10]
        AtkPercent = AtkPercent + ItemData[11]
        SAtkPercent = SAtkPercent + ItemData[12]
        HPRegen = HPRegen + ItemData[13]
        MPRegen = MPRegen + ItemData[14]
        Block = Block + ItemData[15]
        AtkSpd = AtkSpd + ItemData[16]
        MovSpd = MovSpd + ItemData[17]
        MiningSpd = MiningSpd + ItemData[18]
        ChoppingSpd = ChoppingSpd + ItemData[19]

if UserData['Equipment'][6] != "":
    ItemID = UserData['Equipment'][6] + ".json"
    with open('../Game/ItemIDs/' + ItemID, 'r') as f:
        ItemData = json.load(f)
        ItemData = ItemData[UserData['Equipment'][6]]
    
        ExtraBaseHP = ExtraBaseHP + ItemData[1]
        ExtraBaseMP = ExtraBaseMP + ItemData[2]
        ExtraBaseDef = ExtraBaseDef + ItemData[3]
        ExtraBaseSDef = ExtraBaseSDef + ItemData[4]
        ExtraBaseAtk = ExtraBaseAtk + ItemData[5]
        ExtraBaseSAtk = ExtraBaseSAtk + ItemData[6]
        HPPercent = HPPercent + ItemData[7]
        MPPercent = MPPercent + ItemData[8]
        DefPercent = DefPercent + ItemData[9]
        SDefPercent = SDefPercent + ItemData[10]
        AtkPercent = AtkPercent + ItemData[11]
        SAtkPercent = SAtkPercent + ItemData[12]
        HPRegen = HPRegen + ItemData[13]
        MPRegen = MPRegen + ItemData[14]
        Block = Block + ItemData[15]
        AtkSpd = AtkSpd + ItemData[16]
        MovSpd = MovSpd + ItemData[17]
        MiningSpd = MiningSpd + ItemData[18]
        ChoppingSpd = ChoppingSpd + ItemData[19]

if UserData['Equipment'][7] != "":
    ItemID = UserData['Equipment'][7] + ".json"
    with open('../Game/ItemIDs/' + ItemID, 'r') as f:
        ItemData = json.load(f)
        ItemData = ItemData[UserData['Equipment'][7]]
    
        ExtraBaseHP = ExtraBaseHP + ItemData[2]
        ExtraBaseMP = ExtraBaseMP + ItemData[3]
        ExtraBaseDef = ExtraBaseDef + ItemData[4]
        ExtraBaseSDef = ExtraBaseSDef + ItemData[5]
        ExtraBaseAtk = ExtraBaseAtk + ItemData[6]
        ExtraBaseSAtk = ExtraBaseSAtk + ItemData[7]
        HPPercent = HPPercent + ItemData[8]
        MPPercent = MPPercent + ItemData[9]
        DefPercent = DefPercent + ItemData[10]
        SDefPercent = SDefPercent + ItemData[11]
        AtkPercent = AtkPercent + ItemData[12]
        SAtkPercent = SAtkPercent + ItemData[13]
        HPRegen = HPRegen + ItemData[14]
        MPRegen = MPRegen + ItemData[15]
        Block = Block + ItemData[16]
        AtkSpd = AtkSpd + ItemData[17]
        MovSpd = MovSpd + ItemData[18]
        MiningSpd = MiningSpd + ItemData[19]
        ChoppingSpd = ChoppingSpd + ItemData[20]

if UserData['Equipment'][8] != "":
    ItemID = UserData['Equipment'][8] + ".json"
    with open('../Game/ItemIDs/' + ItemID, 'r') as f:
        ItemData = json.load(f)
        ItemData = ItemData[UserData['Equipment'][8]]
    
        ExtraBaseHP = ExtraBaseHP + ItemData[2]
        ExtraBaseMP = ExtraBaseMP + ItemData[3]
        ExtraBaseDef = ExtraBaseDef + ItemData[4]
        ExtraBaseSDef = ExtraBaseSDef + ItemData[5]
        ExtraBaseAtk = ExtraBaseAtk + ItemData[6]
        ExtraBaseSAtk = ExtraBaseSAtk + ItemData[7]
        HPPercent = HPPercent + ItemData[8]
        MPPercent = MPPercent + ItemData[9]
        DefPercent = DefPercent + ItemData[10]
        SDefPercent = SDefPercent + ItemData[10]
        AtkPercent = AtkPercent + ItemData[12]
        SAtkPercent = SAtkPercent + ItemData[13]
        HPRegen = HPRegen + ItemData[14]
        MPRegen = MPRegen + ItemData[15]
        Block = Block + ItemData[16]
        AtkSpd = AtkSpd + ItemData[17]
        MovSpd = MovSpd + ItemData[18]
        MiningSpd = MiningSpd + ItemData[19]
        ChoppingSpd = ChoppingSpd + ItemData[20]

UserData['TotalStats'][0] = (UserData['BaseStats'][0] + ExtraBaseHP) * HPPercent
UserData['TotalStats'][1] = (UserData['BaseStats'][1] + ExtraBaseMP) * MPPercent
UserData['TotalStats'][2] = (UserData['BaseStats'][2] + ExtraBaseDef) * DefPercent
UserData['TotalStats'][3] = (UserData['BaseStats'][3] + ExtraBaseSDef) * SDefPercent
UserData['TotalStats'][4] = (UserData['BaseStats'][4] + ExtraBaseAtk) * AtkPercent
UserData['TotalStats'][5] = (UserData['BaseStats'][5] + ExtraBaseSAtk) * SAtkPercent

with open('../Game/UserData/UserData.json', 'w') as json_file:
    json.dump(UserData, json_file)
