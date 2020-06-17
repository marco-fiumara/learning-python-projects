# Function to print game board
def print_board():
    print('---------')
    print("|", ' '.join(game_board[0:3]), "|")
    print("|", ' '.join(game_board[3:6]), "|")
    print("|", ' '.join(game_board[6:9]), "|")
    print('---------')
# Function to process user input. I did it as a function so i could easily call it
# if input was incorrect


def user_input():
    # List of all possbile coordinates to compare user input against
    coordinates = ["1 3", "2 3", "3 3", "1 2",
                   "2 2", "3 2", "1 1", "2 1", "3 1"]
    # User input stage
    user_turn = input("Enter the coordinates:")

    if user_turn.replace(' ', '').isdecimal() == False:
        print("You should enter numbers!")
        user_input()  # recalled function so it would start again
    elif user_turn not in coordinates:
        print("Coordinates should be from 1 to 3!")
        user_input()
    elif game_board[coordinates.index(user_turn)] != "_":
        print("This cell is occupied! Choose another one!")
        user_input()
    elif user_turn in coordinates:
        del game_board[coordinates.index(user_turn)]
        game_board.insert(coordinates.index(user_turn), "X")
        print_board()


game_board = list(input("Enter cells:").upper())
print_board()
user_input()
