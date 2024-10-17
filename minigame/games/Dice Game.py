#dice game
import random
dice0= random.randint(2,12)
def roll_dice():
    print("Welcome to the Dice Game!")
    print(f"I will roll two dice. If the sum of the two dice is {dice0}, you win!")
    print("Let's roll the dice...")

    while True:
        input("Press Enter to roll the dice...")
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2

        print(f"Dice 1: {dice1}")
        print(f"Dice 2: {dice2}")
        print(f"Total: {total}")

        if total == dice0:
            print("Congratulations! You win!")
            break
        else:
            print("Sorry, try again.")
            print("\n")

roll_dice()
