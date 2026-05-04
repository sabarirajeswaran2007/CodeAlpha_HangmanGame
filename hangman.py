import random

stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /     |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\   |
         |
    =========
    """
]

words = ["Uncharted", "ResidentEvil", "TheLastOfUs", "GodOfWar", "SpiderMan"]
life = 6
theword = random.choice(words).upper()

display = ["_"] * len(theword)

print("Welcome to Hangman Game!")
print("In This Game You have to guess the name of the famous AAA games by guessing the letters in it.")
print(" ".join(display))

game_over = False

while not game_over:
    guess = input("Guess a letter: ").upper()

    if guess in display:
        print("You already guessed that letter. Try something new.")
        continue

    found = False

    for position in range(len(theword)):
        if guess == theword[position]:
            display[position] = guess
            found = True

    if found:
        print("Your guess is in the word!!")
    else:
        life -= 1
        print(stages[6 - life])
        print("This letter is not in the word:(")
        print("Lives left:", life)

        if life == 0:
            game_over = True
            print("You lose!!")
            print("The word was:", theword)

    print(" ".join(display))

    if "_" not in display:
        game_over = True
        print("You win!!")
        print("The word was:", theword)
        print("You play games a lot!! Touch the Grassss!!!")