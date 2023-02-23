# load perks json
# open class csv
# construct class json

import json
perksJson = f"json\\perks.json"
classCsv = f"csv\\class.csv"
jsonFileName = f"json\\class.json"


def loopFileRead(name):
    classFile = open(name,"r")
    allClasses = {}
    perksFile = open(perksJson)
    perkDict = json.load(perksFile)
    for each in classFile:
        each = each.strip()
        row = each.split(",")
        allClasses[row[0]] = constructClass(row,perkDict)
    classFile.close()
    perksFile.close()
    return allClasses

def constructClass(splitRow,perkDict):
    perker = {}
    p = 1
    for each in range(1,len(splitRow)):

        if splitRow[each] != "":
            for i in range(0,int(splitRow[each])):
                perker[p] = ( perkDict[f"{each}"])
                p+=1
    return perker

def writeJson(name,dict):
    perkyFile = open(name,"w")
    perkyFile.write(dict)
    perkyFile.close()

jsoner = loopFileRead(classCsv)
jsoner = json.dumps(jsoner,indent=4)
# print(jsoner)
writeJson(jsonFileName,jsoner)