__author__ = 'kruthar'
'''
Consider all the words which can be formed by selecting letters, in any order, from the phrase:

thereisasyetinsufficientdataforameaningfulanswer
Suppose those with 15 letters or less are listed in alphabetical order and numbered sequentially starting at 1.
The list would include:

1 : a
2 : aa
3 : aaa
4 : aaaa
5 : aaaaa
6 : aaaaaa
7 : aaaaaac
8 : aaaaaacd
9 : aaaaaacde
10 : aaaaaacdee
11 : aaaaaacdeee
12 : aaaaaacdeeee
13 : aaaaaacdeeeee
14 : aaaaaacdeeeeee
15 : aaaaaacdeeeeeef
16 : aaaaaacdeeeeeeg
17 : aaaaaacdeeeeeeh
...
28 : aaaaaacdeeeeeey
29 : aaaaaacdeeeeef
30 : aaaaaacdeeeeefe
...
115246685191495242: euleoywuttttsss
115246685191495243: euler
115246685191495244: eulera
...
525069350231428029: ywuuttttssssrrr
Define P(w) as the position of the word w.
Define W(p) as the word in position p.
We can see that P(w) and W(p) are inverses: P(W(p)) = p and W(P(w)) = w.

Examples:

W(10) = aaaaaacdee
P(aaaaaacdee) = 10
W(115246685191495243) = euler
P(euler) = 115246685191495243
Find W(P(legionary) + P(calorimeters) - P(annihilate) + P(orchestrated) - P(fluttering)).
Give your answer using lowercase characters (no punctuation or space).
'''

import math

def getCombinations(s):
    if len(s) == 0:
        return ['']

    results = []
    for a in range(len(s)):
        for b in getCombinations(s[0:a] + s[a + 1:]):
            if b not in results:
                results.append(b)
            if s[a] +b not in results:
                results.append(s[a] + b)
    return results

def multisetPerms(s):
    uniq = dict()
    for c in s:
        if uniq.has_key(c):
            uniq[c] += 1
        else:
            uniq[c] = 1

    count = math.factorial(len(s))
    for m in uniq.itervalues():
        count /= m

    return count

def allKPerms(n):
    count = 0
    for i in range(1, n + 1):
        count += math.factorial(n) / math.factorial(n - i)
    return count

def choose(n, k):
    return math.factorial(n) / math.factorial(n - k)

def trash(s):
    allk = allKPerms(len(s))

    uniq = dict()
    for c in s:
        if uniq.has_key(c):
            uniq[c] += 1
        else:
            uniq[c] = 1

    for key, value in uniq.iteritems():
        if value > 1:
            for i in range(1, value):
                allk -= choose(value, i)

    return allk


needle = 'bc'
haystack = 'aabd'
list = sorted(getCombinations(haystack))[1:]
print list
print len(list)
print allKPerms(len(haystack))
print trash(haystack)

