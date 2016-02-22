__author__ = 'kruthar'
'''
Powerful digit counts
The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
'''

power = 1
count = 0

while True:
    current = 1
    done = True

    while True:
        exp = str(current ** power)
        if len(exp) == power:
            count += 1
            done = False
        if len(exp) > power:
            break
        current += 1

    if done:
        break

    power += 1

print count