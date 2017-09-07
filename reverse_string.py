# Reverse a String -
# Enter a string and the program will reverse it and print it out.

while True:
    string = input(
        'Enter a string to see the reverse result: (Type Quit/quit to exit)\n')
    if string == 'Quit':
        print(string[::-1])
        break
    elif string =='quit':
        print(string[::-1])
        break
    else:
        print(string[::-1])
        continue

