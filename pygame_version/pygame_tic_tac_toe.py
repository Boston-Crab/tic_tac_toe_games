"""
-----------------------------------------------
>>>> Tic-Tac-Toe Pygame-Library Based Game <<<<
-----------------------------------------------
"""

# ttt stands for Tic Tac Toe
import sys
import pygame
from assets_loading import load_images, load_sounds


pygame.init()

# A list for checking the state of the game:
board_values_list = [" "] * 9

# Setting the desired size of the screen:
screen_width = 600
screen_height = 600
# Making a game screen window:
screen = pygame.display.set_mode((screen_width, screen_height))
# pygame window name:
pygame.display.set_caption("Tic Tac Toe")

# Load assets
images = load_images()
sounds = load_sounds()

# Accessing images and rects from the loaded assets
main_board_image, rect_board = images["main_board_image"]
x_wins_image, rect_x_wins_image = images["x_wins_image"]
o_wins_image, rect_o_wins_image = images["o_wins_image"]
no_winner_image, rect_no_winner_image = images["no_winner_image"]
x_image_scaled, rect_x = images["x_image_scaled"]
o_image_scaled, rect_o = images["o_image_scaled"]
main_menu, rect_main_menu = images["main_menu"]  # Access rect_main_menu
resume = images["resume"]
resume_hovered = images["resume_hovered"]
new_game = images["new_game"]
new_game_hovered = images["new_game_hovered"]
about_image = images["about_image"]
about_image_hovered = images["about_image_hovered"]
quit_image = images["quit_image"]
quit_image_hovered = images["quit_image_hovered"]
pepe_newgame_1 = images["pepe_newgame_1"]
pepe_about_1 = images["pepe_about_1"]
pepe_quit_1 = images["pepe_quit_1"]
pepe_waiting_1 = images["pepe_waiting_1"]
x_turn_announcment, rect_x_turn_announcment = images["x_turn_announcment"]
o_turn_announcment, rect_o_turn_announcment = images["o_turn_announcment"]

# Accessing sounds from the loaded assets
bg_music = sounds["bg_music"]
winning_sound = sounds["winning_sound"]
no_winner_sound = sounds["no_winner_sound"]
figure_placement_sound = sounds["figure_placement_sound"]


def blitme_updating_the_state_of_a_game(
    player, which_player_scaled, which_player_rect, ttt_game_state_list
):
    # Following if statements determine board places by numpad numbers 1-9.
    # Every if stament checks if a mouse click was in the correct place of a
    # screen
    global is_ttt_board_spot_taken
    # >>>>> Tests: <<<<<
    # square_size = 64
    # column_index = (pos[0] - board_top_left_corner_x) // square_size
    # row_index = (pos[1] - board_top_left_corner_y) // square_size
    # board_field_idx = (row_index * 3) + column_index

    # ttt board size is 360x360
    # one square size is 120x120
    # ---------------
    one_ttt_board_sqaure_size = 120
    # x_game_window_start = 0  # left window corner
    # y_game_window_start = 0  # left window corner
    # ---------------
    x_window_0 = 120  # thats where the ttt board starts
    y_window_0 = 120  # thats where the ttt board starts
    # ---------------
    # x_ttt_board_0 = 0
    # y_ttt_board_0 = 0
    x_ttt_board_1 = 360
    y_ttt_board_1 = 360
    # ---------------
    x_window_1 = x_window_0 + x_ttt_board_1  # 480 in total
    y_window_1 = y_window_0 + y_ttt_board_1  # 480 in total
    x_in_board_coordinate_system = pos[0] - x_window_0
    y_in_board_coordinate_system = pos[1] - y_window_0
    colum_index = x_in_board_coordinate_system // one_ttt_board_sqaure_size
    row_index = y_in_board_coordinate_system // one_ttt_board_sqaure_size
    board_field_index = (row_index * 3) + colum_index
    print(board_field_index)

    if pos[0] in range(x_window_0, x_window_1) and pos[1] in range(
        y_window_0, y_window_1
    ):
        # Checking if that spot is taken:
        if " " not in ttt_game_state_list[board_field_index]:
            print("The spot is already taken. Try again.")
            is_ttt_board_spot_taken = True
        else:
            # Telling where to place images of X or O:
            which_player_rect.x = x_window_0 + (one_ttt_board_sqaure_size *
                                                colum_index)
            which_player_rect.y = y_window_0 + (one_ttt_board_sqaure_size *
                                                row_index)
            # Updating the state of the game:
            ttt_game_state_list[board_field_index] = player
            # Printing the image
            screen.blit(which_player_scaled, which_player_rect)
    return
    # >>>>> Tests End. <<<<<


def game_victory_checking(is_it_x_or_o, player_name, ttt_game_state_list):
    global g_ttt_game_loop, g_match_outcome_end_screen
    i = ttt_game_state_list
    k = is_it_x_or_o
    if (
        (i[0] == k and i[1] == k and i[2] == k)
        or (i[0] == k and i[3] == k and i[6] == k)
        or (i[6] == k and i[7] == k and i[8] == k)
    ):
        g_ttt_game_loop = False
    elif (
        (i[3] == k and i[4] == k and i[5] == k)
        or (i[1] == k and i[4] == k and i[7] == k)
        or (i[2] == k and i[5] == k and i[8] == k)
    ):
        g_ttt_game_loop = False
    elif (i[0] == k and i[4] == k and i[8] == k) or (
        i[2] == k and i[4] == k and i[6] == k
    ):
        g_ttt_game_loop = False
    if g_ttt_game_loop is False:
        print(f"{is_it_x_or_o} wins!\nGood job {player_name}.")
        g_match_outcome_end_screen = True


def no_winner_checking(ttt_game_state_list):
    global g_ttt_game_loop, g_match_outcome_end_screen
    if " " not in ttt_game_state_list:
        print("Looks like it's a draw.")
        screen.blit(no_winner_image, rect_no_winner_image)
        g_ttt_game_loop = False
        reseting_win_conditions(ttt_game_state_list)
        pygame.mixer.Channel(2).play(pygame.mixer.Sound(no_winner_sound))
        g_match_outcome_end_screen = True


def reseting_win_conditions(ttt_game_state_list):
    # Resets board values list for a new game:
    ttt_game_state_list.clear()
    for i in range(9):
        ttt_game_state_list.append(" ")


def main_menu_blit():
    screen.blit(main_menu, rect_main_menu)
    screen.blit(new_game, (145, 188))
    screen.blit(about_image, (210, 266))
    screen.blit(quit_image, (230, 331))
    screen.blit(pepe_waiting_1, (4, 441))


def clean_up_after_match_finalisation(
    winner_image, winner_image_rect, ttt_game_state_list
):
    screen.blit(winner_image, winner_image_rect)
    reseting_win_conditions(ttt_game_state_list)
    pygame.mixer.Channel(0).pause()
    pygame.mixer.Channel(1).play(pygame.mixer.Sound(winning_sound))


def blitme_whose_turn_it_is():
    if player_turn_switching is True:
        screen.blit(x_turn_announcment, (211, 35))
    else:
        screen.blit(o_turn_announcment, (211, 35))


def hovering_effect(mouse_postion):
    mp = mouse_postion
    if mp[0] in range(145, 443) and mp[1] in range(188, 267):
        screen.blit(new_game_hovered, (145, 188))
        screen.blit(pepe_newgame_1, (4, 441))
    elif mp[0] in range(210, 381) and mp[1] in range(266, 331):
        screen.blit(about_image_hovered, (210, 266))
        screen.blit(pepe_about_1, (4, 441))
    elif mp[0] in range(230, 354) and mp[1] in range(331, 403):
        screen.blit(quit_image_hovered, (230, 331))
        screen.blit(pepe_quit_1, (4, 441))


def main_menu_pygame_events(mouse_postion):
    global g_ttt_game_loop
    mp = mouse_postion
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Press ESC to close the game window:
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        # Deciding what happens after any mouse button click:
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the position of the mouse click:
            if mp[0] in range(145, 443) and mp[1] in range(188, 267):
                g_ttt_game_loop = True
                break
            elif mp[0] in range(230, 354) and mp[1] in range(331, 403):
                pygame.quit()
                sys.exit()
            elif mp[0] in range(210, 381) and mp[1] in range(266, 331):
                print("Not Finished Feature")


def match_end_screen_waiting_for_a_mouse_click():
    global g_ttt_game_loop, g_match_outcome_end_screen
    pygame.mixer.music.pause()
    pygame.mixer.Channel(0).pause()
    while g_match_outcome_end_screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Press ESC to close the game window:
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                g_ttt_game_loop = True
                pygame.mixer.Channel(1).pause()
                pygame.mixer.Channel(2).pause()
                g_match_outcome_end_screen = False
                break


main_program_loop = True
g_ttt_game_loop = True
# X and O turn switching. |True is X|False is O|:
player_turn_switching = True

# The main game loop
while main_program_loop:
    # pygame.mixer.music.play(-1)

    # >>>>>>>>>>>>>>> Start of - main menu feature: <<<<<<<<<<<<<<<<
    main_menu_blit()
    pos_0 = pygame.mouse.get_pos()
    hovering_effect(pos_0)
    g_ttt_game_loop = False
    main_menu_pygame_events(pos_0)
    # End. ---------------------------------------------------------

    pygame.display.flip()

    # >>>>>>>>>>>> Start of - tic tac toe game feature: <<<<<<<<<<<<
    # The main game board image:
    screen.blit(main_menu, rect_main_menu)
    screen.blit(main_board_image, rect_board)
    player_turn_switching = True
    # Tic Tac Toe loop:
    g_match_outcome_end_screen = False
    while g_ttt_game_loop:
        blitme_whose_turn_it_is()
        # To handle events happening in a pygame window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Press ESC to close the game window:
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            # Deciding what happens after any mouse button click:
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get the position of the mouse click:
                pos = pygame.mouse.get_pos()
                # Redraw after each mouse click:
                # X turn:
                if player_turn_switching is True:
                    is_ttt_board_spot_taken = False
                    blitme_updating_the_state_of_a_game(
                        "X", x_image_scaled, rect_x, board_values_list
                    )
                    game_victory_checking("X", "Player1", board_values_list)
                    if g_ttt_game_loop is False:
                        clean_up_after_match_finalisation(
                            x_wins_image, rect_x_wins_image, board_values_list
                        )
                    no_winner_checking(board_values_list)
                    # Checking if X was placed in the available empty spot,
                    # play the sound and switch the turn:
                    if is_ttt_board_spot_taken is False:
                        pygame.mixer.Channel(0).play(
                            pygame.mixer.Sound(figure_placement_sound)
                        )
                        player_turn_switching = False
                # O turn:
                elif player_turn_switching is False:
                    is_ttt_board_spot_taken = False
                    blitme_updating_the_state_of_a_game(
                        "O", o_image_scaled, rect_o, board_values_list
                    )
                    game_victory_checking("O", "Player2", board_values_list)
                    if g_ttt_game_loop is False:
                        clean_up_after_match_finalisation(
                            o_wins_image, rect_o_wins_image, board_values_list
                        )
                    no_winner_checking(board_values_list)
                    # Checking if O was placed in the available empty spot,
                    # play the sound and switch the turn:
                    if is_ttt_board_spot_taken is False:
                        pygame.mixer.Channel(0).play(
                            pygame.mixer.Sound(figure_placement_sound)
                        )
                        player_turn_switching = True

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    match_end_screen_waiting_for_a_mouse_click()
