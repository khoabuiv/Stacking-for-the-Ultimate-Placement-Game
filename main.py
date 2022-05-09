import pygame
import pygame_menu
import math

import setting
import Board_Type
import Game_Rules

pygame.init()
#Font
Font = pygame.font.SysFont('Arial',35)

board_type = 1
game_type = 1
board_size = 3

window_size = (700,700)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Stacking Games")

def board_Type(type, value):
    global board_type
    board_type = int(value)

def set_game(game, value):
    global game_type
    game_type = int(value)

def change_board_size(number,value):
    global board_size
    board_size = int(value)
 
def start_the_game():

    setting.initialize(board_size,window_size)

    if board_type == 1:
        Board_Type.board_path(board_size,window_size)
    elif board_type == 2:
        Board_Type.board_cycle(board_size,window_size)

    #Winner Screen
    P1_Win = Font.render('Player 1 Wins!' , True , setting.red)
    P1_Win_size = Font.size('Player 1 Wins!')
    P2_Win = Font.render('Player 2 Wins' , True , setting.blue)
    P2_Win_size = Font.size('Player 2 Wins!')

    done = False
    clock = pygame.time.Clock()

    Winner = 0



    alpha = 1
    change = True
    done = False
    blink_spd = 0.6
    pos = (0,0)

    while not done:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()         
                

        #Blinking effect      
        if change == True:
            alpha = alpha + blink_spd
            if alpha >= 175:
                change = False
        elif change == False:
            alpha = alpha - blink_spd
            if alpha <= 30:
                change = True
        
        #Winning Condition
        if ((all(i == 'N' for i in setting.Big_board_possible_red) == True and Winner == 0 and setting.k % 2 == 0)
            or ((all(i == setting.ref_N for i in setting.red_possible)) and setting.k % 2 == 0 and Winner == 0 
                and all(i != 1 for i in setting.Win_con_op) == True)):
            Winner = 2
        elif ((all(i == 'N' for i in setting.Big_board_possible_blue) == True and Winner == 0 and setting.k % 2 == 1)
            or ((all(i == setting.ref_N for i in setting.blue_possible)) and setting.k % 2 == 1 and Winner == 0
                and all(i != 2 for i in setting.Win_con_op) == True)):
            Winner = 1
                    
        #Move set instructions
        for i in range(board_size):    
            Game_Rules.big_board_draw(board_size, i)
            for j in range(board_size):
                Game_Rules.big_board_check(board_size, i, j)
                ###Game goes here
                if board_type == 1:
                    if game_type == 1:
                        Game_Rules.snort_path(pos, board_size, i, j)
                    elif game_type == 2:
                        Game_Rules.cis_path(pos, board_size, i, j)
                    elif game_type == 3:
                        Game_Rules.col_path(pos, board_size, i, j)
                elif board_type == 2:
                    if game_type == 1:
                        Game_Rules.snort_cycle(pos, board_size, i, j)
                    elif game_type == 2:
                        Game_Rules.cis_cycle(pos, board_size, i, j)
                    elif game_type == 3:
                        Game_Rules.col_cycle(pos, board_size, i, j)
                
                Game_Rules.small_board_draw(board_size, i, j)

        setting.blinking.set_alpha(alpha)        
        pos = (0,0)   
                
        screen.fill(setting.white) #Background color 
        screen.blit(setting.static_img,(0,0))
        screen.blit(setting.big_boards_static,(0,0))
        screen.blit(setting.big_boards_active,(0,0))
        screen.blit(setting.small_boards_static,(0,0))
        screen.blit(setting.blinking,(0,0))
        screen.blit(setting.small_boards_active,(0,0))
        if Winner == 1:
            screen.blit(P1_Win,(0,0))
            pygame.draw.circle(setting.static_img, setting.red, setting.Main_center, setting.big_radius, width = 5)
        elif Winner == 2:
            screen.blit(P2_Win,(0,0))
            pygame.draw.circle(setting.static_img, setting.blue, setting.Main_center, setting.big_radius, width = 5)
            
            
        
        
        
        pygame.display.flip()
menu = pygame_menu.Menu('Stacking Games', 700, 700,
                theme=pygame_menu.themes.THEME_BLUE)

menu.add.selector('Board Type:', [('Path', 1), ('Cycle', 2)], onchange=board_Type)
menu.add.selector('Game :', [('Snort', 1), ('Cis', 2), ('Col', 3)], onchange=set_game)
menu.add.selector('Board Size (2-9):', [('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9),], onchange=change_board_size)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)
