import magic
from random import randint

class Game():

    #new game init generate random number
    def __init__(self):
        self.randomNum = randint(1,10)
     
    def prompt(self):
        guess = input("Please select magic number: ")
        return guess

    def check_win(self, guess):
        if (self.randomNum == guess):
            print("Wow.Congratulations, You won the game !")
            return
        else:
            print("Sorry..Wrong Numberm, random number for this game was {}").format(self.randomNum)
            print("\nPlease try again !")
            return


