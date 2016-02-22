__author__ = 'kruthar'
'''
Arithmatic Expressions
By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and making use of the four arithmetic operations (+, -, *, /) and brackets/parentheses, it is possible to form different positive integer targets.

For example,

8 = (4 * (1 + 3)) / 2
14 = 4 * (3 + 1 / 2)
19 = 4 * (2 + 3) - 1
36 = 3 * 4 * (2 + 1)

Note that concatenations of the digits, like 12 + 34, are not allowed.

Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different target numbers of which 36 is the maximum, and each of the numbers 1 to 28 can be obtained before encountering the first non-expressible number.

Find the set of four distinct digits, a < b < c < d, for which the longest set of consecutive positive integers, 1 to n, can be obtained, giving your answer as a string: abcd.
'''

def getPerms(l):
    if len(l) <= 0:
        return [[]]

    results = []
    for i, c in enumerate(l):
        for perm in getPerms(l[0:i] + l[i + 1:]):
            results.append([c] + perm)

    return results

def getExpressions(l):
    if len(l) == 1:
        return l

    results = []
    for i in range(len(l) - 1):
        results += getExpressions(l[0:i] + [{'value': float(l[i]['value']) + float(l[i + 1]['value']), 'expression':'(' + l[i]['expression'] + '+' + l[i + 1]['expression'] + ')'}] + l[i + 2:])
        results += getExpressions(l[0:i] + [{'value': float(l[i]['value']) - float(l[i + 1]['value']), 'expression':'(' + l[i]['expression'] + '-' + l[i + 1]['expression'] + ')'}] + l[i + 2:])
        results += getExpressions(l[0:i] + [{'value': float(l[i]['value']) * float(l[i + 1]['value']), 'expression':'(' + l[i]['expression'] + '*' + l[i + 1]['expression'] + ')'}] + l[i + 2:])
        if l[i + 1]['value'] != 0:
            results += getExpressions(l[0:i] + [{'value': float(l[i]['value']) / float(l[i + 1]['value']), 'expression':'(' + l[i]['expression'] + '/' + l[i + 1]['expression'] + ')'}] + l[i + 2:])

    return results

def expDict(a, b, c, d):
    expr = dict()
    for perm in getPerms([a,b,c,d]):
        for expression in getExpressions([{'value':perm[0], 'expression': str(perm[0])}, {'value':perm[1], 'expression': str(perm[1])}, {'value':perm[2], 'expression': str(perm[2])}, {'value':perm[3], 'expression': str(perm[3])}]):
            if expression['value'] % 1 == 0:
                expr[expression['value']] = expression
    return expr

#for key, value in expDict(1,2,3,4).items():
#    print key, value['expression']


max = 0
maxstring = ''

for a in range(1, 7):
    for b in range(a + 1, 8):
        for c in range(b + 1, 9):
            for d in range(c + 1, 10):
                print str(a) + str(b) + str(c) + str(d)
                expr = expDict(a, b, c, d)

                largest = 1
                while True:
                    if not expr.has_key(largest):
                        break
                    largest += 1

                if largest > max:
                    max = largest
                    maxstring = str(a) + str(b) + str(c) + str(d)

print max
print maxstring
