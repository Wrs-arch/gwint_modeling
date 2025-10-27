import numpy as np
'''
parsed by DeepSeek and QWen
name, type, row, strength, ability, source, count
'''
gwent_cards_north = {
    1: {"name": "Ballista", "type": "Unit", "row": "Siege", "strength": 6, "ability": "", "source": "Part of the base deck", 'count':1},
    2: {"name": "Blue Stripes Commando", "type": "Unit", "row": "Close Combat", "strength": 4, "ability": "Tight Bond: Place next to a card with the same name to double the strength of both cards.", "source": "1 purchased from Elsa or Bram in White Orchard, 1 purchased from Crow's Perch's quartermaster, 1 purchased from Midcopse's merchant", 'count':3},
    3: {"name": "Catapult", "type": "Unit", "row": "Siege", "strength": 8, "ability": "Tight Bond: Place next to a card with the same name to double the strength of both cards.", "source": "1 purchased from Elsa or Bram in White Orchard, 1 purchased from Marquise Serenity at the Passiflora, Hearts of Stone expansion: 1 can be purchased from the merchant at the circus camp near Carsten", 'count':3},
    4: {"name": "Crinfrid Reavers Dragon Hunter", "type": "Unit", "row": "Ranged Combat", "strength": 5, "ability": "Tight Bond: Place next to a card with the same name to double the strength of both cards.", "source": "1 purchased from Elsa or Bram in White Orchard, 1 purchased from Claywich's merchant, 1 purchased from Midcopse's merchant", 'count':3},
    5: {"name": "Dethmold", "type": "Unit", "row": "Ranged Combat", "strength": 6, "ability": "", "source": "Part of the base deck", 'count':1},
    6: {"name": "Dun Banner Medic", "type": "Unit", "row": "Siege", "strength": 5, "ability": "Medic: Choose one card from your discard pile and play it instantly (no Heroes or Special Cards).", "source": "Part of the base deck", 'count':1},
    7: {"name": "Esterad Thyssen", "type": "Hero", "row": "Close Combat", "strength": 10, "ability": "Hero: Not affected by any Special Cards or abilities.", "source": "Won from Sigismund Dijkstra during Gwent: Big City Players", 'count':1},
    8: {"name": "Foltest: King of Temeria", "type": "leader", "row": "", "strength": "", "ability": "Pick an Impenetrable Fog card from your deck and play it instantly.", "source": "Part of the base deck", 'count':1},
    9: {"name": "Foltest: Lord Commander of the North", "type": "leader", "row": "", "strength": "", "ability": "Clear any weather effects (resulting from Biting Frost, Torrential Rain or Impenetrable Fog cards) in play.", "source": "Purchased from Elsa or Bram in White Orchard", 'count':1},
    10: {"name": "Foltest: Son of Medell", "type": "leader", "row": "", "strength": "", "ability": "Destroy your enemy's strongest Ranged Combat unit(s) if the combined strength of all his or her Ranged Combat units is 10 or more.", "source": "Purchased from the merchant at the circus camp near Carsten", 'count':1},
    11: {"name": "Foltest: The Siegemaster", "type": "leader", "row": "", "strength": "", "ability": "Doubles the strength of all your Siege units (unless a Commander's Horn is also present on that row).", "source": "Won from the Nilfgaardian nobleman in Vizima", 'count':1},
    12: {"name": "Foltest: The Steel-Forged", "type": "leader", "row": "", "strength": "", "ability": "Destroy your enemy's strongest Siege unit(s) if the combined strength of all his or her Siege units is 10 or more.", "source": "Won during High Stakes", 'count':1},
    13: {"name": "John Natalis", "type": "Hero", "row": "Close Combat", "strength": 10, "ability": "Hero: Not affected by any Special Cards or abilities.", "source": "A Dangerous Game or Prison Warden during The Great Escape", 'count':1},
    14: {"name": "Kaedweni Siege Expert", "type": "Unit", "row": "Siege", "strength": 1, "ability": "Morale boost: Adds +1 to all units in the row (excluding itself).", "source": "Part of the base deck", 'count':1},
    15: {"name": "Keira Metz", "type": "Unit", "row": "Ranged Combat", "strength": 5, "ability": "", "source": "Part of the base deck", 'count':1},
    16: {"name": "Philippa Eilhart", "type": "Hero", "row": "Ranged Combat", "strength": 10, "ability": "Hero: Not affected by any Special Cards or abilities.", "source": "Random reward from gwent players", 'count':1},
    17: {"name": "Poor Fucking Infantry", "type": "Unit", "row": "Close Combat", "strength": 1, "ability": "Tight Bond: Place next to a card with the same name to double the strength of both cards.", "source": "1 part of the base deck, 1 purchased from Lindenvale's merchant, 1 purchased from Midcopse's merchant", 'count':3},
    18: {"name": "Prince Stennis", "type": "Unit", "row": "Close Combat", "strength": 5, "ability": "Spy: Place on your opponent's battlefield (counts towards opponent's total) and draw 2 cards from your deck.", "source": "Part of the base deck", 'count':1},
    19: {"name": "Redanian Foot Soldier", "type": "Unit", "row": "Close Combat", "strength": 1, "ability": "", "source": "Part of the base deck", 'count':1},
    20: {"name": "Sabrina Glevissig", "type": "Unit", "row": "Ranged Combat", "strength": 4, "ability": "", "source": "Part of the base deck", 'count':1},
    21: {"name": "Sheldon Skaggs", "type": "Unit", "row": "Ranged Combat", "strength": 4, "ability": "", "source": "Part of the base deck", 'count':1},
    22: {"name": "Siege Tower", "type": "Unit", "row": "Siege", "strength": 6, "ability": "", "source": "Random reward from gwent players", 'count':1},
    23: {"name": "Siegfried of Denesle", "type": "Unit", "row": "Close Combat", "strength": 5, "ability": "", "source": "Part of the base deck", 'count':1},
    24: {"name": "Sigismund Dijkstra", "type": "Unit", "row": "Close Combat", "strength": 4, "ability": "Spy: Place on your opponent's battlefield (counts towards opponent's total) and draw 2 cards from your deck.", "source": "Phillip Strenger during Gwent: Velen Players", 'count':1},
    25: {"name": "Síle de Tansarville", "type": "Unit", "row": "Ranged Combat", "strength": 5, "ability": "", "source": "Part of the base deck", 'count':1},
    26: {"name": "Thaler", "type": "Unit", "row": "Siege", "strength": 1, "ability": "Spy: Place on your opponent's battlefield (counts towards opponent's total) and draw 2 cards from your deck.", "source": "Purchased from Arinbjorn's innkeep", 'count':1},
    27: {"name": "Trebuchet", "type": "Unit", "row": "Siege", "strength": 6, "ability": "", "source": "Part of the base deck", 'count':1},
    28: {"name": "Vernon Roche", "type": "Hero", "row": "Close Combat", "strength": 10, "ability": "Hero: Not affected by any Special Cards or abilities.", "source": "Won from Haddy during Gwent: Velen Players", 'count':1},
    29: {"name": "Ves", "type": "Unit", "row": "Close Combat", "strength": 5, "ability": "", "source": "Part of the base deck", 'count':1},
    30: {"name": "Yarpen Zigrin", "type": "Unit", "row": "Close Combat", "strength": 2, "ability": "", "source": "Part of the base deck", 'count':1}
}

gwent_cards_nilfgaard = {
    31: {"name": "Albrich", "type": "Unit", "row": "Ranged Combat", "strength": 2, "ability": "", "source": "Purchase from Crow's Perch's merchant or Devil's Pit's merchant", 'count':1},
    32: {"name": "Assire var Anahid", "type": "Unit", "row": "Ranged Combat", "strength": 6, "ability": "", "source": "Random reward from gwent players", 'count':1},
    33: {"name": "Black Infantry Archer", "type": "Unit", "row": "Ranged Combat", "strength": 10, "ability": "", "source": "1 purchased from Claywich's merchant, 1 purchased from Lindenvale's merchant", 'count':2},
    34: {"name": "Cahir Mawr Dyffryn aep Ceallach", "type": "Unit", "row": "Close Combat", "strength": 6, "ability": "", "source": "Random reward from gwent players", 'count':1},
    35: {"name": "Cynthia", "type": "Unit", "row": "Ranged Combat", "strength": 4, "ability": "", "source": "Purchased from Crow's Perch's quartermaster", 'count':1},
    36: {"name": "Emhyr var Emreis: Emperor of Nilfgaard", "type": "leader", "row": "", "strength": "", "ability": "Emperor of Nilfgaard: Look at 3 random cards from your opponent's hand.", "source": "Purchased from Inn at the Crossroads's innkeep, Purchased from Lindenvale's innkeep", 'count':1},
    37: {"name": "Emhyr var Emreis: His Imperial Majesty", "type": "leader", "row": "", "strength": "", "ability": "His Imperial Majesty: Pick a Torrential Rain card from your deck and play it instantly.", "source": "Part of the base deck", 'count':1},
    38: {"name": "Emhyr var Emreis: Invader of the North", "type": "leader", "row": "", "strength": "", "ability": "Invader of the North: Abilities that restore a unit to the battlefield restore a randomly-chosen unit. Affects both players.", "source": "Purchased from the merchant at the circus camp near Carsten", 'count':1},
    39: {"name": "Emhyr var Emreis: The Relentless", "type": "leader", "row": "", "strength": "", "ability": "The Relentless: Draw a card from your opponent's discard pile.", "source": "Won from Sasha during High Stakes", 'count':1},
    40: {"name": "Emhyr var Emreis: The White Flame", "type": "leader", "row": "", "strength": "", "ability": "The White Flame: Cancel your opponent's Leader Ability.", "source": "Won during Gwent: Skellige Style", 'count':1},
    41: {"name": "Etolian Auxiliary Archers", "type": "Unit", "row": "Ranged Combat", "strength": 1, "ability": "Medic: Choose one card from your discard pile and play it instantly (no Heroes or Special Cards).", "source": "1 purchased from Claywich's merchant, 1 purchased from Lindenvale's merchant", 'count':2},
    42: {"name": "Fringilla Vigo", "type": "Unit", "row": "Ranged Combat", "strength": 6, "ability": "", "source": "A Dangerous Game or Prison Warden during The Great Escape", 'count':1},
    43: {"name": "Heavy Zerrikanian Fire Scorpion", "type": "Unit", "row": "Siege", "strength": 10, "ability": "", "source": "Purchase from Lindenvale's merchant", 'count':1},
    44: {"name": "Impera Brigade Guard", "type": "Unit", "row": "Close Combat", "strength": 3, "ability": "Tight Bond: Place next to a card with the same name to double the strength of both cards.", "source": "1 purchased from Cunny of the Goose's innkeep, 1 purchased from Seven Cats Inn's innkeep, 1 purchased from Crow's Perch's merchant or Devil's Pit's merchant, 1 purchased from Inn at the Crossroads's innkeep or Lindenvale's innkeep", 'count':4},
    45: {"name": "Letho of Gulet", "type": "Hero", "row": "Close Combat", "strength": 10, "ability": "Hero: Not affected by any Special Cards or abilities.", "source": "Won from the Boatwright during Gwent: Velen Players", 'count':1},
    46: {"name": "Menno Coehoorn", "type": "Hero", "row": "Close Combat", "strength": 10, "ability": "Hero: Not affected by any Special Cards or abilities. Medic: Choose one card from your discard pile and play it instantly (no Heroes or Special Cards).", "source": "Won from Inn at the Crossroads's innkeep during Gwent: Playing Innkeeps", 'count':1},
    47: {"name": "Morteisen", "type": "Unit", "row": "Close Combat", "strength": 3, "ability": "", "source": "Purchased from Midcopse's merchant", 'count':1},
    48: {"name": "Morvran Voorhis", "type": "Hero", "row": "Siege", "strength": 10, "ability": "Hero: Not affected by any Special Cards or abilities.", "source": "Won from Marquise Serenity during Gwent: Big City Players", 'count':1},
    49: {"name": "Nausicaa Cavalry Rider", "type": "Unit", "row": "Close Combat", "strength": 2, "ability": "Tight Bond: Place next to a card with the same name to double the strength of both cards.", "source": "1 purchased from Crow's Perch's quartermaster, 1 purchased from Crow's Perch's merchant or Devil's Pit's merchant, 1 purchased from Inn at the Crossroads's innkeep or Lindenvale's innkeep", 'count':3},
    50: {"name": "Puttkammer", "type": "Unit", "row": "Ranged Combat", "strength": 3, "ability": "", "source": "Purchased from Claywich's merchant", 'count':1},
    51: {"name": "Rainfarn", "type": "Unit", "row": "Close Combat", "strength": 4, "ability": "", "source": "Purchased from Lindenvale's merchant", 'count':1},
    52: {"name": "Renuald aep Matsen", "type": "Unit", "row": "Ranged Combat", "strength": 5, "ability": "", "source": "Random reward from gwent players", 'count':1},
    53: {"name": "Rotten Mangonel", "type": "Unit", "row": "Siege", "strength": 3, "ability": "", "source": "Random reward from gwent players", 'count':1},
    54: {"name": "Shilard Fitz-Oesterlen", "type": "Unit", "row": "Close Combat", "strength": 7, "ability": "Spy: Place on your opponent's battlefield (counts towards your opponent's total) and draw 2 cards from your deck.", "source": "Random reward from gwent players", 'count':1},
    55: {"name": "Siege Engineer", "type": "Unit", "row": "Siege", "strength": 6, "ability": "", "source": "Purchased from Inn at the Crossroads's innkeep, Purchased from Lindenvale's innkeep", 'count':1},
    56: {"name": "Siege Technician", "type": "Unit", "row": "Siege", "strength": 0, "ability": "Medic: Choose one card from your discard pile and play it instantly (no Heroes or Special Cards).", "source": "Purchased from The Golden Sturgeon's innkeep, Hearts of Stone expansion: 1 can be purchased from the merchant at the circus camp near Carsten", 'count':1},
    57: {"name": "Stefan Skellen", "type": "Unit", "row": "Close Combat", "strength": 9, "ability": "Spy: Place on your opponent's battlefield (counts towards opponent's total) and draw 2 cards from your deck.", "source": "Random reward from gwent players", 'count':1},
    58: {"name": "Sweers", "type": "Unit", "row": "Ranged Combat", "strength": 2, "ability": "", "source": "Purchased from Claywich's merchant", 'count':1},
    59: {"name": "Tibor Eggebracht", "type": "Hero", "row": "Ranged Combat", "strength": 10, "ability": "Hero: Not affected by any Special Cards or abilities.", "source": "Olivier during Gwent: Playing Innkeeps", 'count':1},
    60: {"name": "Vanhemar", "type": "Unit", "row": "Ranged Combat", "strength": 4, "ability": "", "source": "Random reward from gwent players", 'count':1},
    61: {"name": "Vattier de Rideaux", "type": "Unit", "row": "Close Combat", "strength": 4, "ability": "Spy: Place on your opponent's battlefield (counts towards opponent's total) and draw 2 cards from your deck.", "source": "Random reward from gwent players", 'count':1},
    62: {"name": "Vreemde", "type": "Unit", "row": "Close Combat", "strength": 2, "ability": "", "source": "Random reward from gwent players", 'count':1},
    63: {"name": "Young Emissary", "type": "Unit", "row": "Close Combat", "strength": 5, "ability": "Tight Bond: Place next to a card with the same name to double the strength of both cards.", "source": "1 purchased from Cunny of the Goose's innkeep, 1 purchased from Seven Cats Inn's innkeep", 'count':2},
    64: {"name": "Zerrikanian Fire Scorpion", "type": "Unit", "row": "Siege", "strength": 5, "ability": "", "source": "Purchase from Crow's Perch's merchant or Devil's Pit's merchant", 'count':1}
}

gwent_cards_monsters = {
    65: {"name": "Arachas", "type": "Unit", "row": "Close Combat", "strength": 4, "ability": "Muster: Find any cards with the same name in your deck and play them instantly.", "source": "1 purchased from Arinbjorn's innkeep, 1 purchased from Urialla Harbor's innkeep, 1 purchased from Svorlag's innkeep", "count": 3},
    66: {"name": "Arachas Behemoth", "type": "Unit", "row": "Siege", "strength": 6, "ability": "Muster: Find any cards with the same name in your deck and play them instantly.", "source": "Random reward from gwent players", "count": 1},
    67: {"name": "Botchling", "type": "Unit", "row": "Close Combat", "strength": 4, "ability": "", "source": "Purchased from Jonas at The New Port", "count": 1},
    68: {"name": "Celaeno Harpy", "type": "Unit", "row": "Agile", "strength": 2, "ability": "Agile: Can be placed in either the Close Combat or the Ranged Combat row. Cannot be moved once placed.", "source": "Random reward from gwent players", "count": 1},
    69: {"name": "Cockatrice", "type": "Unit", "row": "Ranged Combat", "strength": 2, "ability": "", "source": "Random reward from gwent players", "count": 1},
    70: {"name": "Crone: Brewess", "type": "Unit", "row": "Close Combat", "strength": 6, "ability": "Muster: Find any cards with the same name in your deck and play them instantly.", "source": "Random reward from gwent players", "count": 1},
    71: {"name": "Crone: Weavess", "type": "Unit", "row": "Close Combat", "strength": 6, "ability": "Muster: Find any cards with the same name in your deck and play them instantly.", "source": "Won from the Old Sage during Gwent: Velen Players", "count": 1},
    72: {"name": "Crone: Whispess", "type": "Unit", "row": "Close Combat", "strength": 6, "ability": "Muster: Find any cards with the same name in your deck and play them instantly.", "source": "Purchased from Arinbjorn's innkeep", "count": 1},
    73: {"name": "Draug", "type": "Hero", "row": "Close Combat", "strength": 10, "ability": "Hero: Not affected by any Special Cards or abilities.", "source": "Won from Crach an Craite during Gwent: Skellige Style", "count": 1},
    74: {"name": "Earth Elemental", "type": "Unit", "row": "Siege", "strength": 6, "ability": "", "source": "Purchased from Jonas at The New Port", "count": 1},
    75: {"name": "Endrega", "type": "Unit", "row": "Ranged Combat", "strength": 2, "ability": "", "source": "Random reward from gwent players", "count": 1},
    76: {"name": "Eredin Bréacc Glas: The Treacherous", "type": "leader", "row": "", "strength": "", "ability": "Doubles the strength of all spy cards (affects both players).", "source": "Purchase from Dulla kh'Amanni in Upper Mill", "count": 1},
    77: {"name": "Eredin: Bringer of Death", "type": "leader", "row": "", "strength": "", "ability": "Restore a card from your discard pile to your hand.", "source": "Won from Count Tybalt during High Stakes", "count": 1},
    78: {"name": "Eredin: Commander of the Red Riders", "type": "leader", "row": "", "strength": "", "ability": "Double the strength of all your Close Combat units (unless a Commander's horn is also present on that row).", "source": "Purchased from Jonas at The New Port", "count": 1},
    79: {"name": "Eredin: Destroyer of Worlds", "type": "leader", "row": "", "strength": "", "ability": "Discard 2 card and draw 1 card of your choice from your deck.", "source": "Won during Gwent: Velen Players", "count": 1},
    80: {"name": "Eredin: King of the Wild Hunt", "type": "leader", "row": "", "strength": "", "ability": "Pick any weather card from your deck and play it instantly.", "source": "Part of the base deck", "count": 1},
    81: {"name": "Fiend", "type": "Unit", "row": "Close Combat", "strength": 6, "ability": "", "source": "Purchased from Arinbjorn's innkeep", "count": 1},
    82: {"name": "Fire Elemental", "type": "Unit", "row": "Siege", "strength": 6, "ability": "", "source": "Random reward from gwent players, Possible loot in house at Hindar", "count": 1},
    83: {"name": "Foglet", "type": "Unit", "row": "Close Combat", "strength": 2, "ability": "", "source": "Purchased from Svorlag's innkeep", "count": 1},
    84: {"name": "Forktail", "type": "Unit", "row": "Close Combat", "strength": 5, "ability": "", "source": "Random reward from gwent players", "count": 1},
    85: {"name": "Frightener", "type": "Unit", "row": "Close Combat", "strength": 5, "ability": "", "source": "Random reward from gwent players", "count": 1},
    86: {"name": "Gargoyle", "type": "Unit", "row": "Ranged Combat", "strength": 2, "ability": "", "source": "Random reward from gwent players", "count": 1},
    87: {"name": "Ghoul", "type": "Unit", "row": "Close Combat", "strength": 1, "ability": "Muster: Find any cards with the same name in your deck and play them instantly.", "source": "2 are random rewards from gwent players, 1 purchased from Harviken's innkeep", "count": 3},
    88: {"name": "Grave Hag", "type": "Unit", "row": "Ranged Combat", "strength": 5, "ability": "", "source": "Random reward from gwent players", "count": 1},
    89: {"name": "Griffin", "type": "Unit", "row": "Close Combat", "strength": 5, "ability": "", "source": "Random reward from gwent players", "count": 1},
    90: {"name": "Harpy", "type": "Unit", "row": "Agile", "strength": 2, "ability": "Agile: Can be placed in either the Close Combat or the Ranged Combat row. Cannot be moved once placed.", "source": "Purchased from Harviken's innkeep", "count": 1},
    91: {"name": "Ice Giant", "type": "Unit", "row": "Siege", "strength": 5, "ability": "", "source": "Purchased from Svorlag's innkeep", "count": 1},
    92: {"name": "Imlerith", "type": "Hero", "row": "Close Combat", "strength": 10, "ability": "Hero: Not affected by any Special Cards or abilities.", "source": "Random reward from gwent players", "count": 1},
    93: {"name": "Kayran", "type": "Hero", "row": "Agile", "strength": 8, "ability": "Hero: Not affected by any Special Cards or abilities. Morale boost: Adds +1 to all units in the row (excluding itself). Agile: Can be placed in either the Close Combat or the Ranged Combat row. Cannot be moved once placed.", "source": "Random reward from gwent players", "count": 1},
    94: {"name": "Leshen", "type": "Hero", "row": "Ranged Combat", "strength": 10, "ability": "Hero: Not affected by any Special Cards or abilities.", "source": "Won from Ermion during Gwent: Skellige Style", "count": 1},
    95: {"name": "Nekker", "type": "Unit", "row": "Close Combat", "strength": 2, "ability": "Muster: Find any cards with the same name in your deck and play them instantly.", "source": "1 obtained during Following the Thread off Hammond's corpse, 1 purchased from Harviken's innkeep, 1 as random reward from gwent players", "count": 3},
    96: {"name": "Plague Maiden", "type": "Unit", "row": "Close Combat", "strength": 5, "ability": "", "source": "Random reward from gwent players", "count": 1},
    97: {"name": "Toad", "type": "Unit", "row": "Ranged Combat", "strength": 7, "ability": "Scorch - Ranged: Destroy your enemy's strongest Ranged Combat unit(s) if the combined strength of all his or her Ranged Combat units is 10 or more.", "source": "Won from Olgierd von Everec", "count": 1},
    98: {"name": "Vampire: Bruxa", "type": "Unit", "row": "Close Combat", "strength": 4, "ability": "Muster: Find any cards with the same name in your deck and play them instantly", "source": "Won during A Matter of Life and Death, Blood and Wine expansion: Rewarded for removing Louis' urn in Till Death Do You Part", "count": 2},
    99: {"name": "Vampire: Ekimmara", "type": "Unit", "row": "Close Combat", "strength": 4, "ability": "Muster: Find any cards with the same name in your deck and play them instantly", "source": "Purchased from Svorlag's innkeep", "count": 1},
    100: {"name": "Vampire: Fleder", "type": "Unit", "row": "Close Combat", "strength": 4, "ability": "Muster: Find any cards with the same name in your deck and play them instantly", "source": "Purchased from Harviken's innkeep", "count": 1},
    101: {"name": "Vampire: Garkain", "type": "Unit", "row": "Close Combat", "strength": 4, "ability": "Muster: Find any cards with the same name in your deck and play them instantly", "source": "Random reward from gwent players", "count": 1},
    102: {"name": "Vampire: Katakan", "type": "Unit", "row": "Close Combat", "strength": 5, "ability": "Muster: Find any cards with the same name in your deck and play them instantly.", "source": "Madman Lugos during Gwent: Skellige Style", "count": 1},
    103: {"name": "Werewolf", "type": "Unit", "row": "Close Combat", "strength": 5, "ability": "", "source": "Purchased from Urialla Harbor's innkeep", "count": 1},
    104: {"name": "Wyvern", "type": "Unit", "row": "Ranged Combat", "strength": 2, "ability": "", "source": "Random reward from gwent players", "count": 1}
}

gwent_cards_skot = {
    105: {"name": "Barclay Els", "type": "Unit", "row": "Agile", "strength": 6, "ability": "Agile: Can be placed in either the Close Combat or the Ranged Combat row. Cannot be moved once placed.", "source": "Purchased from the innkeep of The Golden Sturgeon in Novigrad Hearts of Stone expansion: 1 can be purchased from the merchant at the circus camp near Carsten Blood and Wine expansion: A possible reward during Till Death Do You Part", "count": 3},
    106: {"name": "Ciaran aep Easnillien", "type": "Unit", "row": "Agile", "strength": 3, "ability": "Agile: Can be placed in either the Close Combat or the Ranged Combat row. Cannot be moved once placed.", "source": "Random reward from gwent players", "count": 1},
    107: {"name": "Dennis Cranmer", "type": "Unit", "row": "Close Combat", "strength": 6, "ability": "", "source": "Random reward from gwent players", "count": 1},
    108: {"name": "Dol Blathanna Archer", "type": "Unit", "row": "Ranged Combat", "strength": 4, "ability": "", "source": "Purchase from Marquise Serenity at the Passiflora Hearts of Stone expansion: Purchase from merchant at the circus camp near Carsten Blood and Wine expansion: Purchase from Hugo Monnart or any innkeeper in Toussaint", "count": 3},
    109: {"name": "Dol Blathanna Scout", "type": "Unit", "row": "Agile", "strength": 6, "ability": "Agile: Can be placed in either the Close Combat or the Ranged Combat row. Cannot be moved once placed.", "source": "1 purchased from The Golden Sturgeon's Innkeep 2 are random rewards from gwent players Hearts of Stone expansion: 1 can be purchased from the merchant at the circus camp near Carsten", "count": 4},
    110: {"name": "Dwarven Skirmisher", "type": "Unit", "row": "Close Combat", "strength": 3, "ability": "Muster: Find any cards with the same name in your deck and play them instantly.", "source": "1 purchased from Stjepan at The Alchemy 2 are random rewards from gwent players", "count": 3},
    111: {"name": "Eithné", "type": "Hero", "row": "Ranged Combat", "strength": 10, "ability": "Hero: Not affected by any Special Cards or abilities.", "source": "Won from Zoltan during Gwent: Old Pals", "count": 1},
    112: {"name": "Elven Skirmisher", "type": "Unit", "row": "Ranged Combat", "strength": 2, "ability": "Muster: Find any cards with the same name in your deck and play them instantly.", "source": "1 purchased from Urialla Harbor's Innkeep 2 are random rewards from gwent players", "count": 3},
    113: {"name": "Filavandrel aen Fidhail", "type": "Unit", "row": "Agile", "strength": 6, "ability": "Agile: Can be placed in either the Close Combat or the Ranged Combat row. Cannot be moved once placed.", "source": "Random reward from gwent players", "count": 1},
    114: {"name": "Francesca Findabair: Daisy of the Valley", "type": "leader", "row": "", "strength":  "", "ability": "Daisy of the Valley: Draw an extra card at the beginning of the battle.", "source": "Purchased from Cunny of the Goose's Innkeep", "count": 1},
    115: {"name": "Francesca Findabair: Hope of the Aen Seidhe", "type": "leader", "row": "", "strength":  "", "ability": "Hope of the Aen Seidhe: Move agile units to whichever valid row maximizes their strength (don't move units already in optimal row).", "source": "Purchase from Dulla kh'Amanni at Upper Mill", "count": 1},
    116: {"name": "Francesca Findabair: Pureblood Elf", "type": "leader", "row": "", "strength":  "", "ability": "Pureblood Elf: Pick a Biting Frost card from your deck and play it instantly.", "source": "Part of the base deck", "count": 1},
    117: {"name": "Francesca Findabair: Queen of Dol Blathanna", "type": "leader", "row": "", "strength":  "", "ability": "Queen of Dol Blathanna: Destroy your enemy's strongest Close Combat unit(s) if the combined strength of all his or her Close Combat units is 10 or more.", "source": "Won from Finneas during High Stakes", "count": 1},
    118: {"name": "Francesca Findabair: The Beautiful", "type": "leader", "row": "", "strength":  "", "ability": "The Beautiful: Doubles the strength of all your Ranged Combat units (unless a Commander's Horn is also present on that row).", "source": "Won during Gwent: Big City Players", "count": 1},
    119: {"name": "Havekar Healer", "type": "Unit", "row": "Ranged Combat", "strength": 0, "ability": "Medic: Choose one card from your discard pile and play it instantly (no Heroes or Special Cards).", "source": "1 purchased from The Kingfisher Inn's Innkeep 1 purchased from the Cunny of the Goose's Innkeep 1 is a random reward from gwent players Hearts of Stone expansion: 1 can be purchased from the merchant at the circus camp near Carsten", "count": 4},
    120: {"name": "Havekar Smuggler", "type": "Unit", "row": "Close Combat", "strength": 5, "ability": "Muster: Find any cards with the same name in your deck and play them instantly.", "source": "1 purchased from The Kingfisher Inn's Innkeep 1 purchased from the Seven Cats Inn's Innkeep 1 is a random reward from gwent players Hearts of Stone expansion: 1 can be purchased from the merchant at the circus camp near Carsten", "count": 4},
    121: {"name": "Ida Emean aep Sivney", "type": "Unit", "row": "Ranged Combat", "strength": 6, "ability": "", "source": "Random reward from gwent players", "count": 1},
    122: {"name": "Iorveth", "type": "Hero", "row": "Ranged Combat", "strength": 10, "ability": "Hero: Not affected by any Special Cards or abilities.", "source": "Reward for completing Shock Therapy", "count": 1},
    123: {"name": "Isengrim Faoiltiarna", "type": "Hero", "row": "Close Combat", "strength": 10, "ability": "Morale boost: Adds +1 to all units in the row (excluding itself). Hero: Not affected by any Special Cards or abilities.", "source": "A Dangerous Game or Prison Warden during The Great Escape", "count": 1},
    124: {"name": "Mahakaman Defender", "type": "Unit", "row": "Close Combat", "strength": 5, "ability": "", "source": "1 purchased from The Kingfisher Inn's Innkeep 1 purchased from the Seven Cats Inn's Innkeep 1 purchased from The Golden Sturgeon's Innkeep 1 purchased from Marquise Serenity at the Passiflora 1 purchased from Stjepan at The Alchemy Hearts of Stone expansion: 3 can be purchased from the merchant at the circus camp near Carsten", "count": 8},
    125: {"name": "Milva", "type": "Unit", "row": "Ranged Combat", "strength": 10, "ability": "Morale boost: Adds +1 to all units in the row (excluding itself).", "source": "Won during A Matter of Life and Death", "count": 1},
    126: {"name": "Riordain", "type": "Unit", "row": "Ranged Combat", "strength": 1, "ability": "", "source": "Random reward from gwent players", "count": 1},
    127: {"name": "Saesenthessis", "type": "Hero", "row": "Ranged Combat", "strength": 10, "ability": "Hero: Not affected by any Special Cards or abilities.", "source": "Vernon Roche during Gwent: Old Pals", "count": 1},
    128: {"name": "Schirrú", "type": "Unit", "row": "Siege", "strength": 8, "ability": "Scorch - Siege: Destroys your enemy's strongest Siege Combat unit(s) if the combined strength of all his or her Siege Combat units is 10 or more.", "source": "Won from the merchant at the circus northwest of Carsten", "count": 1},
    129: {"name": "Toruviel", "type": "Unit", "row": "Ranged Combat", "strength": 2, "ability": "", "source": "Random reward from gwent players", "count": 1},
    130: {"name": "Vrihedd Brigade Recruit", "type": "Unit", "row": "Ranged Combat", "strength": 4, "ability": "", "source": "Random reward from gwent players", "count": 1},
    131: {"name": "Vrihedd Brigade Veteran", "type": "Unit", "row": "Agile", "strength": 5, "ability": "Agile: Can be placed in either the Close Combat or the Ranged Combat row. Cannot be moved once placed.", "source": "1 purchased from Stjepan at The Alchemy 1 purchased from The Kingfisher Inn's Innkeep Hearts of Stone expansion: 1 can be purchased from the merchant at the circus camp near Carsten", "count": 3},
    132: {"name": "Yaevinn", "type": "Unit", "row": "Agile", "strength": 6, "ability": "Agile: Can be placed in either the Close Combat or the Ranged Combat row. Cannot be moved once placed.", "source": "Won from Sjusta during Gwent: Skellige Style", "count": 1}
}

gwent_cards_neutral = {
    133: {"name": "Biting Frost", "type": "Weather", "row": "", "strength": 0, "ability": "Sets the strength of all Close Combat cards to 1 for both players", "source": "2 are part of the base deck, 1 is a random reward from gwent players", "count": 3},
    134: {"name": "Bovine Defense Force", "type": "Unit", "row": "Close Combat", "strength": 8, "ability": "Summoned by the removal of the Cow card during play", "source": "Summoned by the removal of the Cow card during play", "count": 1},
    135: {"name": "Cirilla Fiona Elen Riannon", "type": "Hero", "row": "Close Combat", "strength": 15, "ability": "Hero: Not affected by any Special Cards or abilities. Muster: Find the Roach card in your deck and play it instantly", "source": "Won from the Scoia'tael merchant during Gwent: Big City Players", "count": 1},
    136: {"name": "Clear Weather", "type": "Weather", "row": "", "strength": 0, "ability": "Removes all Weather Card (Biting Frost, Impenetrable Fog and Torrential Rain) effects", "source": "2 are part of the base deck, 1 is a random reward from gwent players", "count": 3},
    137: {"name": "Commander's Horn", "type": "Special", "row": "", "strength": 0, "ability": "Doubles the strength of all unit cards in that row. Limited to 1 per row", "source": "Purchase from various innkeeps and merchants", "count": 1},
    138: {"name": "Cow", "type": "Unit", "row": "Ranged Combat", "strength": 0, "ability": "When this card is removed from the battlefield, it summons a powerful new Unit Card to take its place", "source": "Found inside a barn in Brunwich", "count": 1},
    139: {"name": "Dandelion", "type": "Unit", "row": "Close Combat", "strength": 2, "ability": "Commander's Horn: Doubles the strength of all unit cards in that row. Limited to 1 per row", "source": "Won during A Matter of Life and Death", "count": 1},
    140: {"name": "Decoy", "type": "Special", "row": "", "strength": 0, "ability": "Swap with a card on the battlefield to return it to your hand", "source": "Purchase from various merchants", "count": 1},
    141: {"name": "Emiel Regis Rohellec Terzieff", "type": "Unit", "row": "Close Combat", "strength": 5, "ability": "", "source": "Random reward from gwent players", "count": 1},
    142: {"name": "Gaunter O'Dimm", "type": "Unit", "row": "Siege", "strength": 2, "ability": "Muster: Find any cards with the same name in your deck and play them instantly", "source": "Won from Robert Hilbert during Open Sesame!", "count": 1},
    143: {"name": "Gaunter O'Dimm: Darkness", "type": "Unit", "row": "Ranged Combat", "strength": 4, "ability": "Muster: Find any cards with the same name in your deck and play them instantly", "source": "1 purchased from Dulla kh'Amanni at Upper Mill, 2 purchased from the merchant at the circus camp near Carsten", "count": 3},
    144: {"name": "Geralt of Rivia", "type": "Hero", "row": "Close Combat", "strength": 15, "ability": "Hero: Not affected by any Special Cards or abilities. Muster: Find the Roach card in your deck and play it instantly", "source": "Thaler during Gwent: Old Pals or Gwent: Playing Thaler", "count": 1},
    145: {"name": "Impenetrable Fog", "type": "Weather", "row": "", "strength": 0, "ability": "Sets the strength of all Ranged Combat cards to 1 for both players", "source": "2 are part of the base deck, 1 is a random reward from gwent players", "count": 3},
    146: {"name": "Mysterious Elf", "type": "Hero", "row": "Close Combat", "strength": 0, "ability": "Spy: Place on your opponent's battlefield and draw 2 cards from your deck. Hero: Not affected by any Special Cards or abilities", "source": "Won from Gremist during Gwent: Skellige Style", "count": 1},
    147: {"name": "Olgierd von Everec", "type": "Unit", "row": "Agile", "strength": 6, "ability": "Morale boost: Adds +1 to all units in the row (excluding itself). Agile: Can be placed in either Close Combat or Ranged Combat row", "source": "Won from Shani", "count": 1},
    148: {"name": "Roach", "type": "Unit", "row": "Close Combat", "strength": 3, "ability": "", "source": "Reward for playing Gwent: The Witcher Card Game", "count": 1},
    149: {"name": "Scorch", "type": "Special", "row": "", "strength": 0, "ability": "Scorch: Discards after playing. Kills the strongest card(s) on the battlefield", "source": "Purchase from various innkeeps", "count": 1},
    150: {"name": "Skellige Storm", "type": "Weather", "row": "", "strength": 0, "ability": "Reduces the Strength of all Range and Siege Units to 1", "source": "1 from Tourney Grounds' armorer, 1 from Tourney Grounds' barber, 1 from Beauclair Port's butcher", "count": 3},
    151: {"name": "Torrential Rain", "type": "Weather", "row": "", "strength": 0, "ability": "Sets the strength of all Siege Combat cards to 1 for both players", "source": "2 are part of the base deck, 1 is random rewards from gwent players", "count": 3},
    152: {"name": "Triss Merigold", "type": "Hero", "row": "Close Combat", "strength": 7, "ability": "Hero: Not affected by any Special Cards or abilities", "source": "Lambert during Gwent: Old Pals", "count": 1},
    153: {"name": "Vesemir", "type": "Unit", "row": "Close Combat", "strength": 6, "ability": "", "source": "Won from Vimme Vivaldi during Gwent: Big City Players", "count": 1},
    154: {"name": "Villentretenmerth", "type": "Unit", "row": "Close Combat", "strength": 7, "ability": "Scorch - Close Combat: Destroy your enemy's strongest Close Combat unit(s) if the combined strength of all his or her Close Combat units is 10 or more", "source": "Random reward from gwent players", "count": 1},
    155: {"name": "Yennefer of Vengerberg", "type": "Hero", "row": "Ranged Combat", "strength": 7, "ability": "Medic: Choose one card from your discard pile and play it instantly (no Heroes or Special Cards). Hero: Not affected by any Special Cards or abilities", "source": "Won from Stjepan during Gwent: Playing Innkeeps", "count": 1},
    156: {"name": "Zoltan Chivay", "type": "Unit", "row": "Close Combat", "strength": 5, "ability": "", "source": "Won from Aldert Geert in White Orchard or found under the Hanged Man's Tree", "count": 1}
}



def check_amount_of_cards():
    sm = 0
    # gwent_cards_north
    # gwent_cards_nilfgaard
    # gwent_cards_monsters
    for dct in gwent_cards_north:
        sm += gwent_cards_north[dct]['count']
    for dct in gwent_cards_nilfgaard:
        sm += gwent_cards_nilfgaard[dct]['count']
    for dct in gwent_cards_monsters:
        sm += gwent_cards_monsters[dct]['count']
    for dct in gwent_cards_skot:
        sm += gwent_cards_skot[dct]['count']
    for dct in gwent_cards_neutral:
        sm += gwent_cards_neutral[dct]['count']
    print(sm)
    return sm


def row_to_line_type(s):
    if s == 'Agile':
        return 1
    elif s == 'Close Combat':
        return 1
    elif s == 'Ranged Combat':
        return 2
    else:
        return 3


def strength_to_int(s):
    if s == '':
        return 0
    else:
        return int(s)


def ability_to_flag(s):
    if s == '':
        return 0
    else:
        return 1



def get_cards_data_by_dct(dct):
    ids, powers, line_types, abilities_flags = np.array([]), np.array([]), np.array([]), np.array([])
    dtype = np.int64
    for id in dct:
        ids = np.concatenate((ids, np.array([id]*dct[id]['count'], dtype=dtype)))
        powers = np.concatenate((powers, np.array([strength_to_int(dct[id]['strength'])]*dct[id]['count'], dtype=dtype)))
        line_types = np.concatenate((line_types, np.array([row_to_line_type(dct[id]['row'])]*dct[id]['count'], dtype=dtype)))
        abilities_flags = np.concatenate((abilities_flags, np.array([ability_to_flag(dct[id]['row'])]*dct[id]['count'], dtype=dtype)))
    return ids, powers, line_types

# ids, powers, line_types = get_cards_data_by_dct(gwent_cards_skot)
# print(ids)
# print(powers)
# print(line_types)