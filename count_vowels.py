# Count Vowels - Enter a string and the program counts the number of vowels
# in the text. For added complexity have it report a sum of each vowel found.

while True:
    vowels = ['a','e','i','o','u']

    input_string = input('Please input a string to see how many vowels: ').lower()
    vowels_in_string = []

    for x in input_string:
        if x in vowels:
            vowels_in_string.append(x)
        else:
            pass

        
    print('There are a total of {} vowels in the string provided'.format(len(vowels_in_string)))
    print('Count for a : ', vowels_in_string.count('a'))
    print('Count for e : ', vowels_in_string.count('e'))
    print('Count for i : ', vowels_in_string.count('i'))
    print('Count for o : ', vowels_in_string.count('o'))
    print('Count for u : ', vowels_in_string.count('u'))
