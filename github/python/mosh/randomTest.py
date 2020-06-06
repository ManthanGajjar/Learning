from random import randint

class dice:
    def __init__(self):
        pass

    def roll(self):
        defaultTuple = (randint(10,20), randint(10,20))
        print(defaultTuple)
        pass



dice().roll()
