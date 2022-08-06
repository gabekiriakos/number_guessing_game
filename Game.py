import random
from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls') # windows
    else:
        _ = system('clear') # linux, mac

class Game:
    # constructor
    def __init__(self):
        self.score = 10
        self.is_playing_game = True

    def in_game(self):
        return self.is_playing_game

    def guess_wrong(self):
        input("Wrong! Press [ENTER] to try again!")
        if self.score != 0:
            self.score -= 1
        else:
            pass # allows null return w/o error

    def guess_correct(self):
        self.is_playing_game = False
        print("Correct! Your score is {}" .format(self.score))

if __name__ == '__main__':

    game = Game()
    random_num = random.randint(1, 10)
    print("Let's play a game!")
    print("Guess a number between 1 and 10:")
    input("Press [ENTER] to continue.")

    while game.in_game():
        try:
            answer = int(input("What is your answer? "))
        except ValueError:
            clear()
            print("Please enter a NUMBER")
            continue
        if answer != random_num:
            clear()
            game.guess_wrong()
        else:
            clear()
            game.guess_correct()

    input("Press [ENTER] to exit.")