import random

def guess_number():
    number = random.randint(1, 100)  # Random number between 1 and 100
    attempts = 0

    print("🎲 Welcome to Guess the Number!")
    print("I have chosen a number between 1 and 100. Try to guess it!")

    while True:
        guess = input("Enter your guess: ")

        # check if input is number
        if not guess.isdigit():
            print("❌ Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number:
            print("📉 Too low! Try again.")
        elif guess > number:
            print("📈 Too high! Try again.")
        else:
            print(f"✅ Congratulations! You guessed it in {attempts} tries.")
            break

guess_number()
