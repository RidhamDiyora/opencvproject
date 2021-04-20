import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"choose a number between 1 to {x} "))

        if guess < random_number:
           print("too low!")
        elif guess > random_number:
           print("too high!")

    print(f"congratulations you guessed {random_number} correctly.")

guess(5)
