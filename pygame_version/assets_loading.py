""" 
A module that is responsible for loading and preparing images and sounds for a
Pygame Tic-Tac-Toe game.
"""

import pygame

def load_images():
    """
    Loading, scaling all game related images and returning them with their rectangles.

    Returns:
        dict: A dictionary containing images and their rectangles.
    """
    # Loading main board and getting its pixel size:
    main_board_image = pygame.image.load('images/board.png')
    rect_board = main_board_image.get_rect()
    
    # Loading X and O winning, no winner screens images and getting pixel sizes:
    x_wins_image = pygame.image.load('images/board_x_wins.png')
    rect_x_wins_image = x_wins_image.get_rect() 
    o_wins_image = pygame.image.load('images/board_o_wins.png')
    rect_o_wins_image = o_wins_image.get_rect()
    no_winner_image = pygame.image.load('images/board_no_winner.png')
    rect_no_winner_image = no_winner_image.get_rect()
    
    # Loading images for X and O:
    x_image = pygame.image.load('images/X_trans.png')
    o_image = pygame.image.load('images/zero_trans.png')
    
    # Information about desired pixel size of X and O images:
    x_and_o_new_image_size = (118, 118)
    
    # Setting new pixel size of X and O images:
    x_image_scaled = pygame.transform.scale(x_image, x_and_o_new_image_size)
    o_image_scaled = pygame.transform.scale(o_image, x_and_o_new_image_size)
    
    # Getting the pixel size of X and O images:
    rect_x = x_image_scaled.get_rect()
    rect_o = o_image_scaled.get_rect()
    
    # Loading all main menu images:
    main_menu = pygame.image.load('images/main_menu.png')
    rect_main_menu = main_menu.get_rect()  # Added missing rect_main_menu
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
    
    # Whose turn images and rects:
    x_turn_announcment = pygame.image.load('images/x_turn_announcment.png')
    rect_x_turn_announcment = x_turn_announcment.get_rect()
    o_turn_announcment = pygame.image.load('images/o_turn_announcment.png')
    rect_o_turn_announcment = o_turn_announcment.get_rect()
    
    return {
        'main_board_image': (main_board_image, rect_board),
        'x_wins_image': (x_wins_image, rect_x_wins_image),
        'o_wins_image': (o_wins_image, rect_o_wins_image),
        'no_winner_image': (no_winner_image, rect_no_winner_image),
        'x_image_scaled': (x_image_scaled, rect_x),
        'o_image_scaled': (o_image_scaled, rect_o),
        'main_menu': (main_menu, rect_main_menu),  # Include rect_main_menu in the returned dictionary
        'resume': resume,
        'resume_hovered': resume_hovered,
        'new_game': new_game,
        'new_game_hovered': new_game_hovered,
        'about_image': about_image,
        'about_image_hovered': about_image_hovered,
        'quit_image': quit_image,
        'quit_image_hovered': quit_image_hovered,
        'pepe_newgame_1': pepe_newgame_1,
        'pepe_about_1': pepe_about_1,
        'pepe_quit_1': pepe_quit_1,
        'pepe_waiting_1': pepe_waiting_1,
        'x_turn_announcment': (x_turn_announcment, rect_x_turn_announcment),
        'o_turn_announcment': (o_turn_announcment, rect_o_turn_announcment)
    }

def load_sounds():
    """
    Loading all game related sounds into a mixer, setting their volume level and returning them in a dictionary.

    Sounds loaded:
        Background music, winning and draw sounds, figure placement sound.

    Returns:
        dict: A dictionary containing loaded sounds.
    """
    pygame.mixer.music.load('images/bg_sound.mp3')
    pygame.mixer.music.set_volume(0.5)
    winning_sound = pygame.mixer.Sound('images/winning_sound.mp3')
    no_winner_sound = pygame.mixer.Sound('images/no_winner_sound.mp3')
    figure_placement_sound = pygame.mixer.Sound('images/placement_sound.wav')
    
    winning_sound.set_volume(0.7)
    no_winner_sound.set_volume(1)
    
    return {
        'bg_music': pygame.mixer.music,
        'winning_sound': winning_sound,
        'no_winner_sound': no_winner_sound,
        'figure_placement_sound': figure_placement_sound
    }
