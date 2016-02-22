__author__ = 'kruthar'
'''
Number spiral diagnosis
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''

import math

dimension = 1001
center = dimension / 2
count = 2
max = dimension ** 2
level = 1
grid = []
x = center + 1
y = center - 1

for a in range(dimension):
    grid.append([])
    for b in range(dimension):
        grid[a].append(0)

grid[center][center] = 1

while count <= max:
    for a in range(2 * level):
        y += 1
        grid[x][y] = count
        count += 1

    for a in range(2 * level):
        x -= 1
        grid[x][y] = count
        count += 1

    for a in range(2 * level):
        y -= 1
        grid[x][y] = count
        count += 1

    for a in range(2 * level):
        x += 1
        grid[x][y] = count
        count += 1

    x += 1
    y -= 1
    level += 1

sum = 0

for i in range(dimension):
    sum += grid[i][i]
    sum += grid[dimension - i - 1][i]

print sum - 1