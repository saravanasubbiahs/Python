import random

### This is magic_8_ball , used for fortune telling and also for seeking advice.
print("Welcome")


def answer(num):
    if num == 0:
        print("It will happen")
    
    elif num == 1:
        print("No, you may not take that risk.")

    elif num == 2:
        print("yes , but also you can think it for twice , whether you want or not")

    elif num == 3:
        print("Very doubtful")

    elif num == 4:
        print("yes , you can proceed")

    elif num == 5:
        print("No , don't do that")

    elif num == 6:
        print("Yes , but the outcome looks bad")

    elif num == 7:
        print("Yes, definitely")

print("Think of a Yes / No question, and press enter to see the answer given by magic 8 ball")
input()

answer(random.randint(0 , 7))