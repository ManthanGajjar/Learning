luckyNumber = 9
defaultChance = 0
totalChance = 3
while (defaultChance < totalChance):
    enterdNumber = int(input('Guess number: '))
    if(enterdNumber == luckyNumber):
        print("your guess is right !!! ")
        break
    defaultChance += 1
    print("No it's wrong guess :(")
else:
    print("Opps, you lose :(")
