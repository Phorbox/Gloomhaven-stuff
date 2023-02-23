
import json
jsonFileName = f"json\\perks.json"
csvFileName = f"csv\\perks.csv"


def loopFileRead(name):
    perkyFile = open(name,"r")
    bigDict = {}
    id = 1
    for each in perkyFile:
        print(f"line {id}\t", end = '')
        bigDict[id] = constructPerk(each)
        id+=1
    perkyFile.close()
    return bigDict

def constructPerk(line):
    splitter = line.split(",")
    # get adds
    dicter = {"name" : line.strip()}
    adder,remover,elser = {},{},{}
    for each in splitter:
        
        secondSplit = each.split(" ")
        switcher = secondSplit.pop(0)
        quantity = int(secondSplit.pop(0))
        
        card = lineToCard(secondSplit)
        tempy = [card] * quantity
        match switcher:
            case "add":
                if card in adder:
                    adder[card] = (int(adder[card]) + quantity)
                else:
                    adder[card] = quantity
                
            case "remove":
                if card in remover:
                    remover[card] = (int(remover[card]) + quantity)
                else:
                    remover[card] = quantity
            case "else":
                if card in elser:
                    elser[card] = (int(elser[card]) + quantity)
                else:
                    elser[card] = quantity
            case _:
                pass

    if len(adder) != 0:
        dicter["add"] = adder
    if len(remover) != 0:
        dicter["remove"] = remover
    if len(elser) != 0:
        dicter["else"] = elser
    print(dicter)
    return dicter

def lineToCard(line):
    stringer = ""
    for each in line:
        stringer = f"{stringer} {each}"
    return stringer.strip()

def writeJson(name,dict):
    perkyFile = open(name,"w")
    perkyFile.write(dict)
    perkyFile.close()


jsoner = loopFileRead(csvFileName)
jsoner = json.dumps(jsoner,indent=4)
# print(jsoner)
writeJson(jsonFileName,jsoner)
