import random,re,time
nTests = 6
damage = 3


def makeBaseDeck():
    deckFile = open("baseDeck","r")
    decker = []
    for each in deckFile:
        decker.append(each[:-1])
    deckFile.close()
    return decker

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

def testDeck(deck,rolls,damage):
    # print(f"deck:    {testDecker}")
    damager = []
    discard = []
    for i in range(0,rolls):
        damager.append(rollAttack(damage,deck,discard))
        shuffle(deck, discard)
    # print(f"discard: {len(discard)}")
    return avgArray(damager)

def shuffle(deck, discard):
    if isShuffle(discard):
        for i in range(0,len(discard)):
            deck.append(discard.pop(0))      

def isShuffle(discard):
   r = re.compile(".*shuffle")
   return  (len(list(filter(r.match,discard))) > 0)

def isRolling(card):
    return  (re.search(".*rolling",card) != None)



baseDeck = makeBaseDeck()
testDecker = baseDeck
tests = 10
for i in range(0,nTests):
    start_time = time.time()
    avger = testDeck(testDecker,tests,3)
    print(f"---Average: {avger}")
    print(f"---Time:    {round((time.time() - start_time),3)}s ---")
    tests *= 10

