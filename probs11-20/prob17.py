__author__ = 'kruthar'
'''
Number Letter Counts
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

words = {0: '', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight', 9: 'nine',
        10 : 'ten', 11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen', 15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen', 19 : 'nineteen',
        20 : 'twenty', 30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty', 70 : 'seventy', 80 : 'eighty', 90 : 'ninety'}

string = ''

for num in range(1, 1001):
    word = ''

    if num < 10:
        word = words[num]
    else:
        teen = int(str(num)[-2:])
        if teen != 0:
            if teen < 20:
                word = words[teen]
            else:
                tens = int(str(num)[-2:-1] + '0')
                ones = int(str(num)[-1:])
                word = words[tens] + words[ones]


        if num >= 100:
            hundreds = int(str(num)[-3:-2])

            if hundreds != 0:
                if num % 100 != 0:
                    word = 'and' + word

                word = words[hundreds] + 'hundred' + word

        if num >= 1000:
            thousands = int(str(num)[-4:-3])

            if num != 1000:
                word = 'and' + word

            word = words[thousands] + 'thousand' + word

    string += word
    print word

print len(string)


