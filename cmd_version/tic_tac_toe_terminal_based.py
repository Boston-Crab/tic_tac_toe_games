""" -------------------------------------------------- """
""" >>>> Tic-Tac-Toe Text Based Terminal/Cmd Game <<<< """
""" -------------------------------------------------- """

"""
-> Current game match state tracking.
"""
g_board_values_list = []
for i in range(9):
    g_board_values_list.append(" ")
g_player_1 = ""
g_player_2 = ""


def board_print(board):
    """
    -> Board state printing 
    """
    i = board
    print(f"▲▲▲▲▲▲▲▲▲▲▲▲▲")
    print(f"| {i[6]} | {i[7]} | {i[8]} |")
    print(f"|7--|8--|9--|")
    print(f"| {i[3]} | {i[4]} | {i[5]} |")
    print(f"|4--|5--|6--|")
    print(f"| {i[0]} | {i[1]} | {i[2]} |")
    print(f"|1--|2--|3--|")


def how_to_play():
    """
    -> Initial game instructions.
    """
    print("These are the controls of the game.\nEach number represents a spot on a board." +
          "\n type numbers 1 to 9 to select where to place X or O during your turn.")
    board_print(g_board_values_list)


def set_up():
    """
    -> Taking in player 1 and 2 names.
    """
    global g_player_1, g_player_2
    print("---- This is a Tic Tac Toe game ----")
    how_to_play()
    g_player_1 = input("Tell me who will be playing as X?\n")
    g_player_2 = input("Tell me who will be playing as O?\n")


def players_input(is_it_x_or_o, player_name):
    """
    -> Requesting player input for X/O placement location.
    -> Checking if it's a digit from 1 to 9.
    """
    while True:
        i = input(
            f"{player_name.title()} where would you like to place {is_it_x_or_o}?\n")

        if (not i.isdigit()) or (int(i) not in range(1, 10)):
            print("Wrong input. Please only numbers 1-9")
        elif (g_board_values_list[int(i)-1] == " "):
            g_board_values_list[int(i)-1] = is_it_x_or_o
            break
        else:
            print("This spot is already taken. Lets try again.")
            continue


def game_victory_checking(is_it_x_or_o, player_name):
    """
    -> Checking if someone has won the match.
    -> Printing winning players name.
    """
    global g_game_loop
    i = g_board_values_list
    k = is_it_x_or_o
    if (i[0] == k and i[1] == k and i[2] == k) or (i[0] == k and i[3] == k and i[6] == k) or (i[6] == k and i[7] == k and i[8] == k):
        g_game_loop = False
    elif (i[3] == k and i[4] == k and i[5] == k) or (i[1] == k and i[4] == k and i[7] == k) or (i[2] == k and i[5] == k and i[8] == k):
        g_game_loop = False
    elif (i[0] == k and i[4] == k and i[8] == k) or (i[2] == k and i[4] == k and i[6] == k):
        g_game_loop = False
    if g_game_loop == False:
        print(f"{is_it_x_or_o} wins!\nGood job {player_name}.")
    no_winner_checking()


def no_winner_checking():
    """
    -> Checking if a game match is a draw.
    """
    global g_game_loop
    if " " not in g_board_values_list:
        print("Looks like it's a draw.")
        g_game_loop = False


def play_again():
    """
    -> Handling new game match start or exiting of the game, depending on user input.
    """
    global g_main_program_loop, g_board_values_list
    while True:
        play_again_prompt = input("Would you like to play again? Y/N\n> ")
        if play_again_prompt.lower() == "n":
            g_main_program_loop = False
            break
        # clears the board and restarts the game:
        elif play_again_prompt.lower() == "y":
            g_board_values_list.clear()
            for i in range(9):
                g_board_values_list.append(" ")
            break
        else:
            print("Wrong input. Try again.")

""" ----------------------------------------------- """
""" >>>>>>>>>>>>> Main Game/App Loop: <<<<<<<<<<<<< """
""" ----------------------------------------------- """
g_main_program_loop = True
while g_main_program_loop == True:
    set_up()
    g_game_loop = True
    while g_game_loop == True:
        # X turn handling:
        players_input("X", g_player_1)
        board_print(g_board_values_list)
        game_victory_checking("X", g_player_1)
        if g_game_loop == False:
            break
        # --- End ---
        # O turn handling:
        players_input("O", g_player_2)
        board_print(g_board_values_list)
        game_victory_checking("O", g_player_2)
        if g_game_loop == False:
            break
        # --- End ---
    # Match aftermath handling:
    play_again()
    if g_main_program_loop == False:
        break
