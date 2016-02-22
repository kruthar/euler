__author__ = 'kruthar'
'''
Coin Partitions
Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can separated into piles in exactly seven different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O
Find the least value of n for which p(n) is divisible by one million.
'''

pents = dict()

def pent(k):
    return (k * (3 * k - 1)) / 2

parts = dict()

def partitions(n):
    if parts.has_key(n):
        return parts[n]

    if n < 2:
        return 1

    i = 1
    result = 0
    #string = ''
    done = False
    while not done:
        for k in [i, -i]:
            gk = pent(k)
            if n - gk >= 0:
                #string += str(-1 ** (k - 1) * partitions(n - gk)) + ' '
                result += int((-1) ** (k - 1)) * partitions(n - gk)
            else:
                done = True
                break
        i += 1

    parts[n] = result
    #print str(n) + ': ' + string + ' = ' + str(result)
    return result

i = 1

while True:
    p = partitions(i)
    if p % 1000000 == 0:
        print i
        break
    i += 1




