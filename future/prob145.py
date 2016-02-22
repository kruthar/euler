__author__ = 'kruthar'
'''
How many reversible numbers are there below one-million?
Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits.
For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are
reversible. Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (10^9)?
'''

def getOddsBelow(digits):
    if digits == 1:
        return ['']

    results = []
    for entry in getOddsBelow(digits - 1):
        for digit in ['','1','3','5','7','9']:
            if entry+digit != '':
                results.append(entry+digit)

    return results

reversibles = []
digits = 3
done = False
limit = 1000

odds = getOddsBelow(digits)
for odd in odds:
    test = int(odd)
    top = max(test / 2, test - (test / 2))
    bot = test - top

    while (len(str(top)) == len(str(bot))):
        if str(top) == str(bot)[::-1]:
            if top > limit or bot > limit:
                done = True
                break
            if top not in reversibles:
                reversibles.append(top)
            if bot not in reversibles:
                reversibles.append(bot)
            print "found", top, bot
        top += 1
        bot -= 1
    if done:
        break

print reversibles
print len(reversibles)