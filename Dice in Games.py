from random import *
class Dice:
    def __init__(self, sides):
        self.sides = sides
    def roll_dice(self):
        return randint(1, self.sides)
a = Dice(6)
print(a.roll_dice())
