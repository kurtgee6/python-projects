#generate random numbers from 1-21
import random

#Dealer numbers (random)
random_dealer_one = random.randint(1,11)
random_dealer_two = random.randint(1,11)

#Player numbers (random)
random_player_one = int(random.randint(1,11))
random_player_two = int(random.randint(1,11))

#random number
addNum = int(random.randint(1,11))

#start game screen
def welcome():
    print('')
    print(""" == LET'S PLAY BLACKJACK! == """)
    print('')

welcome()

#print out the numbers of player


print('Your first card is: ' + str(random_player_one))
print('Your second card is: ' + str(random_player_two))

currentPlayerVal = random_player_one + random_player_two


user_answer = input("Would you like to HIT or STAND? ").lower().strip()

def ask_user(a, value, random):
    if a == "hit":
        numberRightNow = value + random
        print(numberRightNow)
        if numberRightNow > 21:
            print("Dealer Wins")
    elif a == "stand":
        print('stand')

#calling back the function
ask_user(user_answer, currentPlayerVal, addNum)
