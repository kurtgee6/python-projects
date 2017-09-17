#generate random numbers from 1-21
import random

#Dealer numbers (random)
random_dealer_one = random.randint(1,11)
random_dealer_two = random.randint(1,11)

#Player numbers (random)
random_player_one = int(random.randint(1,11))
random_player_two = int(random.randint(1,11))

#random number
anotherCard = int(random.randint(1,11))

#start game screen
def welcome():
    print('')
    print(""" == LET'S PLAY BLACKJACK! == """)
    print('')

welcome()

#print out the numbers of player


print('Players first card is: ' + str(random_player_one))
print('Players second card is: ' + str(random_player_two))
print("")
print('Dealers first card is: ' + str(random_dealer_one))
print('Dealers second cars is: ?')
print("")

currentPlayerVal = random_player_one + random_player_two
currentDealerVal = random_dealer_one + random_dealer_two

user_answer = input("Would you like to HIT or STAND? ").lower().strip()
print('')


def ask_user(a, value, random):
    if a == "hit":
        numberRightNow = value + random
        print(numberRightNow)
        if numberRightNow > 21:
            print("Dealer Wins")
        elif numberRightNow == 21:
            print("You've won the round")
    elif a == "stand":
        if currentPlayerVal > currentDealerVal:
            print("You won the round. The Dealer had a total of: {}".format(currentDealerVal))
        elif currentPlayerVal == currentDealerVal:
            print('Push')
        elif currentPlayerVal < currentDealerVal:
            print('You have lost the round. The Dealer had a total of: {}'.format(currentDealerVal))


#calling back the function
ask_user(user_answer, currentPlayerVal, anotherCard)
