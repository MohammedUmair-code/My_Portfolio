
def madlib():
    noun = input("Enter a Noun: ")
    adjective = input("Enter an adjective: ")
    adverb = input("Enter an adverb: ")

    para = f"This is a {noun}. \
        It was a/an {adjective} place. \
    We were enjoying the place {adverb}"

    print(para)

# madlib()

import random
def guess_number(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Enter Your Guess between 1 and {x}: "))
        if guess < random_number:
            print("Oops! Try Again. The guess is too low.")
        if guess > random_number:
            print("Oops! Try Again. The guess is too high.")
    print(f"Yay!! Congrats. You have guessed the number {random_number} correctly")
    

#guess_number(10)


def computer_guess(val):
    minRange = 1
    maxRange = val
    feedback = ''
    excluded = 0


    while feedback != 'c':
        if minRange == maxRange:
            guess_number = minRange  # Could also be maxRange because minRange = maxRange
        else:
            guess_number = random.randint(minRange, maxRange)
           
        while guess_number == excluded:
            guess_number = random.randint(minRange, maxRange) 
        print(f"My guess is {guess_number}")

        feedback = input("Is the guess high(H), low(L) or correct(C) : ").lower()
        if feedback == 'h':
            maxRange = guess_number - 1 
            excluded = guess_number
            print("Oops Sorry! Let me try again!!")
        elif feedback == 'l':
            minRange = guess_number + 1 
            excluded = guess_number
            print("Oops Sorry! Let me try again!!")

    print(f"Claps for me for my accomplishment of guessing the right number {guess_number}")


computer_guess(15)
        





