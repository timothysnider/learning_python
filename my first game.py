highest = 10
answer = 7
guess = input("Guess a number from 0 to %d:" % highest)
while (int(guess) != answer):
    if (int(guess) < answer):
        print("answer is higher")
    else:
        print("answer is lower")
    guess = input("Guess a number from 0 to %d:" % highest)
input("you are a winner!!!!")

