x = 1

while x == 1:
    string = input("Please enter word to see pig latin form or Q to quit: ")
    if string == "q" or string == "Q":
        break
    letter1 = string[0]
    letter1join = letter1 + "ay"
    letter2 = string[1:]
    pig_latin = letter2 + letter1join
    pig_latin = pig_latin.lower()
    pig_latin = pig_latin[0].upper() + pig_latin[1:]
    print(pig_latin)
