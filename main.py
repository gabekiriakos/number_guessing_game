from game import Game

game = Game()
correct_guess = game.get_random_number()

print("Let's play a game!")
print("Guess a number between 1 and 100:")
input("Press [ENTER] to continue.")

while game.in_game():
    try:
        guess = int(input("What is your guess? "))
    except ValueError:
        game.clear()
        print("Please enter a NUMBER")
        continue

    game.clear()
    if guess != correct_guess:
        game.give_hint(guess)
    else:
        game.guess_correct()

input("Press [ENTER] to exit.")
