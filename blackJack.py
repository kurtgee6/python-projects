##generate random numbers from 1-21
import random

#Dealer numbers (random)
random_dealer_one = random.randint(1,11)
random_dealer_two = random.randint(1,11)

#Player numbers (random)
random_player_one = int(random.randint(1,11))
random_player_two = int(random.randint(1,11))

##random number
anotherCard = int(random.randint(1,11))
anotherCardTwo = int(random.randint(1,11))

##start game screen
def welcome():
    print('')
    print(""" == LET'S PLAY BLACKJACK! == """)
    print('')

welcome()

##print out the numbers of player
print('Players first card is: ' + str(random_player_one))
print('Players second card is: ' + str(random_player_two))
print("")
print('Dealers first card is: ' + str(random_dealer_one))
print('Dealers second cars is: ?')
print("")

#total of players first two cards
currentPlayerVal = random_player_one + random_player_two

#total of dealers first two cards
currentDealerVal = random_dealer_one + random_dealer_two

def ask_user(player, another, dealer, anotherTwo):

    user_answer = input("Would you like to HIT or STAND? ").lower().strip()

    if user_answer == "hit" and dealer != 21:
        print(currentDealerVal)
        newCurrent = player + another

        if (newCurrent < 17):
            print("Current Total: {}".format(newCurrent))
            next_answer = input("Would you like to HIT or STAND? ").lower().strip()
            if (next_answer == "hit"):
                newCurrent += anotherTwo
    
                if(newCurrent > 21):
                    print("Current Total: {}".format(newCurrent))
                    print('You have lost this round')
                elif(newCurrent == 21):
                    print("Congrats you got 21!")
                    print('Dealer Total: {}'.format(currentDealerVal))
                    print('Player Total: {}'.format(newCurrent))
                elif(newCurrent < 21 and newCurrent > currentDealerVal):
                    print("Congrats you've won this round")
                    print('Dealer Total: {}'.format(currentDealerVal))
                    print('Player Total: {}'.format(newCurrent))

        elif (newCurrent > 17 and newCurrent < 21):
            print("Current Total: {}".format(newCurrent))
            next_answer = input("Would you like to HIT or STAND? ").lower().strip()
            if (next_answer == "hit"):
                print("oompa loompa")

        elif (newCurrent > 21):
            print('')
            print('You have lost this round')
            print('Player Total: {}'.format(newCurrent))
            print('Dealer Total: {}'.format(currentDealerVal))
            print('')

    elif(user_answer == "stand"):
        print('put')


if currentDealerVal == 21 and currentDealerVal != currentPlayerVal:
    print('Dealer Won. Dealer Total: {}'.format(currentDealerVal))
    print('')
elif currentPlayerVal == 21 and currentDealerVal != currentPlayerVal:
    print('Player Won. Player Total: {}'.format(currentPlayerVal))
    print('')
else:
    ask_user(currentPlayerVal, anotherCard, currentDealerVal ,anotherCardTwo)


