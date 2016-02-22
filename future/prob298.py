__author__ = 'kruthar'
'''
Larry and Robin play a memory game involving of a sequence of random numbers between 1 and 10, inclusive, that are
called out one at a time. Each player can remember up to 5 previous numbers. When the called number is in a player's
memory, that player is awarded a point. If it's not, the player adds the called number to his memory, removing another
number if his memory is full.

Both players start with empty memories. Both players always add new missed numbers to their memory but use a different
strategy in deciding which number to remove:

Larry's strategy is to remove the number that hasn't been called in the longest time.
Robin's strategy is to remove the number that's been in the memory the longest time.

Example game:
Turn	Called
number	Larry's
memory	Larry's
score	Robin's
memory	Robin's
score
1	1	1	        0	1	        0
2	2	1,2	        0	1,2	        0
3	4	1,2,4	    0	1,2,4	    0
4	6	1,2,4,6	    0	1,2,4,6	    0
5	1	1,2,4,6	    1	1,2,4,6	    1
6	8	1,2,4,6,8	1	1,2,4,6,8	1
7	10	1,4,6,8,10	1	2,4,6,8,10	1
8	2	1,2,6,8,10	1	2,4,6,8,10	2
9	4	1,2,4,8,10	1	2,4,6,8,10	3
10	1	1,2,4,8,10	2	1,4,6,8,10	3
Denoting Larry's score by L and Robin's score by R, what is the expected value of |L-R| after 50 turns? Give your answer rounded to eight decimal places using the format x.xxxxxxxx .
'''

import random

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def put(self, item):
        self.items.insert(0,item)

    def get(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def contains(self, item):
        return item in self.items

    def __str__(self):
        return str(self.items)

def adjustQueues(num, larry, robin):
    score = [0, 0]
    if larry.contains(num):
        score[0] = 1
        lsize = larry.size()
        for i in range(lsize):
            item = larry.get()
            if item != num:
                larry.put(item)
        larry.put(num)
    else:
        if larry.size() >= 5:
            larry.get()
        larry.put(num)

    if robin.contains(num):
        score[1] = 1
    else:
        if robin.size() >= 5:
            robin.get()
        robin.put(num)


    return score, larry, robin

def runGame():
    larry = Queue()
    robin = Queue()
    score = [0, 0]

    for i in range(50):
        temp, larry, robin = adjustQueues(random.randint(1, 10), larry, robin)
        score[0] += temp[0]
        score[1] += temp[1]

    return abs(score[0] - score[1])

total = 0.0
limit = 100000
for t in range(limit):
    total += runGame()

print total / limit

'''
temp = adjustQueues(1, larry, robin)
print temp[0], str(temp[1]), str(temp[2])
temp = adjustQueues(2, larry, robin)
print temp[0], str(temp[1]), str(temp[2])
temp = adjustQueues(4, larry, robin)
print temp[0], str(temp[1]), str(temp[2])
temp = adjustQueues(6, larry, robin)
print temp[0], str(temp[1]), str(temp[2])
temp = adjustQueues(1, larry, robin)
print temp[0], str(temp[1]), str(temp[2])
temp = adjustQueues(8, larry, robin)
print temp[0], str(temp[1]), str(temp[2])
temp = adjustQueues(10, larry, robin)
print temp[0], str(temp[1]), str(temp[2])
temp = adjustQueues(2, larry, robin)
print temp[0], str(temp[1]), str(temp[2])
temp = adjustQueues(4, larry, robin)
print temp[0], str(temp[1]), str(temp[2])
temp = adjustQueues(1, larry, robin)
print temp[0], str(temp[1]), str(temp[2])
'''






