# Challenge 1.1
# Make a Tic-tac-toe game allowing two players to play against each other.
# Comments are left indicating some of the things that still need to be done, but
# there may be other things you have to code not included in this outline.
# Please look out for errors in the outline, it has not been tested in advance.
# Feel free to modify the outline or expand on the game as you wish, this isnt
# a classroom assignment.  :)


#Period indicates a blank space
board = [
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.']
]

turn = "O"

won = False; #Set to True when a player has won

while (won == False):
    #Switch turn between "X" and "O"
    
    
    #Get user input
    valid_input = false
    while (valid_input = false): #Loop until the user inputs a valid spot
        row = int(input("Input row (0-2): "))
        col = int(input("Input col (0-2): "))
        
        #Check if the user inputted a valid spot, then set valid_input to True

    
    #Update board after input is validated
    board[row][col] = turn

    
    
    #Check if the current player has won
  


    #Print board
    for row in board:
        for col in row:
            print(col + " ", end="")
        print("") #Prints a newline
