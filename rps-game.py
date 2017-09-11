#rock paper scissors game

#introduction to the game
print('')
print(' ======= Welcome to Rock, Paper, and Scissors =======')
print('')
print(' 1) First player is asked first')
print(' 2) Second player is asked second')
print(' 3) The winner is revealed!')
print(' 4) Done? type QUIT')
print('')

while True:
    
    print('')
    print('----------------------')
    player_one = input('Make a move player one > ').strip().lower()
    print('')
    player_two = input('Make a move player two > ').strip().lower()

    #player one
    if player_one == 'rock' and player_two == 'scissors':
        print('')
        print('=== Player one won! ===')
    elif player_one == 'paper' and player_two == 'rock':
        print('')
        print('=== Player one won! ===')
    elif player_one == 'scissors'and player_two == 'paper':
        print('')
        print('=== Player one won! ===')

    #player two
    elif player_two == 'rock' and player_one == 'scissors':
        print('')
        print('=== Player two won! ===')
    elif player_two == 'paper' and player_one == 'rock':
        print('')
        print('=== Player two won! ===')
    elif player_two == 'scissors'and player_one == 'paper':
        print('')
        print('=== Player two won! ===')

    #tie
    elif player_two == 'scissors' and player_one == 'scissors':
        print('')
        print('=== No players win! It is a tie! ===')
    elif player_two == 'paper' and player_one == 'paper':
        print('')
        print('=== No players win! It is a tie! ===')
    elif player_two == 'rock'and player_one == 'rock':
        print('')
        print('=== No players win! It is a tie! ===')

    #quit
    elif player_one == 'QUIT' or player_two == 'QUIT':
        break



