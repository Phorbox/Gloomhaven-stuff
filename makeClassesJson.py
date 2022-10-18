# load perks json
# open class csv
# construct class json

import json
perksJson = f"json\\perks.json"
classCsv = f"csv\\class.csv"
jsonFileName = f"json\\class.json"


def loopFileRead(name):
    classyFile = open(name,"r")
    bigDict = {}
    perksFile = open(perksJson)
    perkDict = json.load(perksFile)
    for each in classyFile:
        each = each.strip()
        row = each.split(",")
        bigDict[row[0]] = constructClass(row,perkDict)
    classyFile.close()
    perksFile.close()
    return bigDict

def constructClass(splitRow,perkDict):
    perker = []
    for each in range(1,len(splitRow)):
        if splitRow[each] != "":
            for i in range(0,int(splitRow[each])):
                perker.append( perkDict[f"{each}"])
    return perker

def writeJson(name,dict):
    perkyFile = open(name,"w")
    perkyFile.write(dict)
    perkyFile.close()

jsoner = loopFileRead(classCsv)
jsoner = json.dumps(jsoner,indent=4)
# print(jsoner)
writeJson(jsonFileName,jsoner)