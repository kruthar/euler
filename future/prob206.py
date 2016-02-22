__author__ = 'kruthar'
'''
Concealed Square
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each "_" is a single digit.
'''

# the only way to square and end in a zero is for the root to end in a zero.
# if the root ends in a zero then the first two digits of the square will also be 0, so we can just cut those from the lookup.

# the only way to square and end in a 9 is for the root to end in a 3 (9) or 7 (49), so we can restrict our testing to
# only root numbers that end in 3 or 7.

import math

for i in range(int(math.sqrt(10203040506070809)), int(math.sqrt(19293949596979899))):
    if str(i)[-1] in ['3','7']:
        square = i ** 2
        if str(square)[0::2] == '123456789':
            print str(i) + '0'
            break