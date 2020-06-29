from random import randint, choice
class Dice:
    def __init__(self): 
        pass

    def roll(self):
        # return random tuple between 1 to 6
        return randint(1,6), randint(1,6)


result = Dice()
print(f'Dice value is {result.roll()}')


