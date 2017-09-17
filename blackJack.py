#generate random numbers from 1-21
import random

random_number_one = random.randint(1,21)
random_number_two = random.randint(1,21)

#There must be a dealer and a player

player = input('Would you like to HIT or STAY? ')

if player == 'HIT':
    if random_number_one + random_number_two == 21:
        print("Your first card is: " + str(random_number_two))
        print("Your second card is: " + str(random_number_one))
        print("Congrats, you've beat the DEALER")
    elif random_number_one + random_number_two < 17:
        print("Your first card is: " + str(random_number_two))
        print("Your second card is: " + str(random_number_one))
        player
    elif random_number_one + random_number_two > 17:
        print("Your first card is: " + str(random_number_two))
        print("Your second card is: " + str(random_number_one))
        print("Sorry, the DEALER won this round.")



#both are given two random numbers
#if the PLAYESs number is greater than the DEALERS number
#the player wins
#there will be two COMMANDS...a HIT and a STAND
