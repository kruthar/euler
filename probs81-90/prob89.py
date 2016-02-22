__author__ = 'kruthar'
'''
Roman Numerals
For a number written in Roman numerals to be considered valid there are basic rules which must be followed. Even though
the rules allow some numbers to be expressed in more than one way there is always a "best" way of writing a particular number.

For example, it would appear that there are at least six ways of writing the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be the most efficient, as it uses the least number of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in valid,
but not necessarily minimal, Roman numerals; see About... Roman Numerals for the definitive rules for this problem.

Find the number of characters saved by writing each of these in their minimal form.

Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.
'''

def getRomanNumeral(n):
    numeral = ''
    current = n

    while current >= 1000:
        numeral += 'M'
        current -= 1000
    if current >= 900:
        numeral += 'CM'
        current -= 900
    if current >= 800:
        numeral += 'CCM'
        current -= 800
    if current >= 700:
        numeral += 'DCC'
        current -= 700
    if current >= 600:
        numeral += 'DC'
        current -= 600
    if current >= 500:
        numeral += 'DC'
        current -= 500

f = open('../data/data-prob89.txt')

denoms = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
saved = 0

for line in f.readlines():
    temp = 0
    total = 0
    last = ''
    reps = 0
    ts = 0

    for num in line.rstrip():
        # if we hit the same numeral as last, then queue it up, just in case it is subtractive
        if num == last:
            reps += 1
            temp += denoms[num]
        else:
            if last == '' or denoms[num] < denoms[last]:
                total += temp
                temp = denoms[num]
                last = num
            else:
                total += denoms[num] - temp
                temp = 0
                last = ''

    edited = line.rstrip()
    le = len(edited)

    while True:
        touched = False
        edited = edited.replace('IIII', 'IV')
        edited = edited.replace('VV', 'X')
        edited = edited.replace('VIV', 'IX')

        edited = edited.replace('XXXX', 'XL')
        edited = edited.replace('LL', 'C')
        edited = edited.replace('LXL', 'XC')

        edited = edited.replace('CCCC', 'CD')
        edited = edited.replace('DD', 'M')
        edited = edited.replace('DCD', 'CM')
        if le == len(edited):
            break
        le = len(edited)


    total += temp
    saved += len(line.rstrip()) - len(edited)

    print line.rstrip() + ' ' + edited + ' ' + str(total)

print saved
