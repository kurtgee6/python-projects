#generate a random number between 1 and 9 (includes 1 and 9)
#Ask the user to guess the number
#Tell whether the user was too high or too low or if they got it right

import random

random_number = random.randint(1, 50)

number_guesses = 0

print('')
print(''' -- GUESS THE NUMBER THAT I'M THINKING OF BETWEEN 1-50 -- ''')
print('I will tell you if you are too high, too low, or just right')
print('Remember...you only have five guesses!')
print('')

while number_guesses < 5:
    
    user_input = int(input("Try to guess my number > "))
    
    if user_input < random_number:
        print('')
        print("You gotta go higher than that buddy.")
        number_guesses+= 1
        print('')
        print('Your guesses: {} '.format(number_guesses))
        print('')

    
    elif user_input > random_number:
        print('')
        print("Woah...too high! Way too high!!")
        number_guesses+= 1
        print('')
        print('Your guesses: {} '.format(number_guesses))
        print('')

    else:
        print('')
        print("Great! You got it.")
        print('')
        break


    #extra stuff
#Keep track of how many guesses the user has
#Keep going until user types exit
























