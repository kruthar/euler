__author__ = 'kruthar'
'''
Passcode Derivation
A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.
'''

from heapq import *

def getPossibles(passcode, current, start = -1):
    # return empty list if we reach the end of the passcode
    if len(passcode) == 0:
        return [current]

    # if we are at the end of the current possible, then just return a list with the remaining passcode appended to the current possible
    if start >= len(current):
        return [current + passcode]

    list = []
    if passcode[0] in current[start + 1:]:
        s = len(current[0:start + 1]) + current[start + 1:].index(passcode[0])
        list += getPossibles(passcode[1:len(passcode)], current, s)
    else:
        for i in range(start + 1, len(current) + 1):
            list += getPossibles(passcode[1:len(passcode)], current[0:i] + passcode[0] + current[i:], i)

    return list

def getPriority(score, remaining, prec):
    result = score
    while len(result) < prec:
        result = '0' + result

    return result + str(remaining)

f = open('../data/data-prob79.txt', 'r')

codes = []
q = []
prec = 50

for line in f.readlines():
    codes.append(line.rstrip())

heappush(q, (getPriority(codes[0], len(codes) - 1, prec), {'current': codes[0], 'remaining': codes[1:]}))

while True:
    tuple = heappop(q)[1]
    print tuple

    if len(tuple['remaining']) == 0:
        print tuple
        break

    newl = tuple['remaining'][1:]

    for possible in getPossibles(tuple['remaining'][0], tuple['current']):
        heappush(q, (getPriority(possible, len(newl), prec), {'current': possible, 'remaining': newl}))
