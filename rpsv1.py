print('rock...')
print('paper...')
print('scissors...')

player1 = input('player 1 ,make your move ')#prompts input from the user and assigns it to player one variable
player2 = input('player 2 ,make your move ') #prompts input from the user and assigns it to the player two variable

if player1 == 'rock' and player2 == 'scissors':
    print('player1 wins')
elif player1 == 'rock' and player2 == 'paper':
    print('player2 wins')   
elif player1 == 'paper' and player2 == 'rock':
    print("player1 wins")
elif player1 == 'paper' and player2 == 'scissors':
    print('player2 wins')   
elif player1 =='scissors' and player2 == 'rock':
    print("player2 wins")  
elif player1 == 'scissors' and player2 == 'paper':
    print('player1 wins')      





elif player1 == player2:
    print("it's a tie")    
else:
    print("something went wrong")    