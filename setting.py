import pygame
import math
import main

def initialize(board_size,window_size):
    global black
    global white
    global red
    global blue
    global grey

    global static_img
    global big_boards_static
    global big_boards_active
    global small_boards_static
    global small_boards_active
    global blinking

    global Main_center
    global big_radius
    global big_board_radius
    global big_board_ref_radius
    global small_board_radius
    global degree_path
    global degree_cycle
    global big_board_center_list
    global small_board_center_list

    global position
    global blue_possible
    global red_possible
    global Win_con_op
    global Big_board_position
    global Big_board_possible_red
    global Big_board_possible_blue
    global ref_N

    global next_game
    next_game = board_size + 1
    global k
    k = 0

    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    blue = (0,0,255)
    grey = (220,220,220)


    #All the surfaces we will use
    static_img = pygame.Surface(window_size,pygame.SRCALPHA) #Biggest circles
    big_boards_static = pygame.Surface(window_size,pygame.SRCALPHA) #The outside of the board
    big_boards_active = pygame.Surface(window_size,pygame.SRCALPHA)
    small_boards_static = pygame.Surface(window_size,pygame.SRCALPHA)
    small_boards_active = pygame.Surface(window_size,pygame.SRCALPHA)
    blinking = pygame.Surface(window_size,pygame.SRCALPHA)


    position = []
    blue_possible = [] #Auxilary list to represent player 2 move on the small board
    red_possible = [] #Auxilary list to represent player 1 move on the small board
    Win_con_op = [] #Auxilary list for the big board
    Big_board_position = [] #Position on the big board. 
    Big_board_possible_red = []
    Big_board_possible_blue = []
    ref_N = []

    for row in range(board_size):
        position.append([])
        blue_possible.append([])
        red_possible.append([])
        Win_con_op.append(0)
        Big_board_position.append(0)
        Big_board_possible_red.append('Y')
        Big_board_possible_blue.append('Y')
        ref_N.append('N')
        for column in range(board_size):
            position[row].append(0)
            blue_possible[row].append('Y')
            red_possible[row].append('Y')


    Main_center = (window_size[0] // 2, window_size[1] // 2)
    big_radius = 260 * window_size[0]/700
    big_board_radius = 87 * window_size[0]/700
    big_board_ref_radius = 47 * window_size[0]/700
    small_board_radius = 17 * window_size[0]/700
    pygame.draw.circle(static_img, black, Main_center, big_radius, width = 5)
    degree_path = math.radians(360 // (board_size+1))
    degree_cycle = math.radians(360 // board_size)
    big_board_center_list = [] #We need this list to change game state later
    small_board_center_list = []