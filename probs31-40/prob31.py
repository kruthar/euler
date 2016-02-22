__author__ = 'kruthar'
'''
Coin Sums
In England the currency is made up of pound, E, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, E1 (100p) and E2 (200p).
It is possible to make E2 in the following way:

1xE1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
How many different ways can E2 be made using any number of coins?
'''
count = 0

e1 = 0
while e1 <= 200:
    p50 = 0
    while e1 + p50 <= 200:
        p20 = 0
        while e1 + p50 + p20 <= 200:
            p10 = 0
            while e1 + p50 + p20 + p10 <= 200:
                p5 = 0
                while e1 + p50 + p20 + p10 + p5 <= 200:
                    p2 = 0
                    while e1 + p50 + p20 + p10 + p5 + p2 <= 200:
                        p1 = 0
                        while e1 + p50 + p20 + p10 + p5 + p2 + p1 <= 200:
                            if e1 + p50 + p20 + p10 + p5 + p2 + p1 == 200:
                                count += 1
                            p1 += 1
                        p2 += 2
                    p5 += 5
                p10 += 10
            p20 += 20
        p50 += 50
    e1 += 100

print count + 1