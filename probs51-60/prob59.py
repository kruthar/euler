__author__ = 'kruthar'
'''
XOR encryption
Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.
'''

from functions import *

f = open('../data/data-prob59.txt')
chars = f.readline().split(',')
key = []
found = False

for a in range(ord('a'), ord('z') + 1):
    if found:
        break
    for b in range(ord('a'), ord('z') + 1):
        if found:
            break
        for c in range(ord('a'), ord('z') + 1):
            '''if a == 103 and b == 111 and c == 100:
                pass
            else:
                continue'''
            key = []
            while len(key) + 3 <= len(chars):
                key.append(a)
                key.append(b)
                key.append(c)
            if len(key) < len(chars):
                key.append(a)
            if len(key) < len(chars):
                key.append(b)
            if len(key) < len(chars):
                key.append(c)

            message = []

            for cell in range(len(key)):
                message.append(chr(getDecimal(xor(getBinary(key[cell]), getBinary(int(chars[cell]))))))

            if ' the ' in ''.join(map(str, message)):
                count = 0
                for char in message:
                    count += ord(char)

                print count
                print message
                print '%d %d %d' % (a, b, c)
                print chr(a) + chr(b) + chr(c)
                found = True
                break