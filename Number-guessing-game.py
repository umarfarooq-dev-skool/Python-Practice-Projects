import random

number = random.randint(1, 100)
attempts = 5

print("Guess a number between 1 and 100")
print("You have 5 attempts.")

for i in range(attempts):
    try:
        guess = int(input("Enter your guess: "))

        if guess < number:
            print("Too low!")

        elif guess > number:
            print("Too high!")

        else:
            print("Correct!")
            print("You guessed it in", i + 1, "attempts.")
            break

    except ValueError:
        print("Please enter a number.")

else:
    print("Game over!")
    print("The correct number was:", number)