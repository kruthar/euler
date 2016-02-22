__author__ = 'kruthar'
'''
Lexicographical Permutations
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

count = 0

def lexico(list):
    perms = []

    if len(list) == 1:
        return [list]

    for a in list:
        lex = []

        for b in list:
            if a != b:
                lex.append(b)

        for perm in lexico(lex):
            perms.append([a] + perm)

    return perms

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for a in list:
    found = False
    lex = []

    for b in list:
        if a != b:
            lex.append(b)

    for perm in lexico(lex):
        count += 1
        if count == 1000000:
            found = True
            word = ''
            for c in [a] + perm:
                word += str(c)
            print word
            break

    if found:
        break