import json

classandperkCsv = f"csv\\classandperk.csv"
jsonFileName = f"json\\class2.json"


def loopFileRead(name):
    classFile = open(name, "r")
    header = classFile.readline()
    header = header.strip()
    classes = header.split(",")
    bigDict = []
    for field in classes:
        if (field != ""):
            bigDict.append({"name": field, "perks": []})

    for each in classFile:
        each = each.strip()
        row = each.split(",")

        perk = constructFunction(row[slice(2)])
        i = 0
        for eachers in row[slice(3, len(row))]:
            if eachers != "":
                for z in range(0, int(eachers)):
                    bigDict[i]["perks"].append(perk)
            i += 1

    classFile.close()
    return bigDict


def constructFunction(effectArray):
    if (effectArray[1] == ""):
        effectArray.pop(1)

    perk = {"name": ",".join(effectArray).rstrip(',')}
    for each in effectArray:
        things = each.split(" ")
        namea = things[0]
        amount = int(things[1])
        effect = " ".join(things[slice(3, len(things))])
        card = f"{things[2]} {effect}".strip()

        if namea not in perk:
            perk[namea] = {card: amount}
        else:
            perk[namea].update({card: amount})
    return perk


def writeJson(name, dict):
    dicter = json.dumps(dict, indent=2)
    perkyFile = open(name, "w")
    perkyFile.write(dicter)
    perkyFile.close()


jsoner = loopFileRead(classandperkCsv)
writeJson(jsonFileName, jsoner)
# print(jsoner[1])
