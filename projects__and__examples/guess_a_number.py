## This is a Guess a number (game). Here just play and have fun with your guessings.

# importing random module.
import random

# printing the initial statements.
print("I have thought a number between 1 to 10, can you guess the number?")


# assigning a random value as my guess 
guess = random.randint(1,10)

for my_guess in range(1,5):
    
    print("Take a guess")
    your_guess = int(input("Enter a number that you guess as a correct one"))

    if your_guess > guess:
        print("Your guess is higher than my number")

    elif your_guess < guess:
        print("your guess is lower that my guess")

    else:
        break

if your_guess == guess:
    print("Great you found out my number at " +str(my_guess)+ "Guesses" )

else:
    print(" No , The number i thought is " + str(guess))
