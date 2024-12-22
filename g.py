import random

bot = random.randrange(1,6)
print("guess a number from one to five\nyou have three guesses")
for i in range (3):
    print(f"Try {i+1}")
    user=int(input())

    if user == bot :
        print("you won")
        break

    else:

        if  i < 2:  # Check if it's not the last attempt
            pass
        else:
            print("You lose! The correct number was", bot)

















