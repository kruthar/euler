__author__ = 'kruthar'
'''
Dice Game
Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.

Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal.

What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven decimal places in the form 0.abcdefg
'''

def diceProb(sides, dice):
    if dice == 1:
        result = dict()
        for i in range(1, sides + 1):
            result[i] = 1
        return result

    result = dict()
    for i in range(1, sides + 1):
        for side, count in diceProb(sides, dice - 1).iteritems():
            if result.has_key(side + i):
                result[side + i] += count
            else:
                result[side + i] = count

    return result

prob4 = diceProb(4, 9)
prob6 = diceProb(6, 6)
wins = 0.0
total = 0.0
for role4, count4 in prob4.iteritems():
    for role6, count6 in prob6.iteritems():
        total += count4 * count6
        if role4 > role6:
            wins += count4 * count6

print wins
print total
print float(wins/total)
print prob4
print prob6