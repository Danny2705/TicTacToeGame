board = ["-1-", "|", "-2-", "|", "-3-",
         "-4-", "|", "-5-", "|", "-6-",
         "-7-", "|", "-8-", "|", "-9-"]


def board_game():
    print(f"{board[0]} {board[1]} {board[2]} {board[3]} {board[4]}\n"
          f"{board[5]} {board[6]} {board[7]} {board[8]} {board[9]}\n"
          f"{board[10]} {board[11]} {board[12]} {board[13]} {board[14]}")


def player_x():
    valid_number = False
    while not valid_number:
        number_input = input("\nPlayer X. Please enter the number to play: ")
        dictionary = {
            "1": 0,
            "2": 2,
            "3": 4,
            "4": 5,
            "5": 7,
            "6": 9,
            "7": 10,
            "8": 12,
            "9": 14,
        }
        if number_input in dictionary:
            valid_number = True
            index = dictionary[number_input]
            board[index] = "-X-"
            board_game()
        else:
            print("Please enter a valid number in the board game!")


def player_o():
    valid_number = False
    while not valid_number:
        number_input = input("\nPlayer O. Please enter the number to play: ")
        dictionary = {
            "1": 0,
            "2": 2,
            "3": 4,
            "4": 5,
            "5": 7,
            "6": 9,
            "7": 10,
            "8": 12,
            "9": 14,
        }
        if number_input in dictionary:
            valid_number = True
            index = dictionary[number_input]
            board[index] = "-O-"
            board_game()
        else:
            print("Please enter a valid number in the board game!")


def check_game():
    row1 = [board[0], board[2], board[4]]
    row2 = [board[5], board[7], board[9]]
    row3 = [board[10], board[12], board[14]]
    col1 = [board[0], board[5], board[10]]
    col2 = [board[2], board[7], board[12]]
    col3 = [board[4], board[9], board[14]]
    dia1 = [board[0], board[7], board[14]]
    dia2 = [board[4], board[7], board[10]]

    maps = [row1, row2, row3, col1, col2, col3, dia1, dia2]

    for checking in maps:
        if checking == ["-X-", "-X-", "-X-"]:
            return True
        if checking == ["-O-", "-O-", "-O-"]:
            return True


def main():
    print("Welcome to Tic Tac Toe Game!!!\n")
    while True:
        option = input("Enter number:\n"
                       "1: To Start The Game\n"
                       "2: To Play Again\n"
                       "3: To Exit The Game\n"
                       "--> ")
        if option == "2":
            global board
            board = ["-1-", "|", "-2-", "|", "-3-",
                     "-4-", "|", "-5-", "|", "-6-",
                     "-7-", "|", "-8-", "|", "-9-"]
        elif option == "3":
            break

        board_game()
        move_count = 0
        while True:
            player_x()
            move_count += 1
            if check_game():
                print("Congratulations! Player X wins this game.")
                break
            if move_count == 9:
                print("Wow, this game is a draw.")
                break

            player_o()
            move_count += 1
            if check_game():
                print("Congratulations! Player O wins this game.")
                break
            if move_count == 9:
                print("Wow, this game is a draw.")
                break

        print("The game is over! \n")


main()
