__author__ = 'kruthar'

def prettyPrintMatrices(m1, m2=None):
    for i in range(len(m1)):
        if m2 != None:
            print m1[i], "\t\t", m2[i]
        else:
            print m1[i]
    print

def getCopy(matrix):
    newmatrix = []
    for row in matrix:
        newmatrix.append(row[:])
    return newmatrix

# gets the smaller matrix, leaving out the given row and column
def getLowerMatrix(matrix, row, col):
    newmatrix = []
    for i in range(len(matrix)):
        if i != row:
            newrow = []
            for j in range(len(matrix[i])):
                if j != col:
                    newrow.append(matrix[i][j])
            newmatrix.append(newrow)
    return newmatrix

def getDeterminate2x2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def getDeterminate(matrix):
    if len(matrix) == 2:
        return getDeterminate2x2(matrix)

    sign = 1
    result = 0

    for i in range(len(matrix[0])):
        result += sign * matrix[0][i] * getDeterminate(getLowerMatrix(matrix, 0, i))
        sign *= -1
    return result

def getCofactorMatrix(matrix):
    newmatrix = []
    sign = 1
    for i in range(len(matrix)):
        newrow = []
        for j in range(len(matrix)):
            newrow.append(sign * getDeterminate(getLowerMatrix(matrix, i, j)))
            sign *= -1
        newmatrix.append(newrow)
    return newmatrix


def transpose(matrix):
    newmatrix = getCopy(matrix)
    for i in range(1, len(newmatrix)):
        for j in range(0, i):
            temp = newmatrix[i][j]
            newmatrix[i][j] = newmatrix[j][i]
            newmatrix[j][i] = temp
    return newmatrix

def getAdjugate(matrix):
    return transpose(getCofactorMatrix(matrix))

# returns the detA value and adjugate matrix
def getInverse(matrix):
    if len(matrix) == 2:
        return getDeterminate2x2(matrix), [[matrix[1][1], -matrix[0][1]], [-matrix[1][0], matrix[0][0]]]
    return getDeterminate(matrix), getAdjugate(matrix)

# Matrix multiplication, only works for m2 with a single column
def matrixMultiplyXx1(m1, m2):
    if len(m1[0]) != len(m2):
        print "m1 columns not equal to m2 rows"
        return None
    result = []

    for m1row in range(len(m1)):
        newrow = []
        for m2col in range(len(m2[m1row])):
            total = 0
            for cell in range(len(m1[m1row])):
                total += m1[m1row][cell] * m2[cell][m2col]
            newrow.append(total)
        result.append(newrow)

    return result

def scalarDivideMatrix(matrix, scalar):
    newmatrix = getCopy(matrix)
    for i in range(len(newmatrix)):
        for j in range(len(newmatrix[i])):
            newmatrix[i][j] /= scalar
    return newmatrix

def solveSystem(equations, solutions):
    detA, inverse = getInverse(equations)
    if detA == 0:
        print "detA = 0, cannot find the inverse"
        return None
    print detA, inverse
    answers = matrixMultiplyXx1(inverse, solutions)
    return scalarDivideMatrix(answers, detA)