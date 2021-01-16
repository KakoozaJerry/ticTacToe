theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
turn = 'X'
for i in range(9):
    printBoard(theBoard)
# PROMPTS THE PLAYER WHOSE TURN IS NEXT
    print('Turn for ' + turn + '. Move on which space?')
# THE PLAYER CAN INPUT EITHER top-L,top-M,top-R,mid-L,mid-M,mid-R,low-L,low-M,low-R depending on where they 
# wish to place their X or 0
    move = input()
#They dictionary value in theBoard array places the X or  O in the appropriate position
    theBoard[move] = turn
#The if function double prompts when whichever player's turn is next
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)
