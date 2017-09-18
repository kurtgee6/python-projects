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
print(random_dealer_two)
print("")

#total of players first two cards
currentPlayerVal = random_player_one + random_player_two

#total of dealers first two cards
currentDealerVal = random_dealer_one + random_dealer_two

def ask_user(player, another, dealer, anotherTwo):

    user_answer = input("Would you like to HIT or STAND? ").lower().strip()

    if user_answer == "hit" and dealer != 21:
        newCurrent = player + another

        if (newCurrent < 17):
            
            print('')
            print("Current Total: {}".format(newCurrent))
            next_answer = input("Would you like to HIT or STAND? ").lower().strip()
            print('')
            
            if (next_answer == "hit"):
                newCurrent += anotherTwo
    
                if(newCurrent > 21):
                    
                    print('')
                    print("Current Total: {}".format(newCurrent))
                    print('You have lost this round')
                    print('')
                    return
                
                elif(newCurrent == 21):
                    
                    print('')
                    print("Congrats you got 21!")
                    print('Player Total: {}'.format(newCurrent))
                    print('Dealer Total: {}'.format(dealer))
                    print('')
                    return
                
                elif(newCurrent < 21 and newCurrent > dealer):
                    
                    print('')
                    print("Congrats you've won this round")
                    print('Player Total: {}'.format(newCurrent))
                    print('Dealer Total: {}'.format(dealer))
                    print('')
                        
            elif next_answer == "stand":
                if (newCurrent > dealer and newCurrent < 21):
                    print('')
                    print('You have won this round')
                    print('Player Total: {}'.format(newCurrent))
                    print('Dealer Total: {}'.format(dealer))
                    print('')
                    return
            
                elif (newCurrent < dealer and dealer < 21 ):
                    print('')
                    print('Dealer won this round')
                    print('Player Total: {}'.format(newCurrent))
                    print('Dealer Total: {}'.format(dealer))
                    print('')
                    return

        elif (newCurrent > 17 and newCurrent < 21):
            print("Current Total: {}".format(newCurrent))
            next_answer = input("Would you like to HIT or STAND? ").lower().strip()
            if (next_answer == "hit"):
                newNewCurrent += newCurrent
                if (newNewCurrent > 21 or newNewCurrent < dealer):
                    print('')
                    print('You have lost this round')
                    print('Player Total: {}'.format(newNewCurrent))
                    print('Dealer Total: {}'.format(dealer))
                    print('')
                elif (newNewCurrent < 21 and newNewCurrent > dealer):
                    print('')
                    print('You have won this round')
                    print('Player Total: {}'.format(newNewCurrent))
                    print('Dealer Total: {}'.format(dealer))
                    print('')
            elif (next_answer == "stand"):
                if (newNewCurrent > dealer and newNewCurrent < 21):
                    print('')
                    print('You have won this round')
                    print('Player Total: {}'.format(newNewCurrent))
                    print('Dealer Total: {}'.format(dealer))
                    print('')
                    return
        
                elif (newNewCurrent < dealer and newNewCurrent < 21 ):
                    print('')
                    print('Dealer won this round')
                    print('Player Total: {}'.format(newNewCurrent))
                    print('Dealer Total: {}'.format(dealer))
                    print('')
                    return

        elif (newCurrent > 21):
            print('')
            print('You have lost this round')
            print('Player Total: {}'.format(newCurrent))
            print('Dealer Total: {}'.format(dealer))
            print('')
            return

    elif(user_answer == "stand"):
        if (player > dealer and player < 21):
            print('')
            print('You have won this round')
            print('Player Total: {}'.format(player))
            print('Dealer Total: {}'.format(dealer))
            print('')
            return
        
        elif (player < dealer and dealer < 21 ):
            print('')
            print('Dealer won this round')
            print('Player Total: {}'.format(player))
            print('Dealer Total: {}'.format(dealer))
            print('')
            return

if currentDealerVal == 21 and currentDealerVal != currentPlayerVal:
    print('Dealer Won. Dealer Total: {}'.format(currentDealerVal))
    print('')
elif currentPlayerVal == 21 and currentDealerVal != currentPlayerVal:
    print('Player Won. Player Total: {}'.format(currentPlayerVal))
    print('')
else:
    ask_user(currentPlayerVal, anotherCard, currentDealerVal ,anotherCardTwo)



#stand after the first hit
