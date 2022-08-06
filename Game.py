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

    def give_hint(self, answer):
        self.guess_wrong()
        if self.random_number > answer:
            print("Hint: The number is greater than {}" .format(answer))
        else:
            print("Hint: The number is less than {}" .format(answer))

    def guess_wrong(self):
        print("Wrong! Try again!")
        if self.score != 0:
            self.score -= 1

    def guess_correct(self):
        self.is_playing_game = False
        print("Correct! The number was {}." .format(self.random_number))
        print("Your score is {}" .format(self.score))
        print("Thank you for playing!")
    
    def clear(self):
        if name == 'nt':
            _ = system('cls') # windows
        else:
            _ = system('clear') # linux, mac

if __name__ == '__main__':

    game = Game()
    random_num = game.get_random_number()

    print("Let's play a game!")
    print("Guess a number between 1 and 100:")
    input("Press [ENTER] to continue.")

    while game.in_game():
        try:
            answer = int(input("What is your answer? "))
        except ValueError:
            game.clear()
            print("Please enter a NUMBER")
            continue

        game.clear()
        if answer != random_num:
            game.give_hint(answer)
        else:
            game.guess_correct()

    input("Press [ENTER] to exit.")