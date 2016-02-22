__author__ = 'kruthar'
'''
Path Sum: 4 ways
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by moving left, right, up, and down, is indicated in bold red and is equal to 2297.

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by moving left, right, up, and down.
'''

from heapq import *

prec = 10

f = open('../data/data-prob82-hard.txt')

grid = []
spots = []

for line in f.readlines():
    list = []
    plist = []
    for cell in line.rstrip().split(','):
        list.append(int(cell))
        plist.append(0)
    grid.append(list)
    spots.append(plist)

h = []

def getPriority(score):
    result = str(score)
    while len(result) < prec:
        result = '0' + result

    return result

def push(x, y, sum, prev):
    spot = str(x) + '_' + str(y)
    if x >=0 and x < len(grid) and y >= 0 and y < len(grid):
        if cell not in prev:
            if spots[x][y] == 0 or sum < spots[x][y]:
                spots[x][y] = sum
                heappush(h, (getPriority(sum), {'x': x, 'y': y, 'sum':sum, 'prev': prev[:] + [spot]}))


heappush(h, (getPriority(grid[0][0]), {'x':0, 'y':0, 'sum':grid[0][0], 'prev':['0_0']}))
spots[0][0] = True

count = 1
while True:
    count -= 1

    tuple = heappop(h)
    x = int(tuple[1]['x'])
    y = int(tuple[1]['y'])
    sum = int(tuple[1]['sum'])
    prev = tuple[1]['prev'][:]
    spot = str(x) + '_' + str(y)
    print str(sum) + ' ' + str(x + y)

    if x > 0:
        push(x - 1, y, sum + grid[x - 1][y], prev)
    if x < len(grid) - 1:
        push(x + 1, y, sum + grid[x + 1][y], prev)
    if y > 0:
        push(x, y - 1, sum + grid[x][y - 1], prev)
    if y < len(grid) - 1:
        push(x, y + 1, sum + grid[x][y + 1], prev)

    if x == len(grid) - 1 and y == len(grid) - 1:
        print sum
        break

print count




