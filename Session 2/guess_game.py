import random

def guess_number():
    guess_num = random.randint(0, 20)
    for round in range(0, 10):
        print "Guess the number:"
        user_num = int(raw_input())

        if user_num == guess_num:
            print "Congratulations! You guessed it! on round {}".format(round) 
        elif user_num > guess_num:
            print "The number was too big"
        elif user_num < guess_num:
            print "The number was too small"
        else: 
            print "There was an error somewhere"

guess_number()
