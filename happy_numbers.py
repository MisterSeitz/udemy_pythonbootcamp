def squaresum(x):
    x = str(x)
    y = []
    for i in x:
        i = int(i)
        i = i**2
        y.append(i)
    return sum(y)
    
while True:
    unhappycycle = [4, 16, 37, 58, 89, 145, 42, 20, 4]
    x = input("Please insert a number to see if it's a happy number: ")
    try:
        y = squaresum(x)
        while y != 1:
            if y in unhappycycle:
                print('{} is not a happy number'.format(x))
                break
            else:
                y = squaresum(y)
                continue
            
        else:
            print('{} is a happy number'.format(x))
            continue
        
    
    except (TypeError, ValueError):
        print('Please insert number only!')
        continue

          
