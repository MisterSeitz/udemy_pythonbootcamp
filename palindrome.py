# Check if Palindrome - Checks if the string entered by the user is a palindrome.
# That is that it reads the same forwards as backwards like “racecar”


string = input('Enter a string to see if it is a Palindrome: ')
rev_string = string[::-1]

if rev_string == string:
    print('"', string, '" is a Palindrome')
else:
    print('"', string, '" is not a Palindrome')
