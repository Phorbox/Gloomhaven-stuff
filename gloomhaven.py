import random,re,time,math,json
SCENARIOLENGTH = 20
BASEDECKPATH = "json\\baseDeck.json"
# testnumber is set to the amount of tests my laptop can run in one second
TESTNUMBER = 12500
CLASSPATH = f"json\\class.json"


def makeBaseDeck():
    deckFile = open(BASEDECKPATH)
    decktionary = json.load(deckFile)
    decker = makeDeck(decktionary)
    deckFile.close()
    return decker

def makeDeck(decktionary):
    decker = []
    for typer in decktionary:
        for i in range(0,decktionary[f"{typer}"]):
            decker.append(typer)
    # print(f"deck Size : {len(decker)} contents:{decker}")
    return decker


baseDeck = makeBaseDeck()

def rollAttack(Damage, deck,discard):
    card = drawCard(deck,discard)
    rolls = 0
    while isRolling(card):
        # print(f"Rolling:\t{card}")
        operation = card[0]
        value = int(card[1])
        Damage = calculator(Damage,value,operation)
        card = drawCard(deck,discard)
        rolls+=1
    
    operation = card[0]
    value = int(card[1])
    return calculator(Damage,value,operation)

def drawCard(deck,discard):
    cardI = random.randint(0,len(deck)-1)
    returner = deck[cardI]
    discard.append(deck.pop(cardI))
    return(returner)

def calculator(a,b,op):
    match op:
        case "+":
            return a + b
        case "-":
            return a - b    
        case "*":
            return a * b
        case _:
            return a

def sumArray(arry):
    returner = 0
    for each in arry:
        returner += each
    return returner

def avgArray(arry):
    return round(sumArray(arry) / len(arry),2)

def runScenario(deck,nAttacks,baseDamage):
    # print(f"deck:    {testDecker}")
    damageRolls = 0
    discardPile = []
    for i in range(0,nAttacks):
        damageRolls+=(rollAttack(baseDamage,deck,discardPile))
        shuffle(deck, discardPile)
    # print(f"discard: {len(discard)}")
    return damageRolls / nAttacks

def shuffle(deck, discard):
    if isShuffle(discard):
        for i in range(0,len(discard)):
            deck.append(discard.pop(0))      

def isShuffle(discard):
   r = re.compile(".*shuffle")
   return  (len(list(filter(r.match,discard))) > 0)

def isRolling(card):
    return  (re.search(".*rolling",card) != None)

def runTest(nTests):
    testDecker = baseDeck
    results = 0
    for i in range(0,nTests):
       results+= runScenario(testDecker,SCENARIOLENGTH,3)

    return results / nTests

def loadClasses(classJson):
    classFile = open(classJson)
    classDict = json.load(classFile)
    classFile.close()
    return classDict

# def loopClasses(bigDict):
#     for anyClass, perkList in bigDict.items():
#         for perkEffect in perkList:
#             currentDeck = makeDeck(each)


print(f"---Test  :\tBase Deck\t---")
start_time = time.time()
avger = round(runTest(TESTNUMBER),2)
print(f"---Average:\t{avger}\t---")
print(f"---Time   :\t{round((time.time() - start_time),3)}s\t---\n")

# classDict = loadClasses(CLASSPATH)
# loopClasses(classDict)


