import pygame
import math

import setting


def board_path(board_size,window_size):
    #Start Drawing Board
    big_board_center = (setting.Main_center[0] - setting.big_radius*math.sin(0), setting.Main_center[1] - setting.big_radius*math.cos(0))
    pygame.draw.circle(setting.big_boards_active, setting.white, big_board_center, setting.big_board_radius, width = 0)
    for i in range(board_size):
        big_board_center = (setting.Main_center[0] - setting.big_radius*math.sin(setting.degree_path*(i+1)), setting.Main_center[1] - setting.big_radius*math.cos(setting.degree_path*(i+1)))
        setting.big_board_center_list.append(big_board_center)
        setting.small_board_center_list.append([])
        pygame.draw.circle(setting.big_boards_active, setting.black, setting.big_board_center_list[i], setting.big_board_radius, width = 5)
        pygame.draw.circle(setting.big_boards_static, setting.white, setting.big_board_center_list[i], setting.big_board_radius-5)
        pygame.draw.circle(setting.small_boards_static, setting.black, setting.big_board_center_list[i],setting.big_board_ref_radius, width = 3)
        pygame.draw.circle(setting.small_boards_active, setting.black, setting.big_board_center_list[i],setting.small_board_radius, width = 3)
        
        small_board_center = (setting.big_board_center_list[i][0] - (setting.big_board_ref_radius)*math.sin(setting.degree_path*(0)), 
                                        setting.big_board_center_list[i][1] - (setting.big_board_ref_radius)*math.cos(setting.degree_path*(0)))
        pygame.draw.circle(setting.small_boards_active, setting.white, small_board_center, setting.small_board_radius, width = 0)
        
        for j in range(board_size):
            small_board_center = (setting.big_board_center_list[i][0] - (setting.big_board_ref_radius)*math.sin(setting.degree_path*(j+1)), 
                                        setting.big_board_center_list[i][1] - (setting.big_board_ref_radius)*math.cos(setting.degree_path*(j+1)))
            setting.small_board_center_list[i].append(small_board_center)
            pygame.draw.circle(setting.small_boards_active, setting.black, setting.small_board_center_list[i][j], setting.small_board_radius, width = 3)
            pygame.draw.circle(setting.small_boards_static, setting.white, setting.small_board_center_list[i][j], setting.small_board_radius-3)
    #End Drawing Board

    
def board_cycle(board_size,window_size):
    #Start Drawing Board
    for i in range(board_size):
        big_board_center = (setting.Main_center[0] - setting.big_radius*math.sin(setting.degree_cycle*i), setting.Main_center[1] - setting.big_radius*math.cos(setting.degree_cycle*i))
        setting.big_board_center_list.append(big_board_center)
        setting.small_board_center_list.append([])
        pygame.draw.circle(setting.big_boards_active, setting.black, setting.big_board_center_list[i], setting.big_board_radius, width = 5)
        pygame.draw.circle(setting.big_boards_static, setting.white, setting.big_board_center_list[i], setting.big_board_radius-5)
        pygame.draw.circle(setting.small_boards_static, setting.black, setting.big_board_center_list[i],setting.big_board_ref_radius, width = 3)
        pygame.draw.circle(setting.small_boards_active, setting.black, setting.big_board_center_list[i],setting.small_board_radius, width = 3)
        for j in range(board_size):
            small_board_center = (setting.big_board_center_list[i][0] - (setting.big_board_ref_radius)*math.sin(setting.degree_cycle*j), 
                                        setting.big_board_center_list[i][1] - (setting.big_board_ref_radius)*math.cos(setting.degree_cycle*j))
            setting.small_board_center_list[i].append(small_board_center)
            pygame.draw.circle(setting.small_boards_active, setting.black, setting.small_board_center_list[i][j], setting.small_board_radius, width = 3)
            pygame.draw.circle(setting.small_boards_static, setting.white, setting.small_board_center_list[i][j], setting.small_board_radius-3)
    #End Drawing Board