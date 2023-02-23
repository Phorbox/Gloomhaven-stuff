import json
INPUTJSON = f"json\\class2.json"
BASEDECKJSON = f"json\\baseDeck.json"
outputJson = f"json\\classBaseDecks.json"


def makeDecks():
    inson = open(INPUTJSON)
    classes = json.load(inson)
    bason = open(BASEDECKJSON)
    basedeck = json.load(bason)
    returner = []
    for character in classes:
        currentDeck = basedeck.copy()
        for perk in character["perks"]:
            for effect in perk:
                effectAmount = effects(effect)
                if not effectAmount:
                    continue
                cards = perk[effect]
                for card in cards:
                    if card in currentDeck:
                        currentDeck[card] = effectAmount * \
                            cards[card] + currentDeck[card]
                    else:
                        currentDeck[card] = effectAmount * cards[card]
        popList = []
        for types in currentDeck:
            if currentDeck[types] == 0:
                popList.append(types)
        for types in popList:
            currentDeck.pop(types)
        currentDeck = sortDict(currentDeck)
        returner.append({"name": character["name"], "deck": currentDeck},)
    return returner


def effects(op):
    match op:
        case "add":
            return 1
        case "remove":
            return -1
        case "else":
            return 0
        case _:
            return False


def writeJson(name, dict):
    dicter = json.dumps(dict, indent=2)
    perkyFile = open(name, "w")
    perkyFile.write(dicter)
    perkyFile.close()


def sortDict(myDict):
    myKeys = list(myDict.keys())
    myKeys.sort(reverse=True, key=sorterFunc)
    return {i: myDict[i] for i in myKeys}


def sorterFunc(e):
    if e[slice(2)] == "*0":
        return -99
    val1 = e[0]
    counter = 0
    match val1:
        case "*":
            counter += 999 * int(e[1])
        case "-":
            counter += -1 * int(e[1]) * 10
        case "+":
            counter += 1 * int(e[1]) * 10
        case _:
            return False
    if "rolling" in e:
        counter += -999
    counter += len(e) - 3
    return counter


jsoner = makeDecks()
writeJson(outputJson, jsoner)
