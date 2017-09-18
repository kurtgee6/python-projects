
#DISCLAIMER: This is the first time I've ever written in Python, I've heard that python is a very friendly language to code with and wanted to try for myself. Here is an attempt I've made to create my own blackjack game for python practices. Although most of the game logic isn't finished, it's still a solid game that runs smoothly.

    #My GOAL for this game was to learn how to use functions and pass paramaters inside the functions. I feel that I've completed my goal but still want to challenge myself even more by adding other features like double down, push, the value of the ace and more of the dealers logic.

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
anotherCardTwo = int(random.randint(1,11))
anotherCardThree = int(random.randint(1,11))

#welcome function
def welcome():
    print('')
    print(""" == LET'S PLAY BLACKJACK! == """)
    print('')

#start of game screen
welcome()

#print out the numbers of player
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

#passing parameters inside the function
def ask_user(player, another, dealer, anotherTwo, anotherThree):
    
    #createed variable for user input
    user_answer = input("Would you like to HIT or STAND? ").lower().strip()
    
    #if user types hit...do this
    if user_answer == "hit" and dealer != 21:
        newCurrent = player + another
        
        #checking to see if users value right now is less than 17
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
                    return
                        
            elif next_answer == "stand":
                newCurrent += anotherTwo

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

        #checking to see if users value right now is between 17 and 21
        elif (newCurrent > 17 and newCurrent < 21):
            
            print("Current Total: {}".format(newCurrent))
            next_answer = input("Would you like to HIT or STAND? ").lower().strip()
            
            if (next_answer == "hit"):
                
                newCurrent += anotherThree
                
                if (newCurrent > 21 or newCurrent < dealer):
                    print('')
                    print('You have lost this round')
                    print('Player Total: {}'.format(newCurrent))
                    print('Dealer Total: {}'.format(dealer))
                    print('')
                    return
                
                elif (newCurrent < 21 and newCurrent > dealer):
                    print('')
                    print('You have won this round')
                    print('Player Total: {}'.format(newCurrent))
                    print('Dealer Total: {}'.format(dealer))
                    print('')
                    return
        
            elif (next_answer == "stand"):
                
                if (newCurrent > dealer and newCurrent < 21):
                    print('')
                    print('You have won this round')
                    print('Player Total: {}'.format(newCurrent))
                    print('Dealer Total: {}'.format(dealer))
                    print('')
                    return
        
                elif (newCurrent > 21 ):
                    print('')
                    print('Dealer won this round')
                    print('Player Total: {}'.format(newCurrent))
                    print('Dealer Total: {}'.format(dealer))
                    print('')
                    return

        #checking to see if users value right now is more than 21
        elif (newCurrent > 21):
            print('')
            print('You have lost this round')
            print('Player Total: {}'.format(newCurrent))
            print('Dealer Total: {}'.format(dealer))
            print('')
            return

    #if user types stand...do this
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

#main game function
def game ():
    if currentDealerVal == 21 and currentDealerVal != currentPlayerVal:
        print('Dealer Won. Dealer Total: {}'.format(currentDealerVal))
        print('')
    elif currentPlayerVal == 21 and currentDealerVal != currentPlayerVal:
        print('Player Won. Player Total: {}'.format(currentPlayerVal))
        print('')
    else:
        ask_user(currentPlayerVal, anotherCard, currentDealerVal ,anotherCardTwo, anotherCardThree)

#start game
game()
