# first try by yourself.
# you can then reserach on internet.

#rock
#paper
#scissor
import random

print("\nWelcome to 'rock' , 'paper' , 'scissor' game.")


for i in range(3):
    ans = input("Enter you choice :\n")
    values = ['rock' , 'paper' , 'scissor']
    #print(random.choice(values))
    val = random.choice(values)
    print(val)
    
    if ans in values:

        if ans == val:
            continue
        elif ans == 'rock':
            if val == 'paper':
                print("you lose")
            else:
                print("you win")

        elif ans == 'paper':
            if val == 'scissor':
                print('you lose')
            else:
                print("you win")

        else:
            if val == 'rock':
                print('You lose')
            else:
                print("you win")
    else:
        print("enter a correct choice. ")