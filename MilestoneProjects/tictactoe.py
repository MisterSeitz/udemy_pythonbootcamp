p1 = []
p2 = []

# Winning Lists:
wl1 = ['1', '2', '3']
wl2 = ['4', '5', '6']
wl3 = ['7', '8', '9']
wl4 = ['1', '4', '7']
wl5 = ['2', '5', '8']
wl6 = ['3', '6', '9']
wl7 = ['1', '5', '9']
wl8 = ['3', '5', '7']

line1 = '| 1 | 2 | 3 |'
line2 = ' --- --- --- '
line3 = '| 4 | 5 | 6 |'
line4 = ' --- --- --- '
line5 = '| 7 | 8 | 9 |'

def printboard():
    global line1,line2,line3,line4,line5
    print('\n',line1,'\n',line2,'\n',line3,'\n',line4,'\n',line5,'\n')

def checkboardx():
    global line1,line2,line3,line4,line5
    if userinput in line1[2]:
        line1 = line1.replace("1", "X")
    elif userinput in line1[6]:
        line1 = line1.replace("2", "X")
    elif userinput in line1[10]:
        line1 = line1.replace("3", "X")
    elif userinput in line3[2]:
        line3 = line3.replace("4", "X")
    elif userinput in line3[6]:
        line3 = line3.replace("5", "X")
    elif userinput in line3[10]:
        line3 = line3.replace("6", "X")
    elif userinput in line5[2]:
        line5 = line5.replace("7", "X")
    elif userinput in line5[6]:
        line5 = line5.replace("8", "X")
    elif userinput in line5[10]:
        line5 = line5.replace("9", "X")
        
def checkboardo():
    global line1,line2,line3,line4,line5
    if userinput in line1[2]:
        line1 = line1.replace("1", "O")
    elif userinput in line1[6]:
        line1 = line1.replace("2", "O")
    elif userinput in line1[10]:
        line1 = line1.replace("3", "O")
    elif userinput in line3[2]:
        line3 = line3.replace("4", "O")
    elif userinput in line3[6]:
        line3 = line3.replace("5", "O")
    elif userinput in line3[10]:
        line3 = line3.replace("6", "O")
    elif userinput in line5[2]:
        line5 = line5.replace("7", "O")
    elif userinput in line5[6]:
        line5 = line5.replace("8", "O")
    elif userinput in line5[10]:
        line5 = line5.replace("9", "O")

game = 'ongoing'

while game == 'ongoing':
    print('startloop')
    printboard()
    userinput = input('Player 1 (X), Please enter number (1-9): ')
    p1.append(userinput)
    checkboardx()
    printboard()

    userinput = input('Player 2 (O), Please enter number (1-9): ')
    if userinput in p1:
    p2.append(userinput)
    checkboardo()
    printboard()

    userinput = input('Player 1 (X), Please enter number (1-9): ')
    p1.append(userinput)
    checkboardx()
    printboard()

    userinput = input('Player 2 (O), Please enter number (1-9): ')
    p2.append(userinput)
    checkboardo()
    printboard()

    userinput = input('Player 1 (X), Please enter number (1-9): ')
    p1.append(userinput)
    checkboardx()
    printboard()

    if all(item in p1 for item in wl1) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain =='N':
            break
        elif playagain == 'y' or playagain =='Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'
            continue
    elif all(item in p1 for item in wl2) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'           
            continue
    elif all(item in p1 for item in wl3) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'
            continue
    elif all(item in p1 for item in wl4) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'
            continue
    elif all(item in p1 for item in wl5) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'
            continue
    elif all(item in p1 for item in wl6) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'
            continue
    elif all(item in p1 for item in wl7) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'
            continue
    elif all(item in p1 for item in wl8) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'
            continue
        
    userinput = input('Player 2 (O), Please enter number (1-9): ')
    p2.append(userinput)
    checkboardo()
    printboard()

    if all(item in p2 for item in wl1) == True:
        playagain = input('Player 2 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain =='N':
            break
        elif playagain == 'y' or playagain =='Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'
            continue
    elif all(item in p2 for item in wl2) == True:
        playagain = input('Player 2 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'          
            continue
    elif all(item in p2 for item in wl3) == True:
        playagain = input('Player 2 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'
            continue
    elif all(item in p2 for item in wl4) == True:
        playagain = input('Player 2 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'
            continue
    elif all(item in p2 for item in wl5) == True:
        playagain = input('Player 2 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'
            continue
    elif all(item in p2 for item in wl6) == True:
        playagain = input('Player 2 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'
            continue
    elif all(item in p2 for item in wl7) == True:
        playagain = input('Player 2 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'
            continue
    elif all(item in p2 for item in wl8) == True:
        playagain = input('Player 2 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'
            continue
        
    userinput = input('Player 1 (X), Please enter number (1-9): ')
    p1.append(userinput)
    checkboardx()
    printboard()

    if all(item in p1 for item in wl1) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain =='N':
            break
        elif playagain == 'y' or playagain =='Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'
            continue
    elif all(item in p1 for item in wl2) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'          
            continue
    elif all(item in p1 for item in wl3) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'
            continue
    elif all(item in p1 for item in wl4) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'
            continue
    elif all(item in p1 for item in wl5) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'
            continue
    elif all(item in p1 for item in wl6) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'
            continue
    elif all(item in p1 for item in wl7) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'
            continue
    elif all(item in p1 for item in wl8) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'
            continue

    userinput = input('Player 2 (O), Please enter number (1-9): ')
    p2.append(userinput)
    checkboardo()
    printboard()

    if all(item in p2 for item in wl1) == True:
        playagain = input('Player 2 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain =='N':
            break
        elif playagain == 'y' or playagain =='Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'
            continue
    elif all(item in p2 for item in wl2) == True:
        playagain = input('Player 2 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'          
            continue
    elif all(item in p2 for item in wl3) == True:
        playagain = input('Player 2 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'
            continue
    elif all(item in p2 for item in wl4) == True:
        playagain = input('Player 2 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'
            continue
    elif all(item in p2 for item in wl5) == True:
        playagain = input('Player 2 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'
            continue
    elif all(item in p2 for item in wl6) == True:
        playagain = input('Player 2 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'
            continue
    elif all(item in p2 for item in wl7) == True:
        playagain = input('Player 2 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'
            continue
    elif all(item in p2 for item in wl8) == True:
        playagain = input('Player 2 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'
            continue

    userinput = input('Player 1 (X), Please enter number (1-9): ')
    p1.append(userinput)
    checkboardx()
    printboard()

    if all(item in p1 for item in wl1) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain =='N':
            break
        elif playagain == 'y' or playagain =='Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'
            continue
    elif all(item in p1 for item in wl2) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'           
            continue
    elif all(item in p1 for item in wl3) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'
            continue
    elif all(item in p1 for item in wl4) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'
            continue
    elif all(item in p1 for item in wl5) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'
            continue
    elif all(item in p1 for item in wl6) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'
            continue
    elif all(item in p1 for item in wl7) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'
            continue
    elif all(item in p1 for item in wl8) == True:
        playagain = input('Player 1 Wins, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'
            continue
    else:
        playagain = input('Draw Game!, Play Again (Y/N)? ')
        if playagain == 'n' or playagain == 'N':
            break
        elif playagain == 'y' or playagain == 'Y':
            p1 = []
            p2 = []
            line1 = '| 1 | 2 | 3 |'
            line2 = ' --- --- --- '
            line3 = '| 4 | 5 | 6 |'
            line4 = ' --- --- --- '
            line5 = '| 7 | 8 | 9 |'
            continue
