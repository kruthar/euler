__author__ = 'kruthar'
'''
Coded Triangle Numbers
The nth term of the sequence of triangle numbers is given by, tn = n/2(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
'''

from generators import *

f = open('../data/data-prob42.txt')
words = f.readline().replace('"', '').split(',')
ts = []
count = 0

for t in triangle(1000):
    ts.append(t)

for a in words:
    if getWordScore(a) in ts:
        count += 1

print count