__author__ = 'kruthar'
'''
Poker Hands
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

0 High Card: Highest value card.
1 One Pair: Two cards of the same value.
2 Two Pairs: Two different pairs.
3 Three of a Kind: Three cards of the same value.
4 Straight: All cards are consecutive values.
5 Flush: All cards of the same suit.
6 Full House: Three of a kind and a pair.
7 Four of a Kind: Four cards of the same value.
8 Straight Flush: All cards are consecutive values of same suit.
9 Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 	    Player 2	 	    Winner
1	 	    5H 5C 6S 7S KD      2C 3S 8S 8D TD      Player 2
            Pair of Fives       Pair of Eights

2	 	    5D 8C 9S JS AC      2C 5C 7D 8S QH      Player 1
            Highest card Ace    Highest card Queen

3	 	    2D 9C AS AH AC      3D 6D 7D TD QD      Player 2
            Three Aces          Flush with Diamonds

4	 	    4D 6S 9H QH QC      3D 6D 7H QD QS      Player 1
            Pair of Queens      Pair of Queens
            Highest card Nine   Highest card Seven

5	 	    2H 2D 4C 4D 4S      3C 3D 3S 9S 9D      Player 1
            Full House          Full House
            With Three Fours    with Three Threes

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
'''

types = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
stypes = {2: '02', 3: '03', 4: '04', 5: '05', 6: '06', 7: '07', 8: '08', 9: '09', 10: '10', 11: '11', 12: '12', 13: '13', 14: '14'}

def getPokerScore(cards):
    values = []
    distinct = dict()
    suits = []
    flush = False
    straight = False
    primDup = 1
    secDup = 1
    score = 0

    for card in cards:
        values.append(types[card[0]])

        if types[card[0]] in distinct.keys():
            distinct[types[card[0]]] += 1
        else:
            distinct[types[card[0]]] = 1

        suits.append(card[1])

    values.sort()
    suits.sort()

    if suits[0] == suits[4]:
        flush = True

    if values[0] + 4 == values[4] and len(distinct.keys()) == 5:
        straight = True




    if flush and straight:
        if values[0] == 10:
            score += 91413 * 10 ** 10

        else:
            score += 8 * 10 ** 14
            score += int(stypes[values[4]] + stypes[values[3]]) * 10 ** 10
    elif flush:
        score += 5 * 10 ** 14
        score += int(stypes[values[4]] + stypes[values[3]]) * 10 ** 10
    elif straight:
        score += 4 * 10 ** 14
        score += int(stypes[values[4]] + stypes[values[3]]) * 10 ** 10
    elif len(distinct.keys()) in [2, 3, 4]:
        prim = 0
        primv = 0
        sec = 0
        secv = 0

        for key, value in distinct.iteritems():
            if value > primv or (value == primv and key > prim):
                secv = primv
                sec = prim
                primv = value
                prim = key
            elif value > secv or (value == secv and key > sec):
                secv = value
                sec = key

        if primv == 4:
            score += 7 * 10 ** 14
        elif primv == 3 and len(distinct.keys()) == 2:
            score += 6 * 10 ** 14
        elif primv == 3 and len(distinct.keys()) == 3:
            score += 3 * 10 ** 14
        elif primv == 2 and len(distinct.keys()) == 3:
            score += 2 * 10 ** 14
        elif primv == 2 and len(distinct.keys()) == 4:
            score += 1 * 10 ** 14

        score += int(stypes[prim] + stypes[sec]) * 10 ** 10
    else:
        score += int(stypes[values[4]] + stypes[values[3]]) * 10 ** 10

    score += int(stypes[values[4]] + stypes[values[3]] + stypes[values[2]] + stypes[values[1]] + stypes[values[0]])

    return score

f = open('../data/data-prob54.txt')
count = 0

for line in f.readlines():
    cards = line.split(' ')
    p1 = getPokerScore(cards[0:5])
    p2 = getPokerScore(cards[5:])

    if p1 > p2:
        count += 1

print count





