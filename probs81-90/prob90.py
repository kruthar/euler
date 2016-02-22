from sets import Set

__author__ = 'kruthar'
'''
Each of the six faces on a cube has a different digit (0 to 9) written on it; the same is done to a second cube.
By placing the two cubes side-by-side in different positions we can form a variety of 2-digit numbers.

For example, the square number 64 could be formed:


In fact, by carefully choosing the digits on both cubes it is possible to display all of the square numbers below
one-hundred: 01, 04, 09, 16, 25, 36, 49, 64, and 81.

For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on one cube and {1, 2, 3, 4, 8, 9} on the other cube.

However, for this problem we shall allow the 6 or 9 to be turned upside-down so that an arrangement like {0, 5, 6, 7, 8, 9}
and {1, 2, 3, 4, 6, 7} allows for all nine square numbers to be displayed; otherwise it would be impossible to obtain 09.

In determining a distinct arrangement we are interested in the digits on each cube, not the order.

{1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
{1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}

But because we are allowing 6 and 9 to be reversed, the two distinct sets in the last example both represent the
extended set {1, 2, 3, 4, 5, 6, 9} for the purpose of forming 2-digit numbers.

How many distinct arrangements of the two cubes allow for all of the square numbers to be displayed?
'''

squares = ['01', '04', '09', '16', '25', '36', '49', '46', '81']

def diceHelper(start):
    if start > 9:
        return [[]]

    dice = []
    for die in diceHelper(start + 1):
        if len(die) < 6:
            dice.append([start] + die)
        dice.append(die)

    return dice

def getDice():
    dice = []
    for die in diceHelper(0):
        if len(die) == 6:
            dice.append(die)
    return dice

dice = getDice()
goal = []

for d1 in dice:
    for d2 in dice:
        satisfies = True
        for square in squares:
            i1 = int(square[0])
            i2 = int(square[1])

            if (i2 == 6 or i2 == 9) and ((i1 in d1 and (6 in d2 or 9 in d2)) or ((6 in d1 or 9 in d1) and i1 in d2)):
                pass
            elif (i1 in d1 and i2 in d2) or (i2 in d1 and i1 in d2):
                pass
            else:
                satisfies = False
                break
        if satisfies:
            if [d1, d2] not in goal and [d2, d1] not in goal:
                goal.append([d1, d2])

print len(goal)