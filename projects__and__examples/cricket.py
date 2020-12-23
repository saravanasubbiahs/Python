import random
import sys

out = True

while out == True:
    toss = input("Enter you choice between batting or bowling \n")

    computer = random.randint(1,5)

    run =0
    
    if toss == 'batting':   
        cho = True
        score = 0
        while cho == True:
            print("Enter numbers between 1 to 5")
            inp = input()
            try:
                if int(inp) < 6:
                    if int(inp) == computer:
                        print("you are Out with a score of " + str(score) + ' runs')
                        break
                    else:
                        score = score + int(inp)
                else:
                    print("Enter a valid number between 1 to 5")
                     
            except ValueError:
                print("Enter a valid number between 1 to 5")
                cho = True
        if run > 0:        
            if score > run:
                print("You have won the game")
    else:
        print("start bowling")
        print("Enter numbers between 1 to 5")
        bowl = True
        run = 0

        while bowl == True:
                    
            man_put = input()
            rand_bowl = random.randint(1,5)
            
            if rand_bowl == int(man_put):
                
                print("you have to score " + str(run + 1)+ " to win")
                break 

            else:
                run = run + rand_bowl
                print("run till now", run)
