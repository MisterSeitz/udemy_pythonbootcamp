nine = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# Global Winning Lists:

wl1 = ['1', '2', '3']
wl2 = ['4', '5', '6']
wl3 = ['7', '8', '9']
wl4 = ['1', '4', '7']
wl5 = ['2', '5', '8']
wl6 = ['3', '6', '9']
wl7 = ['1', '5', '9']
wl8 = ['3', '5', '7']

# Global Default Board Lines

line1 = '| 7 | 8 | 9 |'
line2 = ' --- --- --- '
line3 = '| 4 | 5 | 6 |'
line4 = ' --- --- --- '
line5 = '| 1 | 2 | 3 |'


def printboard():
    ''' Function That Prints Board Based On Current Global Line Values '''
    global line1, line2, line3, line4, line5
    print(
        '\n', line1, '\n', line2, '\n', line3, '\n', line4, '\n', line5, '\n')


def reset():
    ''' Function That Resets Board To Global Default Lines '''
    global line1, line2, line3, line4, line5
    line1 = '| 7 | 8 | 9 |'
    line2 = ' --- --- --- '
    line3 = '| 4 | 5 | 6 |'
    line4 = ' --- --- --- '
    line5 = '| 1 | 2 | 3 |'


def checkboardx():
    ''' Funtion that replaces number on board with X for Player1 '''
    global line1, line2, line3, line4, line5
    if userinput in line1[2]:
        line1 = line1.replace("7", "X")
    elif userinput in line1[6]:
        line1 = line1.replace("8", "X")
    elif userinput in line1[10]:
        line1 = line1.replace("9", "X")
    elif userinput in line3[2]:
        line3 = line3.replace("4", "X")
    elif userinput in line3[6]:
        line3 = line3.replace("5", "X")
    elif userinput in line3[10]:
        line3 = line3.replace("6", "X")
    elif userinput in line5[2]:
        line5 = line5.replace("1", "X")
    elif userinput in line5[6]:
        line5 = line5.replace("2", "X")
    elif userinput in line5[10]:
        line5 = line5.replace("3", "X")


def checkboardo():
    ''' Funtion that replaces number on board with O for Player2 '''
    global line1, line2, line3, line4, line5
    if userinput in line1[2]:
        line1 = line1.replace("7", "O")
    elif userinput in line1[6]:
        line1 = line1.replace("8", "O")
    elif userinput in line1[10]:
        line1 = line1.replace("9", "O")
    elif userinput in line3[2]:
        line3 = line3.replace("4", "O")
    elif userinput in line3[6]:
        line3 = line3.replace("5", "O")
    elif userinput in line3[10]:
        line3 = line3.replace("6", "O")
    elif userinput in line5[2]:
        line5 = line5.replace("1", "O")
    elif userinput in line5[6]:
        line5 = line5.replace("2", "O")
    elif userinput in line5[10]:
        line5 = line5.replace("3", "O")


def player1():
    ''' Player1 Function That Checks & Displays Board '''
    global userinput
    userinput = input('Player 1 (X), Please enter number (1-9): ')
    while userinput not in nine or userinput in p1 or userinput in p2:
        userinput = input(
            'Please only enter number not already entered between 1 and 9: ')
    else:
        p1.append(userinput)
        checkboardx()
        printboard()


def player2():
    ''' Player2 Function That Checks & Displays Board '''
    global userinput
    userinput = input('Player 2 (O), Please enter number (1-9): ')
    while userinput not in nine or userinput in p1 or userinput in p2:
        userinput = input(
            'Please only enter number not already entered between 1 and 9: ')
    else:
        p2.append(userinput)
        checkboardo()
        printboard()


def p1condition():
    ''' Function To Check Board For Player1 Win Determination '''
    global wl1, wl2, wl3, wl4, wl5, wl6, wl7, wl8
    if all(item in p1 for item in wl1) or \
        all(item in p1 for item in wl2) or \
        all(item in p1 for item in wl3) or \
        all(item in p1 for item in wl4) or \
        all(item in p1 for item in wl5) or \
        all(item in p1 for item in wl6) or \
        all(item in p1 for item in wl7) or \
            all(item in p1 for item in wl8):
            return True


def p2condition():
    ''' Function To Check Board For Player2 Win Determination '''
    global wl1, wl2, wl3, wl4, wl5, wl6, wl7, wl8
    if all(item in p2 for item in wl1) or \
        all(item in p2 for item in wl2) or \
        all(item in p2 for item in wl3) or \
        all(item in p2 for item in wl4) or \
        all(item in p2 for item in wl5) or \
        all(item in p2 for item in wl6) or \
        all(item in p2 for item in wl7) or \
            all(item in p2 for item in wl8):
            return True

# Program Starts

while True:
    reset()
    p1 = []
    p2 = []
    printboard()

    userinput = input('Player 1 (X), Please enter number (1-9): ')
    while userinput not in nine:
        userinput = input('Please only enter number between 1 and 9: ')
    else:
        p1.append(userinput)
        checkboardx()
        printboard()

    player2()
    player1()
    player2()
    player1()

    if p1condition():
        playagain = ''
        while not (
            playagain == 'n' or playagain == 'N' or
                playagain == 'y' or playagain == 'Y'):
                playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            print('Thanks for playing. Goodbye.')
            break
        elif playagain == 'y' or playagain == 'Y':
            continue

    player2()

    if p2condition():
        playagain = ''
        while not (
            playagain == 'n' or playagain == 'N' or
                playagain == 'y' or playagain == 'Y'):
                playagain = input('Player 2 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            print('Thanks for playing. Goodbye.')
            break
        elif playagain == 'y' or playagain == 'Y':
            continue

    player1()

    if p1condition():
        playagain = ''
        while not (
            playagain == 'n' or playagain == 'N' or
                playagain == 'y' or playagain == 'Y'):
                playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            print('Thanks for playing. Goodbye.')
            break
        elif playagain == 'y' or playagain == 'Y':
            continue

    player2()

    if p2condition():
        playagain = ''
        while not (
            playagain == 'n' or playagain == 'N' or
                playagain == 'y' or playagain == 'Y'):
                playagain = input('Player 2 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            print('Thanks for playing. Goodbye.')
            break
        elif playagain == 'y' or playagain == 'Y':
            continue

    player1()

    if p1condition():
        playagain = ''
        while not (
            playagain == 'n' or playagain == 'N' or
                playagain == 'y' or playagain == 'Y'):
                playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            print('Thanks for playing. Goodbye.')
            break
        elif playagain == 'y' or playagain == 'Y':
            continue
    else:
        playagain = input('Draw Game!, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            print('Thanks for playing. Goodbye.')
            break
        elif playagain == 'y' or playagain == 'Y':
            continue
