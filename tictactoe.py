import sys

board = ['-']*9
gameOver = False

while gameOver == False: 
    #user input for X or 0
    inputChoice = input("Enter X or 0")

    #user input for board position
    inputDestination = input("Enter a value between 1 to 9")

    #validate user input
    isValidInput = validate_user_input(inputChoice, inputDestination)
    if(isValidInput == False):
        sys.exit()

    inputDestination = int(inputDestination)

    #check if board position is available
    isValidBoardPosition = validate_board_position(board, inputDestination)
    if(isValidBoardPosition == False):
        sys.exit()

    board[inputDestination-1] = inputChoice

    #game is over if there is a winner or a tie
    gameOver = check_for_winner(board) or check_for_tie(board)

    inputNewGame = input("Do you want to start a new game? (Yes/No)")
    if inputNewGame == 'Yes':
        board = ['-']*9
        gameOver = False
        print("New game started")

def validate_user_ input(inputChoice, inputDestination):
    #check if valid input destination
    if not str(inputDestination).isdigit() or int(inputDestination) < 0 or int(inputDestination) > 9:
        print("Invalid destination choice")
        return False        

    #check if valid input choice
    if not (str(inputChoice) == '0' or str(inputChoice) == 'X'):
        print("Invalid input choice")
        return False
    
    return True

def validate_board_position(board, inputDestination):
    #check if inputDestination is already filled
    if board[inputDestination-1] != '-':
        print("Selected position cannot be used")
        return False

    return True

def check_for_winner(board):
    for i in range(0,9):
        #check rows combination
        if (i == 0 or i == 3 or i == 6) and (board[i] == board[i+1] == board[i+2]) and board[i] != '-':
            print("Winner is " + str(board[i]))
            return True
        #check columns combination
        if (i == 0 or i == 1 or i == 2) and (board[i] == board[i+3] == board[i+6]) and board[i] != '-' :
            print("Winner is " + str(board[i]))
            return True

    #check diagonal combination
    if board[0] == board[4] == board[8] and board[0] != '-':
        print("Winner is " + board[0])
        return True

    if board[2] == board[4] == board[6] and board[2] != '-':
        print("Winner is " + board[2])
        return True

    return False

def check_for_tie(board):
    #check if any empty position is present
    return '-' in set(board)
