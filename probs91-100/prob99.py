__author__ = 'kruthar'
'''
Largest Exponential
Comparing two numbers written in index form like 2^11 and 3^7 is not difficult, as any calculator would confirm that 2^11 = 2048 < 3^7 = 2187.

However, confirming that 632382^518061 > 519432^525806 would be much more difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a
base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
'''

from functions import *

f = open('../data/data-prob99.txt')
max = 0
index = 0
count = 1

for line in f.readlines():
    exp = line.rstrip().split(',')
    val = int(exp[1]) * math.log10(int(exp[0]))
    if val > max:
        max = val
        index = count
    count += 1


print max
print index