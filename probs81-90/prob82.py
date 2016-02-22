__author__ = 'kruthar'
'''
Path Sum: 3 ways
The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell in the right column, and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the left column to the right column.
'''

f = open('../data/data-prob81-hard.txt')

grid = []
paths = []

for line in f.readlines():
    list = []
    plist = []
    for cell in line.rstrip().split(','):
        list.append(int(cell))
        plist.append([])
    grid.append(list)
    paths.append(plist)

print grid
print paths

for col in reversed(range(0, len(grid))):
    for row in reversed(range(0, len(grid))):
        print 'dispersing %d %d' % (row, col)

        if col == len(grid) - 1:
            paths[row][col].append(grid[row][col])
        else:
            paths[row][col].append(grid[row][col] + min(paths[row][col+1]))
            if row > 0:
                sum = grid[row][col] + min(paths[row][col + 1])
                for i in reversed(range(0, row)):
                    sum += grid[i][col]
                    paths[i][col].append(sum)
            if row < len(grid) - 1:
                sum = grid[row][col] + min(paths[row][col + 1])
                for i in range(row + 1, len(grid)):
                    sum += grid[i][col]
                    paths[i][col].append(sum)

least = 0

for row in paths:
    if min(row[0]) < least or least == 0:
        least = min(row[0])

print least


