import random
from os import system, name

class Game:
    # constructor
    def __init__(self):
        self.score = 10
        self.is_playing_game = True
        self.random_number = random.randint(1, 100)

    def in_game(self):
        return self.is_playing_game

    def get_random_number(self):
        return self.random_number

    def give_hint(self, selection):
        self.guess_wrong()
        if self.random_number > selection:
            print(f"Hint: The number is greater than {selection}")
        else:
            print(f"Hint: The number is less than {selection}")

    def guess_wrong(self):
        print("Wrong! Try again!")
        if self.score != 0:
            self.score -= 1

    def guess_correct(self):
        self.is_playing_game = False
        print(f"Correct! The number was {self.random_number}.")
        print(f"Your score is {self.score}")
        print("Thank you for playing!")

    def clear(self):
        if name == 'nt':
            _ = system('cls') # windows
        else:
            _ = system('clear') # linux, mac
