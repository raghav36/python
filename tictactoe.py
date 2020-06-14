import sys

board = ['-']*9
gameOver = False

while gameOver == False: 
    inputChoice = input("Enter X or 0")
    inputDestination = input("Enter a value between 1 to 9")

    isValidInput = validate_user_input(inputChoice, inputDestination)
    if(isValidInput == False):
        sys.exit()

    inputDestination = int(inputDestination)

    isValidBoardPosition = validate_board_position(board, inputDestination)
    if(isValidBoardPosition == False):
        sys.exit()

    board[inputDestination-1] = inputChoice

    gameOver = check_for_winner(board)

    inputNewGame = input("Do you want to start a new game? (Yes/No)")
    if inputNewGame == 'Yes':
        board = ['-']*9
        gameOver = False
        print("New game started")

def validate_user_ input(inputChoice, inputDestination):
    if not str(inputDestination).isdigit() or int(inputDestination) < 0 or int(inputDestination) > 9:
        print("Invalid destination choice")
        return False        

    if not (str(inputChoice) == '0' or str(inputChoice) == 'X'):
        print("Invalid input choice")
        return False
    
    return True

def validate_board_position(board, inputDestination):
    if board[inputDestination-1] != '-':
        print("Selected position cannot be used")
        return False

    return True

def check_for_winner(board):
    for i in range(0,9):
        if (i == 0 or i == 3 or i == 6) and (board[i] == board[i+1] == board[i+2]) and board[i] != '-':
            print("Winner is " + str(board[i]))
            return True

        if (i == 0 or i == 1 or i == 2) and (board[i] == board[i+3] == board[i+6]) and board[i] != '-' :
            print("Winner is " + str(board[i]))
            return True

    if board[0] == board[4] == board[8] and board[0] != '-':
        print("Winner is " + board[0])
        return True

    if board[2] == board[4] == board[6] and board[2] != '-':
        print("Winner is " + board[2])
        return True
    
    return False