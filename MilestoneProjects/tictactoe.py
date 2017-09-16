nine = ['1', '2', '3', '4', '5' ,'6', '7', '8', '9']

# Winning Lists:
wl1 = ['1', '2', '3']
wl2 = ['4', '5', '6']
wl3 = ['7', '8', '9']
wl4 = ['1', '4', '7']
wl5 = ['2', '5', '8']
wl6 = ['3', '6', '9']
wl7 = ['1', '5', '9']
wl8 = ['3', '5', '7']

line1 = '| 7 | 8 | 9 |'
line2 = ' --- --- --- '
line3 = '| 4 | 5 | 6 |'
line4 = ' --- --- --- '
line5 = '| 1 | 2 | 3 |'


def printboard():
    global line1,line2,line3,line4,line5
    print('\n',line1,'\n',line2,'\n',line3,'\n',line4,'\n',line5,'\n')

def reset():    
    global line1,line2,line3,line4,line5
    line1 = '| 7 | 8 | 9 |'
    line2 = ' --- --- --- '
    line3 = '| 4 | 5 | 6 |'
    line4 = ' --- --- --- '
    line5 = '| 1 | 2 | 3 |'

def checkboardx():
    global line1,line2,line3,line4,line5
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
    global line1,line2,line3,line4,line5
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
    global userinput
    userinput = input('Player 1 (X), Please enter number (1-9): ')
    while userinput not in nine or userinput in p1 or userinput in p2:
        userinput = input('Please only enter number not already entered between 1 and 9: ')
    else:
        p1.append(userinput)
        checkboardx()
        printboard()

def player2():
    global userinput
    userinput = input('Player 2 (O), Please enter number (1-9): ')
    while userinput not in nine or userinput in p1 or userinput in p2:
        userinput = input('Please only enter number not already entered between 1 and 9: ')
    else:
        p2.append(userinput)
        checkboardo()
        printboard()


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

    if all(item in p1 for item in wl1) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain =='N':
            break
        elif playagain == 'y' or playagain =='Y':
            continue
    elif all(item in p1 for item in wl2) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':         
            continue
    elif all(item in p1 for item in wl3) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            continue
    elif all(item in p1 for item in wl4) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            continue
    elif all(item in p1 for item in wl5) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            continue
    elif all(item in p1 for item in wl6) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            continue
    elif all(item in p1 for item in wl7) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            continue
    elif all(item in p1 for item in wl8) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            continue
        
    player2()

    if all(item in p2 for item in wl1) == True:
        playagain = input('Player 2 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain =='N':
            break
        elif playagain == 'y' or playagain =='Y':
            continue
    elif all(item in p2 for item in wl2) == True:
        playagain = input('Player 2 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':          
            continue
    elif all(item in p2 for item in wl3) == True:
        playagain = input('Player 2 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            continue
    elif all(item in p2 for item in wl4) == True:
        playagain = input('Player 2 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            continue
    elif all(item in p2 for item in wl5) == True:
        playagain = input('Player 2 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            continue
    elif all(item in p2 for item in wl6) == True:
        playagain = input('Player 2 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            continue
    elif all(item in p2 for item in wl7) == True:
        playagain = input('Player 2 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            continue
    elif all(item in p2 for item in wl8) == True:
        playagain = input('Player 2 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            continue
        
    player1()

    if all(item in p1 for item in wl1) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain =='N':
            break
        elif playagain == 'y' or playagain =='Y':
            continue
    elif all(item in p1 for item in wl2) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            p1 = []
            p2 = []          
            continue
    elif all(item in p1 for item in wl3) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            p1 = []
            p2 = []
            continue
    elif all(item in p1 for item in wl4) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            continue
    elif all(item in p1 for item in wl5) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            continue
    elif all(item in p1 for item in wl6) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            continue
    elif all(item in p1 for item in wl7) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            continue
    elif all(item in p1 for item in wl8) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            continue

    player2()

    if all(item in p2 for item in wl1) == True:
        playagain = input('Player 2 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain =='N':
            break
        elif playagain == 'y' or playagain =='Y':
            continue
    elif all(item in p2 for item in wl2) == True:
        playagain = input('Player 2 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':          
            continue
    elif all(item in p2 for item in wl3) == True:
        playagain = input('Player 2 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            continue
    elif all(item in p2 for item in wl4) == True:
        playagain = input('Player 2 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            continue
    elif all(item in p2 for item in wl5) == True:
        playagain = input('Player 2 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            continue
    elif all(item in p2 for item in wl6) == True:
        playagain = input('Player 2 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            continue
    elif all(item in p2 for item in wl7) == True:
        playagain = input('Player 2 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            continue
    elif all(item in p2 for item in wl8) == True:
        playagain = input('Player 2 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            continue

    player1()

    if all(item in p1 for item in wl1) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain =='N':
            break
        elif playagain == 'y' or playagain =='Y':
            continue
    elif all(item in p1 for item in wl2) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':          
            continue
    elif all(item in p1 for item in wl3) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            continue
    elif all(item in p1 for item in wl4) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            continue
    elif all(item in p1 for item in wl5) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            continue
    elif all(item in p1 for item in wl6) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            continue
    elif all(item in p1 for item in wl7) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            continue
    elif all(item in p1 for item in wl8) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            continue
    else:
        playagain = input('Draw Game!, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            continue
