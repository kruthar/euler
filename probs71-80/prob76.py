__author__ = 'kruthar'
'''
Counting Summations
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
'''

n = 100

remCounts = dict()

def countSummations(n, last, rem, list):
    if rem == 0:
        return 1
    if remCounts.has_key(str(last) + ' ' + str(rem)):
        return remCounts[str(last) + ' ' + str(rem)]

    count = 0
    for i in range(last, rem + 1):
        count += countSummations(n, i, rem - i, list + [i])

    remCounts[str(last) + ' ' + str(rem)] = count
    return count

counts = countSummations(n, 1, n, [])
print counts - 1