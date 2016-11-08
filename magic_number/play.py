import game

#create game instance
new_game = game.Game()

#prompt for input
guess = new_game.prompt()
#check if corrent number
new_game.check_win(guess)