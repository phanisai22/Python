""" Tic Tac Toe
    A multi-player game with no AI moves
    Two persons are must to play this game."""

import random
import time


def display_board(board):
    # Print the board.
    # Taking the board of length 10 ignore index 0.

    print("-" * 13)
    print("| " + board[7] + " | " + board[8] + " | " + board[9] + " |")
    print("-" * 13)
    print("| " + board[4] + " | " + board[5] + " | " + board[6] + " |")
    print("-" * 13)
    print("| " + board[1] + " | " + board[2] + " | " + board[3] + " |")
    print("-" * 13)


def set_names():
    # Set the names, each for a player if he wants to.
    # Else go with default name.
    choice = input("YES - Enter player names \n"
                   "Enter key - Go with default names \n").lower()

    if choice == "yes":
        player1_name = input("Enter player1 's name : ")
        player2_name = input("Enter player2 's name : ")
        return player1_name, player2_name

    return "player 1", "player 2"


def choose_first(player1_name, player2_name):
    # A player is selected and returned randomly .

    if random.randint(0, 10) % 2 == 0:
        # Select player 1 if even. Else go for player 2.
        # More randomness ;)
        return "" + player1_name

    return "" + player2_name


def player_input():
    # Take player's marker 'X' or 'O' and return it

    player1_name, player2_name = set_names()
    first_player = choose_first(player1_name, player2_name)

    print(first_player + " will select the marker first !")

    while True:
        marker = input(first_player +
                       " ! Please select a marker "
                       "of your choice X or O - ").upper()
        if marker == 'O' or marker == 'X':
            break

    if first_player == player1_name:
        if marker == 'X':
            return player1_name, player2_name, 'X', 'O'
        else:
            return player1_name, player2_name, 'O', 'X'
    else:
        if marker == 'X':
            return player1_name, player2_name, 'O', 'X'
        else:
            return player1_name, player2_name, 'X', 'O'


def is_empty(board, position):
    # Check if the position on board is empty.
    return board[position] == ' '


def place_marker(board, marker, position):
    # Place the marker and return true.
    # Couldn't place the marker return false.
    # Check if 1 <= position <= 9
    try:
        if is_empty(board, position):
            board[position] = marker
            return True
        return False
    except IndexError or ValueError:
        print("Invalid position! Try (1-9) only.")
        return False


def is_full(board):
    # Check if the board is full and return True is yes. Else return false.
    for i in range(1, 10):
        if is_empty(board, i):
            return False

    return True


def win_check(board, marker):
    # Check if the board has a win sequence
    # win sequences - (1, 2, 3) (4, ,5, 6) (7, 8, 9) - Horizontal
    # (1, 4, 7) (2, 5, 8) (3, 6, 9) - Vertical
    # (3, 5, 7) (1, 5, 9) - Diagonal
    if board[1] == board[2] == board[3] == marker or \
            board[4] == board[5] == board[6] == marker or \
            board[7] == board[8] == board[9] == marker or \
            board[1] == board[4] == board[7] == marker or \
            board[2] == board[5] == board[8] == marker or \
            board[3] == board[6] == board[9] == marker or \
            board[3] == board[5] == board[7] == marker or \
            board[1] == board[5] == board[9] == marker:
        return True

    return False


def quit_game():
    # Ask user if he wants to quit or replay.
    wanna_quit = input("\nWanna quit the game - \nYes for yes - \nEnter key for no : ").lower()
    if wanna_quit == "yes":
        return True

    return False


def wait(t):
    # Making game to wait for better experience ;)
    time.sleep(t)


if __name__ == '__main__':
    # Declare play board
    play_board = [' '] * 10

    print("\n==========Welcome to TIC TAC TOE game==========\n\n")
    wait(2)
    print("Please, use your number pad to play this game\n")
    wait(1)

    # Display the number pad for an idea to user.
    display_board(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    print()

    # Initial credentials like name , marker...
    p1_name, p2_name, p1_marker, p2_marker = \
        player_input()

    # Start the game.
    # Loop will run until player quits the game.
    while True:
        # Choose a random player.
        player = choose_first(p1_name, p2_name)
        wait(1)
        print("\n" + player + " will move first\n")
        ready = input("Ready to play ? \nEnter key for YES -"
                      " \nNo for NO -\n").lower()
        if ready == 'no':
            game_on = False
        else:
            game_on = True

        # GamePlay.
        while game_on:
            if player == p1_name:
                # Player 1 turn.
                display_board(play_board)

                # Check for input errors.
                # Example - Special characters instead of numbers.
                try:
                    position = int(input("\n" + player + " ! Choose a position (1-9) - "))
                    while not place_marker(play_board, p1_marker, position):
                        # Warning message.
                        if 1 <= position <= 9:
                            print("Position taken, Choose another one")
                        position = int(input(player + " ! Choose a position (1-9) - "))
                except ValueError:
                    print("\nOnly numbers please\n")
                    player = p1_name
                    continue

                # Check if player 1 has won the match by this mov.
                # If yes game is over ask for replay,
                # if not continue with player 2' s move.
                if win_check(play_board, p1_marker):
                    display_board(play_board)
                    wait(1)
                    print("----------" + p1_name.upper() + " HAS WON----------")
                    game_on = False
                else:
                    if is_full(play_board):
                        display_board(play_board)
                        wait(1)
                        print("----------TIE GAME!----------")
                        game_on = False
                    else:
                        player = p2_name

            if player == p2_name:
                # Player 2 turn.
                display_board(play_board)

                try:
                    # Check for input errors.
                    # Example - Special characters instead of numbers.
                    position = int(input(player + " ! Choose a position (1-9) - "))
                    while not place_marker(play_board, p2_marker, position):
                        # Warning message
                        if 1 <= position <= 9:
                            print("Position taken, Choose another one")
                            position = int(input(player + " ! Choose a position (1-9) - "))
                except ValueError:
                    print("\nOnly numbers please.\n")
                    player = p2_name
                    continue

                # Check if player 2 has won the match by this mov.
                # If yes game is over ask for replay,
                # if not continue with player 1' s move.
                if win_check(play_board, p2_marker):
                    display_board(play_board)
                    wait(1)
                    print("----------" + p2_name.upper() + " HAS WON----------")
                    game_on = False
                else:
                    if is_full(play_board):
                        display_board(play_board)
                        wait(1)
                        print("----------TIE GAME!----------")
                        game_on = False
                    else:
                        player = p1_name

        # Ask user to play again or quit the game.
        if quit_game():
            break
        else:
            # New game.
            play_board = [' '] * 10

# End of lines.