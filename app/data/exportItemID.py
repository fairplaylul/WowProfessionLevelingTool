#!/usr/bin/env python3.7

items = {
    "Blindweed": 8839,
    "Goldthorn": 3821,
    "Oily Blackmouth": 6358,
    "Crystal Vial": 8925,
    "Empty Vial": 3371,
    "Fadeleaf": 3818,
    "Leaded Vial": 3372,
    "Discolored Worg Heart": 3164,
    "Peacebloom": 2447,
    "Purple Lotus": 8831,
    "Stranglekelp": 3820,
    "Gromsblood": 8846,
    "Plaguebloom": 13466,
    "Wild Steelbloom": 3355,
    "Ghost Mushroom": 8845,
    "Khadgars Whisker": 3358,
    "Fire Oil": 6371,
    "Kingsblood": 3356,
    "Wintersbite": 3819,
    "Deviate Fish": 6522,
    "Earthroot": 2449,
    "Sungrass": 8838,
    "Firebloom": 4625,
    "Ichor of Undeath": 7972,
    "Swiftthistle": 2452,
    "Earthroot": 2449,
    "Silverleaf": 765, 
    "Large Venom Sac": 1288,
    "Bruiseweed": 2453,
    "Stonescale Oil": 13423,
    "Mountain Silversage": 13465,
    "Dreamfoil": 13463,
    "Blackmouth Oil": 6370,
    "Mageroyal": 785,
    "Briarthorn": 2450,
    "Firefin Snapper": 6359,
    "Small Flame Sac": 4402,
    "Purple Dye": 4342,
    "Volatile Rum": 9260,
    "Large Fang": 5637,
    "Dream Dust": 11176,
    "Golden Sansam": 13464,
    "Elemental Fire": 7068,
    "Elemental Water": 7070,
    "Liferoot": 3357,
    "Elemental Earth": 7067,
    "Shadow Oil": 3824,
    "Thorium Ore": 10620,
    "Minor Healing Potion": 118,
    "Mithril Ore": 3858,
    "Icecap": 13467,
    "Heart of the Wild": 10286,
    "Sharp Claw": 5635,
    "Grave Moss": 3369,
    "Stonescale Eel": 13422,
    "Wildvine": 8153,
    "Arthas Tears": 8836
}


import json
with open('itemID.json', 'w') as jsonFile:
    json.dump(items, jsonFile)