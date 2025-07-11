import random

def number_guessing_game():
    print("🎮 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    
    # Generate random number between 1-100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts}. Enter your guess: "))
            
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100!")
                continue
                
            attempts += 1
            
            if guess == secret_number:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts!")
                return
            elif guess < secret_number:
                print("⬆️ Too low! Try a higher number.")
            else:
                print("⬇️ Too high! Try a lower number.")
                
        except ValueError:
            print("⚠️ Please enter a valid number!")
    
    print(f"\nGame over! The number was {secret_number}.")
    print("Better luck next time!")

# Start the game
number_guessing_game()