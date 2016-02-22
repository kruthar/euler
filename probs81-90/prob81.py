__author__ = 'kruthar'
'''
Path Sum: two ways
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.
'''

f = open('../data/data-prob81-hard.txt')

grid = []
paths = []

for line in f.readlines():
    list = []
    plist = []
    for cell in line.rstrip().split(','):
        list.append(int(cell))
        plist.append(0)
    grid.append(list)
    paths.append(plist)

print grid
print paths

for diag in reversed(range(0, len(grid))):
    for step in range(0, len(grid) - diag):
        print '%d %d' % (len(grid) - 1 - step, diag + step)
        row = len(grid) - 1 - step
        col = diag + step

        if row == len(grid) - 1 and col == len(grid) - 1:
            paths[row][col] = grid[row][col]
        elif row == len(grid) - 1:
            paths[row][col] = grid[row][col] + paths[row][col + 1]
        elif col == len(grid) - 1:
            paths[row][col] = grid[row][col] + paths[row + 1][col]
        else:
            paths[row][col] = grid[row][col] + min(paths[row][col + 1], paths[row + 1][col])

print paths

for diag in reversed(range(0, len(grid) - 1)):
    for step in range(0, diag + 1):
        print '%d %d' % (diag - step, step)
        row = diag- step
        col = step

        paths[row][col] = grid[row][col] + min(paths[row][col + 1], paths[row + 1][col])

print paths
