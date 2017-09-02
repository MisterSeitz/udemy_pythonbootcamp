# Count Words in a String -
# Counts the number of individual words in a string.
# For added complexity read these strings in from a
# text file and generate a summary.

import string
file = open(input('Enter File Name (File must be in same directory): '))
line = file.read()
line = line.translate(str.maketrans('', '', string.punctuation))
word = line.split()
wordlist = []
for word in word:
    word = wordlist.append(word)
    length = len(wordlist)

print('The file has {x} words'.format(x=length))

