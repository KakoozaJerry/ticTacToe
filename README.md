# TIC-TAC-TOE
This is a simple Tic Tac Toe Game to allow only 2 players to complete the board either with an 'X'
or a 'O'.

## Instructions
When promted whose turn is next,the player can input either top-L,top-M,top-R,mid-L,mid-M,mid-R,low-L,low-M,low-R depending on where they wish to place their 'X' or 'O'.

## How the Code Works
They dictionary value in theBoard array places the 'X' or  'O' in the appropriate position.

I used a simple if function to switch prompts when whichever player's turn is next.

## How to get the game running on your machine locally
- Ensure you have python version 3 installed on your computer .
- Clone this repository to your local machine.
- Navigate using your terminal into the folder containing the cloned repository.
- Run the TicTacToe.py file within the terminal by typing `python TicTacToe.py` 
- Each player is now given turns to play their move.
- However this game does not double check to determine when a player has won.