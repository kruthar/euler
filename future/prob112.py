__author__ = 'kruthar'
'''
Bouncy Numbers
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525)
are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
'''

def isBouncy(n):
    up = False
    down = False
    string = str(n)

    for c in range(len(string) - 1):
        if string[c] > string[c + 1]:
            down = True
        if string[c] < string[c + 1]:
            up = True

    return up and down

limit = 0.99
total = 1.0
count = 0.0

while count / total < limit:
    total += 1
    if isBouncy(int(total)):
        count += 1

print total