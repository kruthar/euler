__author__ = 'kruthar'
'''
By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number: 1296 = 36^2.
What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square number: 9216 = 96^2.
We shall call CARE (and RACE) a square anagram word pair and specify further that leading zeroes are not permitted,
neither may a different letter have the same digital value as another letter.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common
English words, find all the square anagram word pairs (a palindromic word is NOT considered to be an anagram of itself).

What is the largest square number formed by any member of such a pair?

NOTE: All anagrams formed must be contained in the given text file.
'''

from generators import *
from functions import *

def getSubOf(word, mapping):
    numstring = ''
    for letter in word:
        numstring += str(mapping[letter])

    if numstring[0] == '0':
        return -1
    return int(numstring)

def getSubstitutionsHelper(word, index, mapping, digits, original, anagrams):
    result = 0
    if index >= len(word):
        if word[0] != '0' and isSquare(int(word)):
            for anagram in anagrams:
                num = getSubOf(anagram, mapping)
                if num > 0 and isSquare(num):
                    print original, word, anagram, num
                    result = max(result, max(int(word), num))
    else:
        if mapping.has_key(word[index]):
            result = getSubstitutionsHelper(word[:index] + str(mapping[word[index]]) + word[index + 1:], index + 1, mapping, digits, original, anagrams)
        else:
            for i in digits:
                newDigits = digits[:]
                newDigits.remove(i)
                newMapping = mapping.copy()
                newMapping[word[index]] = i
                result = max(result, getSubstitutionsHelper(word[:index] + str(i) + word[index + 1:], index + 1, newMapping, newDigits, original, anagrams))
    return result

def getSubstitutions(anagrams):
     return getSubstitutionsHelper(anagrams[0], 0, dict(), [0,1,2,3,4,5,6,7,8,9], anagrams[0], anagrams[1:])

f = open('../data/data-prob98.txt')
words_raw = f.next()
words = list((x[1:-1] for x in words_raw.split(',')))
sorted_dict = dict()

for word in words:
    s = ''.join(sorted(word))
    if s in sorted_dict:
        sorted_dict[s].append(word)
    else:
        sorted_dict[s] = [word]

max_length = 0
candidates = []
result = 0
for key, value in sorted_dict.iteritems():
    if len(value) > 1:
        print "testing ", value
        result = max(result, getSubstitutions(value))

print result

