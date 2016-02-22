__author__ = 'kruthar'
'''
Sudoku
Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept. Its origin is unclear, but credit
must be attributed to Leonhard Euler who invented a similar, and much more difficult, puzzle idea called Latin Squares.
The objective of Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, column,
and 3 by 3 box contains each of the digits 1 to 9. Below is an example of a typical starting puzzle grid and its solution grid.

A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be necessary to employ
"guess and test" methods in order to eliminate options (there is much contested opinion over this). The complexity of the
search determines the difficulty of the puzzle; the example above is considered easy because it can be solved by straight
forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles ranging
in difficulty, but all with unique solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid;
for example, 483 is the 3-digit number found in the top left corner of the solution grid above.
'''

import math
from sets import Set
import heapq


def numOrBlank(num):
    if num == 0:
        return ' '
    return num

def prettyprint(grid):
    for i, row in enumerate(grid):
        print numOrBlank(row[0]), numOrBlank(row[1]), numOrBlank(row[2]), '|', numOrBlank(row[3]), numOrBlank(row[4]), numOrBlank(row[5]), '|', numOrBlank(row[6]), numOrBlank(row[7]), numOrBlank(row[8])
        if (i + 1) % 3 == 0 and i < 8:
            print '_____________________'
            print

def getPuzzle(lines):
    title = lines[0]
    grid = []

    for i in range(9):
        line = lines[i + 1]
        row = []
        for digit in line:
            row.append(int(digit))
        grid.append(row)
    return title, grid

def puzzles():
    f = open('../data/data-prob96.txt')

    i = 0
    puzzle = []
    for l in f.readlines():
        puzzle.append(l.strip())
        i += 1
        if i == 10:
            yield(getPuzzle(puzzle))
            puzzle = []
            i = 0

def checkAndFill(grid, row, col):
    if grid[row][col] != 0:
        return False

    possibles = [1,2,3,4,5,6,7,8,9]

    # Check horizontal row
    for i in grid[row]:
        if i in possibles:
            possibles.remove(i)

    # Check vertical column
    for j in grid:
        if j[col] in possibles:
            possibles.remove(j[col])

    # Check 3x3 box
    rowOffset = (row / 3) * 3
    colOffset = (col / 3) * 3
    for a in range(rowOffset, rowOffset + 3):
        for b in range(colOffset, colOffset + 3):
            if grid[a][b] in possibles:
                possibles.remove(grid[a][b])

    if len(possibles) == 1:
        grid[row][col] = possibles[0]
        return True

    return False

def check(grid, row, col):
    if grid[row][col] != 0:
        return []

    possibles = [1,2,3,4,5,6,7,8,9]

    # Check horizontal row
    for i in grid[row]:
        if i in possibles:
            possibles.remove(i)

    # Check vertical column
    for j in grid:
        if j[col] in possibles:
            possibles.remove(j[col])

    # Check 3x3 box
    rowOffset = (row / 3) * 3
    colOffset = (col / 3) * 3
    for a in range(rowOffset, rowOffset + 3):
        for b in range(colOffset, colOffset + 3):
            if grid[a][b] in possibles:
                possibles.remove(grid[a][b])

    return possibles

def simpleSolve(grid):
    found = True
    rounds = 0
    while found:
        rounds += 1
        found = False
        for i in range(9):
            for j in range(9):
                if checkAndFill(grid, i, j):
                    found = True

    return rounds > 1, grid

def getRowsAndCols(grid, num):
    rowPossibles = [0,1,2,3,4,5,6,7,8]
    colPossibles = [0,1,2,3,4,5,6,7,8]
    for i in range(9):
        for j in range(9):
            if grid[i][j] == num:
                if i in rowPossibles:
                    rowPossibles.remove(i)
                if j in colPossibles:
                    colPossibles.remove(j)

    return rowPossibles, colPossibles

def getAllSims(rows, cols):
    if len(rows) > 5:
        return []

    if len(rows) == 1:
        return [[(rows[0], cols[0])]]

    results = []
    for i, r in enumerate(rows):
        for j, c in enumerate(cols):
            if i >= j:
                for sim in getAllSims(rows[:i] + rows[i + 1:], cols[:j] + cols[j + 1:]):
                    results.append(sim + [(r, c)])
    return results

def testSimPossible(grid, sim):
    blocks = []
    for placement in sim:
        # Test if cell is open
        if grid[placement[0]][placement[1]] != 0:
            return False

        # Test if blockRow is open
        br = placement[0] / 3
        bc = placement[1] / 3
        if (br, bc) in blocks:
            return False
        blocks.append((br,bc))

    return True

def getPossibleSims(grid, sims):
    results = []
    for sim in sims:
        if testSimPossible(grid, sim):
            if sorted(sim) not in results:
                results.append(sorted(sim))
    return results

def intelligentSolve(grid):
    for i in range(1, 10):
        rows, cols = getRowsAndCols(grid, i)
        allsims = getAllSims(rows, cols)
        possiblesims = getPossibleSims(grid, allsims)
        if len(possiblesims) == 1:
            for sim in possiblesims[0]:
                grid[sim[0]][sim[1]] = i
            return True, grid
    return False, grid

def lineSolve(grid):
    found = False

    for i, row in enumerate(grid):
        possibles = [1,2,3,4,5,6,7,8,9]
        for cell in row:
            if cell in possibles:
                possibles.remove(cell)
        byNumber = dict()
        byCell = dict()
        for j, cell in enumerate(row):
            if cell == 0:
                cellPossibles = check(grid, i, j)
                for possible in possibles:
                    if possible in cellPossibles:
                        if possible in byNumber.keys():
                            byNumber[possible].append(j)
                        else:
                            byNumber[possible] = [j]

                        if j in byCell.keys():
                            byCell[j].append(possible)
                        else:
                            byCell[j] = [possible]

        for key, value in byNumber.iteritems():
            if len(value) == 1:
                found = True
                grid[i][value[0]] = key
        for key, value in byCell.iteritems():
            if len(value) == 1:
                found = True
                grid[i][key] = value[0]

    for col in range(9):
        possibles = [1,2,3,4,5,6,7,8,9]
        for row in range(9):
            if grid[row][col] in possibles:
                possibles.remove(grid[row][col])
        byNumber = dict()
        byCell = dict()
        for row in range(9):
            if grid[row][col] == 0:
                cellPossibles = check(grid, row, col)
                for possible in possibles:
                    if possible in cellPossibles:
                        if possible in byNumber.keys():
                            byNumber[possible].append(row)
                        else:
                            byNumber[possible] = [row]

                        if row in byCell.keys():
                            byCell[row].append(possible)
                        else:
                            byCell[row] = [possible]

        for key, value in byNumber.iteritems():
            if len(value) == 1:
                found = True
                grid[value[0]][col] = key
        for key, value in byCell.iteritems():
            if len(value) == 1:
                found = True
                grid[key][col] = value[0]

    for boxRow in range(3):
        for boxCol in range(3):
            possibles = [1,2,3,4,5,6,7,8,9]
            for rowOffset in range(3):
                row = boxRow * 3 + rowOffset
                for colOffset in range(3):
                    col = boxCol * 3 + colOffset

                    if grid[row][col] in possibles:
                        possibles.remove(grid[row][col])
            byNumber = dict()
            byCell = dict()
            for rowOffset in range(3):
                row = boxRow * 3 + rowOffset
                for colOffset in range(3):
                    col = boxCol * 3 + colOffset

                    if grid[row][col] == 0:
                        cellPossibles = check(grid, row, col)
                        for possible in possibles:
                            if possible in cellPossibles:
                                cellIndex = "%d#%d" % (row, col)
                                if possible in byNumber.keys():
                                    byNumber[possible].append(cellIndex)
                                else:
                                    byNumber[possible] = [cellIndex]

                                if cellIndex in byCell.keys():
                                    byCell[cellIndex].append(possible)
                                else:
                                    byCell[cellIndex] = [possible]

            for key, value in byNumber.iteritems():
                if len(value) == 1:
                    found = True
                    r,c = value[0].split("#")
                    grid[int(r)][int(c)] = key
            for key, value in byCell.iteritems():
                if len(value) == 1:
                    found = True
                    r,c = key.split("#")
                    grid[int(r)][int(c)] = value[0]

    return found, grid

def isSolved(grid):
    for row in grid:
        possibles = [1,2,3,4,5,6,7,8,9]
        for cell in row:
            if cell in possibles:
                possibles.remove(cell)
        if len(possibles) != 0:
            return False
    for col in range(9):
        possibles = [1,2,3,4,5,6,7,8,9]
        for row in range(9):
            if grid[row][col] in possibles:
                possibles.remove(grid[row][col])
        if len(possibles) != 0:
            return False
    return True

def attemptSolve(grid):
    temp = grid
    found = True
    while found:
        found = False
        altered = True
        while altered:
            altered, temp = simpleSolve(temp)
            if altered:
                found + True

        altered = True
        while altered:
            altered, temp = intelligentSolve(temp)
            if altered:
                found + True

        altered = True
        while altered:
            altered, temp = lineSolve(temp)
            if altered:
                found + True
    return temp

def copyGrid(grid):
    newGrid = []
    for row in grid:
        newGrid.append(row[:])
    return newGrid

def guessAndCheck(grid):
    for row in range(9):
        for col in range(9):
            for possible in check(grid, row, col):
                testGrid = copyGrid(grid)
                testGrid[row][col] = possible
                testGrid = attemptSolve(testGrid)
                if isSolved(testGrid):
                    return testGrid


pgen = puzzles()
total = 0;
for puz in pgen:
    print "solving ", puz[0]

    temp = attemptSolve(puz[1])

    if not isSolved(temp):
        temp = guessAndCheck(temp)

    if isSolved(temp):
        raw = "%d%d%d" % (temp[0][0], temp[0][1], temp[0][2])
        total += int(raw)
    else:
        print "uh oh"

    print "solved ", puz[0]

print total