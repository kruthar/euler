__author__ = 'kruthar'
'''
Monopoly Odds
In the game, Monopoly, the standard board is set up in the following way:

GO	A1	CC1	A2	T1	R1	B1	CH1	B2	B3	JAIL
H2	 	                                C1
T2	 	                                U1
H1	 	                                C2
CH3	 	                                C3
R4	 	                                R2
G3	 	                                D1
CC3	 	                                CC2
G2	 	                                D2
G1	 	                                D3
G2J	F3	U2	F2	F1	R3	E3	E2	CH2	E1	FP

A player starts on the GO square and adds the scores on two 6-sided dice to determine the number of squares they advance
in a clockwise direction. Without any further rules we would expect to visit each square with equal probability: 2.5%.
However, landing on G2J (Go To Jail), CC (community chest), and CH (chance) changes this distribution.In addition to G2J,
and one card from each of CC and CH, that orders the player to go directly to jail, if a player rolls three consecutive
doubles, they do not advance the result of their 3rd roll. Instead they proceed directly to jail.At the beginning of the
game, the CC and CH cards are shuffled. When a player lands on CC or CH they take a card from the top of the respective
pile and, after following the instructions, it is returned to the bottom of the pile. There are sixteen cards in each
pile, but for the purpose of this problem we are only concerned with cards that order a movement; any instruction not
concerned with movement will be ignored and the player will remain on the CC/CH square.

Community Chest (2/16 cards):
    Advance to GO
    Go to JAIL
Chance (10/16 cards):
    Advance to GO
    Go to JAIL
    Go to C1
    Go to E3
    Go to H2
    Go to R1
    Go to next R (railway company)
    Go to next R
    Go to next U (utility company)
    Go back 3 squares.

The heart of this problem concerns the likelihood of visiting a particular square. That is, the probability of finishing
at that square after a roll. For this reason it should be clear that, with the exception of G2J for which the probability
of finishing on it is zero, the CH squares will have the lowest probabilities, as 5/8 request a movement to another square,
and it is the final square that the player finishes at on each roll that we are interested in. We shall make no distinction
between "Just Visiting" and being sent to JAIL, and we shall also ignore the rule about requiring a double to "get out of jail",
assuming that they pay to get out on their next turn.By starting at GO and numbering the squares sequentially from 00 to
39 we can concatenate these two-digit numbers to produce strings that correspond with sets of squares.Statistically it
can be shown that the three most popular squares, in order, are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO
(3.09%) = Square 00. So these three most popular squares can be listed with the six-digit modal string: 102400.If, instead
of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.
'''

from functions import *
import random

squareList = ['GO','A1','CC1','A2','T1','R1','B1','CH1','B2','B3','JAIL','C1','U1','C2',\
              'C3','R2','D1','CC2','D2','D3','FP','E1','CH2','E2','E3','R3','F1',\
              'F2','U2','F3','G2J','G1','G2','CC3','G3','R4','CH3','H1','T2','H2']
squareMap = {'GO':0,'A1':1,'CC1':2,'A2':3,'T1':4,'R1':5,'B1':6,'CH1':7,'B2':8,'B3':9,'JAIL':10,'C1':11,'U1':12,'C2':13,\
             'C3':14,'R2':15,'D1':16,'CC2':17,'D2':18,'D3':19,'FP':20,'E1':21,'CH2':22,'E2':23,'E3':24,'R3':25,'F1':26,\
             'F2':27,'U2':28,'F3':29,'G2J':30,'G1':31,'G2':32,'CC3':33,'G3':34,'R4':35,'CH3':36,'H1':37,'T2':38,'H2':39}
communityChest = ['GO', 'JAIL', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE',\
                  'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE']
chance = ['GO', 'JAIL', 'C1', 'E3', 'H2', 'R1', 'RX', 'RX', 'UX', 'B3', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE']

dice = 4
allowedDoubles = 3
outcomes = [0] * len(squareList)
cc = 0
ch = 0
square = 0
dubs = 0

def findNext(start, prefix):
    current = (start + 1) % len(squareList)
    while squareList[current][0:len(prefix)] != prefix:
        current = (current + 1) % len(squareList)
    return current

def takeCC():
    global cc
    cc += 1
    if cc >= len(communityChest):
        cc = 0
    return communityChest[cc]

def takeCH():
    global ch
    ch += 1
    if ch >= len(chance):
        ch = 0
    return chance[ch]

for go in range(1000000):
    d1 = random.randint(1, dice)
    d2 = random.randint(1, dice)

    landing = square + d1 + d2
    while landing >= len(squareList):
        landing -= len(squareList)

    if d1 == d2 and dubs >= allowedDoubles:
        square = squareMap['JAIL']
        dubs = 0
    else:
        isDub = False
        if d1 == d2:
            isDub = True
            dubs += 1
        else:
            dubs = 0

        if squareList[landing] == 'G2J':
            square = squareMap['JAIL']
            dubs = 0
        elif 'CC' in squareList[landing]:
            card = takeCC()
            if card == 'NONE':
                square = landing
            elif card == 'JAIL':
                dubs == 0
                square = squareMap['JAIL']
            else:
                square = squareMap[card]
        elif 'CH' in squareList[landing]:
            card = takeCH()
            if card == 'NONE':
                square = landing
            elif card == 'JAIL':
                dubs = 0
                square = squareMap['JAIL']
            elif card == 'RX':
                square = findNext(landing, 'R')
            elif card == 'UX':
                square = findNext(landing, 'U')
            elif card == 'B3':
                if squareList[landing] == 'CH1':
                    square = squareMap['T1']
                elif squareList[landing] == 'CH2':
                    square = squareMap['D3']
                elif squareList[landing] == 'CH3':
                    card = takeCC()
                    if card == 'NONE':
                        square = landing
                    elif card == 'JAIL':
                        dubs == 0
                        square = squareMap['JAIL']
                    else:
                        square = squareMap[card]
            else:
                square = squareMap[card]
        else:
            square = landing
    outcomes[square] += 1

total = float(sumList(outcomes))
for i, outcome in enumerate(outcomes):
    if outcome / total * 100 > 3:
        print squareList[i], ":", outcome / total * 100, "%"

'''

def addLists(a, b):
    result = [0] * len(a)
    for i in range(len(a)):
        result[i] += a[i] + b[i]
    return result

def rolldice(start, doubles):
    outcomes = [0] * len(squareList)
    for d1 in range(1, dice + 1):
        for d2 in range(1, dice + 1):
            dubs = doubles
            if d1 == d2:
                dubs += 1

            if dubs >= 3:
                outcomes[squareMap['JAIL']] += 1
            else:
                if d1 == d2:
                    temp = addLists(outcomes[:], getOutcomes(start + d1 + d2))
                    for i, outcome in enumerate(temp):
                        outcomes = addLists(outcomes[:], rolldice(i, dubs))
                else:
                    outcomes = addLists(outcomes[:], getOutcomes(start + d1 + d2))
    return outcomes

def getOutcomes(landing):
    outcomes = [0] * len(squareList)

    while landing >= len(squareList):
        landing -= len(squareList)

    outcomes[landing] += 1
    return outcomes


count = 0
result = rolldice(0, 0)

while count < 1:
    temp = [0] * len(squareList)
    for i, count in enumerate(result):
        temp = addLists(temp[:], rolldice(i, 0))
    result = addLists(result[:], temp[:])
    count += 1

total = float(sumList(result))
print [x / total for x in result]
'''

'''

def findNext(start, prefix):
    current = (start + 1) % len(squareList)
    while squareList[current][0:len(prefix)] != prefix:
        current = (current + 1) % len(squareList)
    return current

def addLists(a, b):
    result = [0] * len(a)
    for i in range(len(a)):
        result[i] += a[i] + b[i]
    return result

def rollDice(start, doubles):
    outcomes = [0] * len(squareList)

    for d1 in range(1, dice + 1):
        for d2 in range(1, dice + 1):
            # Reinstantiate a variable, so we can change and use it specifically for this dice outcome and not change it
            # for the rest of the dice outcomes
            dub = doubles
            if d1 == d2:
                dub += 1

            # If we hit the 3rd double then go straight to JAIL
            if dub >= 3:
                outcomes[squareMap['JAIL']] += 1
            # Otherwise, pass on the landing square and doubles to find the array of outcomes
            else:
                outcomes = addLists(outcomes[:], getOutcomes(start + d1 + d2, d1 == d2, dub)[:])
    return outcomes

def getOutcomes(landing, isdouble, doubles):
    outcomes = [0] * len(squareList)

    # If we have rounded the board, then reduce the landing number by the board size
    while landing >= len(squareList):
        landing -= len(squareList)

    space = squareList[landing]

    # If we landed on G2J, go to jail
    if space == 'G2J':
        outcomes[squareMap['JAIL']] += 1
    # If we landed on Community Chest we have some options depending on the card we choose
    elif space[0:2] == 'CC':
        # 1 Chance of moving to GO
        if isdouble:
            outcomes = addLists(outcomes[:], rollDice(squareMap['GO'], doubles))
        outcomes[squareMap['GO']] += 1

        # 1 Chance of going to JAIL
        outcomes[squareMap['JAIL']] += 1

        # 14 chances of staying put
        if isdouble:
            outcomes = addLists(outcomes[:], [x * 14 for x in rollDice(landing, doubles)])
        outcomes[landing] += 14
    # If we landed on Chance we have some options depending on the card we choose
    elif space[0:2] == 'CH':
        # 1 Chance of going to JAIL
        outcomes[squareMap['JAIL']] += 1

        # 5 Chances to go to another destination
        for s in ['GO','C1','E3','H2','R1']:
            if isdouble:
                outcomes = addLists(outcomes[:], rollDice(squareMap[s], doubles))
            outcomes[squareMap[s]] += 1

        # 2 Chances to go to the next Railroad
        # 1 Chance to go to the next Utility
        for p in ['R','R','U']:
            if isdouble:
                outcomes = addLists(outcomes[:], rollDice(findNext(landing, p), doubles))
            outcomes[findNext(landing, p)] += 1

        # 6 chances of staying put
        if isdouble:
            outcomes = addLists(outcomes[:], [x * 6 for x in rollDice(landing, doubles)])
        outcomes[landing] += 6

        # 1 Chance of moving backwards 3 steps
        outcomes = addLists(outcomes[:], getOutcomes(landing - 3, isdouble, doubles)[:])
    # All other spaces have no chance to redirect
    else:
        if isdouble:
            outcomes = addLists(outcomes[:], rollDice(landing, doubles))
        outcomes[landing] += 1

    return outcomes

results = [0] * len(squareList)
results[squareMap['GO']] = 1
limit = 100

for turn in range(limit):
    temp = [0] * len(squareList)
    for i, square in enumerate(results):
        if square > 0:
            temp = addLists(temp[:], [x * square for x in rollDice(i, 0)])
    total = float(sumList(temp))
    print temp[0] / total
    results = temp[:]

total = float(sumList(results))


for cell in range(len(results)):
    print squareList[cell] + ': ' + str(results[cell] / total)


results = [0] * len(squareList)

# calculate the odds for landing on spaces, using each possible square as the starting spot
for start in range(0, 40):
    results = addLists(results[:], rollDice(start, 0))

total = float(sumList(results))


for cell in range(len(results)):
    print squareList[cell] + ': ' + str(results[cell] / total)
'''
