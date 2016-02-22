__author__ = 'kruthar'
'''
Magic 5-gon ring
Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.


Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this example), each solution can be described uniquely. For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.

Total	Solution Set
9	4,2,3; 5,3,1; 6,1,2
9	4,3,2; 6,2,1; 5,1,3
10	2,3,5; 4,5,1; 6,1,3
10	2,5,3; 6,3,1; 4,1,5
11	1,4,6; 3,6,2; 5,2,4
11	1,6,4; 5,4,2; 3,2,6
12	1,5,6; 2,6,4; 3,4,5
12	1,6,5; 3,5,4; 2,4,6
By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is the maximum 16-digit string for a "magic" 5-gon ring?
'''

from generators import *

gon = 5
limit = 16
max = 0

for perm in permutations(range(1, 2 * gon + 1)):
    total = sumList(perm[0:3])
    construct = perm[0:3]
    last = perm[2]
    fail = False

    for side in range(gon - 2):
        construct += [perm[3 + 2 * side]] + [last] + [perm[4 + 2 * side]]
        temp = perm[3 + 2 * side] + last + perm[4 + 2 * side]
        if temp != total:
            fail = True
            break

        last = perm[4 + 2 * side]

    construct += [perm[-1]] + [perm[-2]] + [perm[1]]

    if min(construct[0::3]) != construct[0]:
        continue

    if total != perm[1] + sumList(perm[len(perm) - 2:]):
        fail = True

    if not fail and len(''.join(map(str, construct))) == limit and int(''.join(map(str, construct))) > max:
        max = int(''.join(map(str, construct)))

print max


