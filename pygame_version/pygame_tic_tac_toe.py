#ttt stands for Tic Tac Toe
import sys
import pygame

pygame.init()

#A list for checking the state of the game:
board_values_list = []
for i in range(9):
    board_values_list.append(" ")

#Setting the desired size of the screen:
screen_width = 600
screen_height = 600
#Making a game screen window:
screen = pygame.display.set_mode((screen_width, screen_height))
#pygame window name:
pygame.display.set_caption("Tic Tac Toe")

#Sounds:
pygame.mixer.music.load('images/bg_sound.mp3')
pygame.mixer.music.set_volume(0.5)
winning_sound = pygame.mixer.Sound('images/winning_sound.mp3')
no_winner_sound = pygame.mixer.Sound('images/no_winner_sound.mp3')
figure_placement_sound = pygame.mixer.Sound('images/placement_sound.wav')
winning_sound.set_volume(0.7)
no_winner_sound.set_volume(1)

#>>>>>>>>>>>>>>>>>>>>>>> Images: <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#Loading main board and getting its pixel size:
main_board_image = pygame.image.load('images/board.png')
rect_board = main_board_image.get_rect()
#Loading X and O winning, no winner screens images and geting pixel sizes:
x_wins_image = pygame.image.load('images/board_x_wins.png')
rect_x_wins_image = x_wins_image.get_rect() 
o_wins_image = pygame.image.load('images/board_o_wins.png')
rect_o_wins_image = o_wins_image.get_rect()
no_winner_image = pygame.image.load('images/board_no_winner.png')
rect_no_winner_image = no_winner_image.get_rect()
#Loading images for X and O:
x_image = pygame.image.load('images/X_trans.png')
o_image = pygame.image.load('images/zero_trans.png')
#Information about desired pixel size of X and O images:
x_and_o_new_image_size = (118, 118)
#Setting new pixel size of X and O images:
x_image_scaled = pygame.transform.scale(x_image, x_and_o_new_image_size)
o_image_scaled = pygame.transform.scale(o_image, x_and_o_new_image_size)
#Getting the pixel size of X and O images:
rect_x = x_image_scaled.get_rect()
rect_o = o_image_scaled.get_rect()
#Loading all main menu images:
main_menu = pygame.image.load('images/main_menu.png')
resume = pygame.image.load('images/resume.png')
resume_hovered = pygame.image.load('images/resume_hovered.png')
new_game = pygame.image.load('images/new_game.png')
new_game_hovered = pygame.image.load('images/new_game_hovered.png')
about_image = pygame.image.load('images/about.png')
about_image_hovered = pygame.image.load('images/about_hovered.png')
quit_image = pygame.image.load('images/quit.png')
quit_image_hovered = pygame.image.load('images/quit_hovered.png')
pepe_newgame_1 = pygame.image.load('images/pepe_newgame_1.png')
pepe_about_1 = pygame.image.load('images/pepe_about_1.png')
pepe_quit_1 = pygame.image.load('images/pepe_quit_1.png')
pepe_waiting_1 = pygame.image.load('images/pepe_waiting_1.png')
#All main menu images rects:
rect_main_menu = main_menu.get_rect()
rect_resume = resume.get_rect()
rect_resume_hovered = resume_hovered.get_rect()
rect_new_game = new_game.get_rect()
rect_new_game_hovered = new_game_hovered.get_rect()
rect_about_image = about_image.get_rect()
rect_about_image_hovered = about_image_hovered.get_rect()
rect_quit_image = quit_image.get_rect()
rect_quit_image_hovered = quit_image_hovered.get_rect()
#Whose turn images and rects:
x_turn_announcment = pygame.image.load('images/x_turn_announcment.png')
rect_x_turn_announcment = x_turn_announcment.get_rect()
o_turn_announcment = pygame.image.load('images/o_turn_announcment.png')
rect_o_turn_announcment = o_turn_announcment.get_rect()

def blitme_updating_the_state_of_a_game(player, which_player_scaled, which_player_rect, ttt_game_state_list):  
    #Following if statements determine board places by numpad numbers 1-9.
    #Every if stament checks if a mouse click was in the correct place of a screen
    global is_ttt_board_spot_taken
    #>>>>> Tests: <<<<<
    #square_size = 64
    #column_index = (pos[0] - board_top_left_corner_x) // square_size
	#row_index = (pos[1] - board_top_left_corner_y) // square_size
	#board_field_idx = (row_index * 3) + column_index

    #ttt board size is 360x360
    #one square size is 120x120
    #---------------
    one_ttt_board_sqaure_size = 120
    x_game_window_start = 0 #left window corner
    y_game_window_start = 0 #left window corner
    #---------------
    x_window_0 = 120 #thats where the ttt board starts
    y_window_0 = 120 #thats where the ttt board starts
    #---------------
    x_ttt_board_0 = 0
    y_ttt_board_0 = 0
    x_ttt_board_1 = 360
    y_ttt_board_1 = 360
    #---------------
    x_window_1 = x_window_0 + x_ttt_board_1 #480 in total
    y_window_1 = y_window_0 + y_ttt_board_1 #480 in total
    x_in_board_coordinate_system = (pos[0] - x_window_0)
    y_in_board_coordinate_system = (pos[1] - y_window_0)
    colum_index = x_in_board_coordinate_system // one_ttt_board_sqaure_size
    row_index = y_in_board_coordinate_system // one_ttt_board_sqaure_size
    board_field_index = (row_index * 3) + colum_index
    print(board_field_index)


    if pos[0] in range(x_window_0, x_window_1) and pos[1] in range(y_window_0, y_window_1):
        #Checking if that spot is taken:
        if " " not in ttt_game_state_list[board_field_index]:
            print("The spot is already taken. Try again.")
            is_ttt_board_spot_taken = True
        else:
            #Telling where to place images of X or O:
            which_player_rect.x = x_window_0 + (one_ttt_board_sqaure_size * colum_index)
            which_player_rect.y = y_window_0 + (one_ttt_board_sqaure_size * row_index)
            #Updating the state of the game:
            ttt_game_state_list[board_field_index] = player
            #Printing the image
            screen.blit(which_player_scaled, which_player_rect)
    return
    #>>>>> Tests End. <<<<<

    if pos[0] in range(120, 238) and pos[1] in range(361,479):
        #Checking if that spot is taken:
        if " " not in ttt_game_state_list[0]:
            print("The spot is already taken. Try again.")
            is_ttt_board_spot_taken = True
        else:
            #Telling where to place images of X or O:
            which_player_rect.x = 120
            which_player_rect.y = 361
            #Updating the state of the game:
            ttt_game_state_list[0] = player
            #Printing the image
            screen.blit(which_player_scaled, which_player_rect)
    elif pos[0] in range(241, 358) and pos[1] in range(361,479):
        if " " not in ttt_game_state_list[1]:
            print("The spot is already taken. Try again.")
            is_ttt_board_spot_taken = True
        else:
            which_player_rect.x = 241
            which_player_rect.y = 361
            ttt_game_state_list[1] = player
            screen.blit(which_player_scaled, which_player_rect)
    elif pos[0] in range(361, 479) and pos[1] in range(361,479):
        if " " not in ttt_game_state_list[2]:
            print("The spot is already taken. Try again.")
            is_ttt_board_spot_taken = True
        else:
            which_player_rect.x = 361
            which_player_rect.y = 361
            ttt_game_state_list[2] = player
            screen.blit(which_player_scaled, which_player_rect)
    elif pos[0] in range(120, 238) and pos[1] in range(241, 358):
        if " " not in ttt_game_state_list[3]:
            print("The spot is already taken. Try again.")
            is_ttt_board_spot_taken = True
        else:
            which_player_rect.x = 120
            which_player_rect.y = 241
            ttt_game_state_list[3] = player
            screen.blit(which_player_scaled, which_player_rect)
    elif pos[0] in range(241, 358) and pos[1] in range(241, 358):
        if " " not in ttt_game_state_list[4]:
            print("The spot is already taken. Try again.")
            is_ttt_board_spot_taken = True
        else:
            which_player_rect.x = 241
            which_player_rect.y = 241
            ttt_game_state_list[4] = player
            screen.blit(which_player_scaled, which_player_rect)
    elif pos[0] in range(361, 479) and pos[1] in range(241, 358):
        if " " not in ttt_game_state_list[5]:
            print("The spot is already taken. Try again.")
            is_ttt_board_spot_taken = True
        else:
            which_player_rect.x = 361
            which_player_rect.y = 241
            ttt_game_state_list[5] = player
            screen.blit(which_player_scaled, which_player_rect)
    elif pos[0] in range(120, 238) and pos[1] in range(120, 238):
        if " " not in ttt_game_state_list[6]:
            print("The spot is already taken. Try again.")
            is_ttt_board_spot_taken = True
        else:
            which_player_rect.x = 120
            which_player_rect.y = 120
            ttt_game_state_list[6] = player
            screen.blit(which_player_scaled, which_player_rect)
    elif pos[0] in range(241, 358) and pos[1] in range(120,238):
        if " " not in ttt_game_state_list[7]:
            print("The spot is already taken. Try again.")
            is_ttt_board_spot_taken = True
        else:
            which_player_rect.x = 241
            which_player_rect.y = 120
            ttt_game_state_list[7] = player
            screen.blit(which_player_scaled, which_player_rect)
    elif pos[0] in range(361, 479) and pos[1] in range(120, 238):
        if " " not in ttt_game_state_list[8]:
            print("The spot is already taken. Try again.")
            is_ttt_board_spot_taken = True
        else:
            which_player_rect.x = 361
            which_player_rect.y = 120
            ttt_game_state_list[8] = player
            screen.blit(which_player_scaled, which_player_rect)
    else:
        is_ttt_board_spot_taken = True

def game_victory_checking(is_it_x_or_o, player_name, ttt_game_state_list):
    global g_ttt_game_loop, g_match_outcome_end_screen
    i = ttt_game_state_list
    k = is_it_x_or_o
    if (i[0] == k and i[1] == k and i[2] == k) or (i[0] == k and i[3] == k and i[6] == k) or (i[6] == k and i[7] == k and i[8] == k):
        g_ttt_game_loop = False
    elif (i[3] == k and i[4] == k and i[5] == k) or (i[1] == k and i[4] == k and i[7] == k) or (i[2] == k and i[5] == k and i[8] == k):
        g_ttt_game_loop = False
    elif (i[0] == k and i[4] == k and i[8] == k) or (i[2] == k and i[4] == k and i[6] == k):
        g_ttt_game_loop = False
    if g_ttt_game_loop == False:
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
    #Resets board values list for a new game:
    ttt_game_state_list.clear()        
    for i in range(9):
        ttt_game_state_list.append(" ")   

def main_menu_blit():
    screen.blit(main_menu, rect_main_menu)
    screen.blit(new_game, (145,188))
    screen.blit(about_image, (210,266))
    screen.blit(quit_image, (230,331))
    screen.blit(pepe_waiting_1, (4,441))

def clean_up_after_match_finalisation(winner_image, winner_image_rect, ttt_game_state_list):
    screen.blit(winner_image, winner_image_rect)
    reseting_win_conditions(ttt_game_state_list)
    pygame.mixer.Channel(0).pause()
    pygame.mixer.Channel(1).play(pygame.mixer.Sound(winning_sound))

def blitme_whose_turn_it_is():
    if player_turn_switching == True:
        screen.blit(x_turn_announcment, (211,35))        
    else:
        screen.blit(o_turn_announcment, (211,35))

def hovering_effect(mouse_postion):
        mp = mouse_postion
        if mp[0] in range(145, 443) and mp[1] in range(188, 267):
            screen.blit(new_game_hovered, (145,188))
            screen.blit(pepe_newgame_1, (4,441))
        elif mp[0] in range(210, 381) and mp[1] in range(266, 331):
            screen.blit(about_image_hovered, (210,266))
            screen.blit(pepe_about_1, (4,441))
        elif mp[0] in range(230, 354) and mp[1] in range(331, 403):
            screen.blit(quit_image_hovered, (230,331))
            screen.blit(pepe_quit_1, (4,441))

def main_menu_pygame_events(mouse_postion):
    global g_ttt_game_loop
    mp = mouse_postion
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #Press ESC to close the game window:  
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        #Deciding what happens after any mouse button click:
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #Get the position of the mouse click:
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
            #Press ESC to close the game window:  
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
#X and O turn switching. |True is X|False is O|:
player_turn_switching = True

#The main game loop
while main_program_loop:
    #pygame.mixer.music.play(-1)
    
    #>>>>>>>>>>>>>>> Start of - main menu feature: <<<<<<<<<<<<<<<<
    main_menu_blit()
    pos_0 = pygame.mouse.get_pos()
    hovering_effect(pos_0)
    g_ttt_game_loop = False
    main_menu_pygame_events(pos_0)
    #End. ---------------------------------------------------------
                
    pygame.display.flip()
    
    #>>>>>>>>>>>> Start of - tic tac toe game feature: <<<<<<<<<<<<
    #The main game board image:
    screen.blit(main_menu, rect_main_menu)
    screen.blit(main_board_image, rect_board)
    player_turn_switching = True
    #Tic Tac Toe loop:
    g_match_outcome_end_screen = False
    while g_ttt_game_loop:
        blitme_whose_turn_it_is()
        # To handle events happening in a pygame window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #Press ESC to close the game window:  
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            #Deciding what happens after any mouse button click:
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #Get the position of the mouse click:
                pos = pygame.mouse.get_pos()
                #Redraw after each mouse click:
                #X turn:
                if player_turn_switching == True:
                    is_ttt_board_spot_taken = False   
                    blitme_updating_the_state_of_a_game("X", x_image_scaled, rect_x, board_values_list)
                    game_victory_checking("X", "Player1", board_values_list) 
                    if g_ttt_game_loop == False:
                        clean_up_after_match_finalisation(x_wins_image, rect_x_wins_image, board_values_list)
                    no_winner_checking(board_values_list)
                    #Checking if X was placed in the available empty spot, play the sound and switch the turn:
                    if is_ttt_board_spot_taken == False:
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound(figure_placement_sound))
                        player_turn_switching = False
                #O turn:
                elif player_turn_switching == False:
                    is_ttt_board_spot_taken = False
                    blitme_updating_the_state_of_a_game("O", o_image_scaled, rect_o, board_values_list)
                    game_victory_checking("O", "Player2", board_values_list)   
                    if g_ttt_game_loop == False:
                        clean_up_after_match_finalisation(o_wins_image, rect_o_wins_image, board_values_list)
                    no_winner_checking(board_values_list)
                    #Checking if O was placed in the available empty spot, play the sound and switch the turn:
                    if is_ttt_board_spot_taken == False:
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound(figure_placement_sound))         
                        player_turn_switching = True
    
        #Make the most recently drawn screen visible.
        pygame.display.flip()

    match_end_screen_waiting_for_a_mouse_click()

