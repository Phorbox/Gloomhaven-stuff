import json
jsonFileName = f"json\\baseDeck.json"
csvFileName = f"csv\\baseDeck"


def loopFileRead(name):
    perkyFile = open(name,"r")
    bigDict = {}
    for each in perkyFile:
        id = each.strip()
        # print (each)
        print(f"adding {id}\n")
        if f"{id}" in bigDict :
            bigDict[f"{id}"] = (int(bigDict[f"{id}"]) + 1)
        else:
            bigDict[f"{id}"] = 1
    perkyFile.close()
    return bigDict


def writeJson(name,dict):
    perkyFile = open(name,"w")
    perkyFile.write(dict)
    perkyFile.close()


jsoner = loopFileRead(csvFileName)
jsoner = json.dumps(jsoner,indent=4)
# print(jsoner)
writeJson(jsonFileName,jsoner)
