import pygame
import setting

def big_board_draw_grid(board_size,a, b):
    #Draw on the big board
    if setting.Big_board_position[a][b] == 1:
        pygame.draw.polygon(setting.active_board_img_1, setting.red, [setting.small_center_list[a][b][0][0], #Top Left
                                    setting.small_center_list[a][b][0][board_size-1], #Top Right
                                    setting.small_center_list[a][b][board_size-1][board_size-1], #Bottom Right
                                    setting.small_center_list[a][b][board_size-1][0]], width = 0) #Bottom Left
    elif setting.Big_board_position[a][b] == 2:
        pygame.draw.polygon(setting.active_board_img_1, setting.blue, [setting.small_center_list[a][b][0][0], #Top Left
                                    setting.small_center_list[a][b][0][board_size-1], #Top Right
                                    setting.small_center_list[a][b][board_size-1][board_size-1], #Bottom Right
                                    setting.small_center_list[a][b][board_size-1][0]], width = 0) #Bottom Left
    #Draw the blinking effect for big board
    if (setting.Win_con_op[a][b] == 1
        and setting.Big_board_possible_red[a][b] == 'Y' 
        and setting.Big_board_position[a][b] == 0 and setting.k % 2 == 0):
        pygame.draw.polygon(setting.blinking_1, setting.red, [setting.small_center_list[a][b][0][0], #Top Left
                                    setting.small_center_list[a][b][0][board_size-1], #Top Right
                                    setting.small_center_list[a][b][board_size-1][board_size-1], #Bottom Right
                                    setting.small_center_list[a][b][board_size-1][0]], width = 0) #Bottom Left
    elif (setting.Win_con_op[a][b] == 2 
        and setting.Big_board_possible_blue[a][b] == 'Y' 
        and setting.Big_board_position[a][b] == 0 and setting.k % 2 == 1):
        pygame.draw.polygon(setting.blinking_1, setting.blue, [setting.small_center_list[a][b][0][0], #Top Left
                                    setting.small_center_list[a][b][0][board_size-1], #Top Right
                                    setting.small_center_list[a][b][board_size-1][board_size-1], #Bottom Right
                                    setting.small_center_list[a][b][board_size-1][0]], width = 0) #Bottom Left
    else:
        pygame.draw.polygon(setting.blinking_1, setting.white, [setting.small_center_list[a][b][0][0], #Top Left
                                    setting.small_center_list[a][b][0][board_size-1], #Top Right
                                    setting.small_center_list[a][b][board_size-1][board_size-1], #Bottom Right
                                    setting.small_center_list[a][b][board_size-1][0]], width = 0) #Bottom Left  


def big_board_draw(board_size, i):
        # Draw for the big board
    if setting.Big_board_position[i] == 1:
        pygame.draw.circle(setting.big_boards_active, setting.red, setting.big_board_center_list[i], setting.big_board_radius, width = 5)
        pygame.draw.circle(setting.big_boards_active, setting.red, setting.big_board_center_list[i], setting.big_board_ref_radius, width = 8)
        pygame.draw.circle(setting.small_boards_active, setting.red, setting.big_board_center_list[i], setting.small_board_radius, width = 0)
        pygame.draw.circle(setting.small_boards_static, setting.white, setting.big_board_center_list[i], setting.big_board_ref_radius, width = 3)
    elif setting.Big_board_position[i] == 2:
        pygame.draw.circle(setting.big_boards_active, setting.blue, setting.big_board_center_list[i], setting.big_board_radius, width = 5)
        pygame.draw.circle(setting.big_boards_active, setting.blue, setting.big_board_center_list[i], setting.big_board_ref_radius, width = 8)
        pygame.draw.circle(setting.small_boards_active, setting.blue, setting.big_board_center_list[i], setting.small_board_radius, width = 0)
        pygame.draw.circle(setting.small_boards_static, setting.white, setting.big_board_center_list[i], setting.big_board_ref_radius, width = 3)
    #Draw the blinking effect for big board
    if (setting.Win_con_op[i] == 1 
            and setting.Big_board_possible_red[i] == 'Y' 
            and setting.Big_board_position[i] == 0 and setting.k % 2 == 0):
        pygame.draw.circle(setting.blinking, setting.red, setting.big_board_center_list[i], setting.big_board_radius + 3, width = 3)
        pygame.draw.circle(setting.blinking, setting.red, setting.big_board_center_list[i], setting.small_board_radius - 3, width = 3)
    elif (setting.Win_con_op[i] == 2 
            and setting.Big_board_possible_blue[i] == 'Y' 
            and setting.Big_board_position[i] == 0 and setting.k % 2 == 1):
        pygame.draw.circle(setting.blinking, setting.blue, setting.big_board_center_list[i], setting.big_board_radius + 3, width = 3)
        pygame.draw.circle(setting.blinking, setting.blue, setting.big_board_center_list[i], setting.small_board_radius - 3, width = 3)
    else:
        pygame.draw.circle(setting.blinking, setting.white, setting.big_board_center_list[i], setting.big_board_radius + 3, width = 3)
        pygame.draw.circle(setting.blinking, setting.white, setting.big_board_center_list[i], setting.small_board_radius - 3, width = 3)


def big_board_check_grid(board_size, a, b):
    #Check the board state
    if (all(i == setting.ref_N for i in setting.red_possible[a][b]) == True and setting.k % 2 == 0):
        if setting.next_game == (a,b):
            setting.next_game = (setting.n+1,setting.n+1) 
            #If there is no possible move on a board i, then the player free to move anywhere
        if (setting.Win_con_op[a][b] == 0):
            setting.Win_con_op[a][b] = 2 # small boards winning conditions checks

    if (all(i == setting.ref_N for i in setting.blue_possible[a][b]) == True and setting.k % 2 == 1):
        if setting.next_game == (a,b):
            setting.next_game = (setting.n+1, setting.n+1) 
            #If there is no possible move on a board i, then the player free to move anywhere
        if (setting.Win_con_op[a][b] == 0):
            setting.Win_con_op[a][b] = 1 # small boards winning conditions checks


def big_board_check(board_size, i, j):
    if (all(a == 'N' for a in setting.red_possible[i]) == True and setting.k % 2 == 0):
        if setting.next_game == i:
            setting.next_game = board_size + 1 #If there is no possible move on a board i, then the player free to move anywhere
        if (setting.Win_con_op[i] == 0 and setting.position[i][j] == 2):
            setting.Win_con_op[i] = 2 # small boards winning conditions checks
    if (all(a == 'N' for a in setting.blue_possible[i]) == True and setting.k % 2 == 1):
        if setting.next_game == i:
            setting.next_game = board_size + 1
        if (setting.Win_con_op[i] == 0 and setting.position[i][j] == 1):
            setting.Win_con_op[i] = 1 # small boards winning conditions checks

def small_board_draw_grid(board_size, a, b, c, d):
    if setting.position[a][b][c][d] == 1:
        pygame.draw.circle(setting.active_board_img_2,setting.red,setting.small_center_list[a][b][c][d],setting.small_radius-3,width=0)
    elif setting.position[a][b][c][d] == 2:
        pygame.draw.circle(setting.active_board_img_2,setting.blue,setting.small_center_list[a][b][c][d],setting.small_radius-3,width=0)
        
    if (setting.red_possible[a][b][c][d] == 'Y' 
            and setting.position[a][b][c][d] == 0
            and setting.k % 2 == 0 
            and (setting.next_game == (setting.n+1,setting.n+1) or setting.next_game == (a,b))
            ):
        pygame.draw.circle(setting.blinking_2,setting.red,setting.small_center_list[a][b][c][d],setting.small_radius-3,width=3)
    elif (setting.blue_possible[a][b][c][d] == 'Y' 
            and setting.position[a][b][c][d] == 0
            and setting.k % 2 == 1 
            and (setting.next_game == (setting.n+1,setting.n+1) or setting.next_game == (a,b))
            ):
        pygame.draw.circle(setting.blinking_2,setting.blue,setting.small_center_list[a][b][c][d],setting.small_radius-3,width=3)
    else:
        pygame.draw.circle(setting.blinking_2,setting.white,setting.small_center_list[a][b][c][d],setting.small_radius-3,width=3)



def small_board_draw(board_size, i, j):
    #Draw on the small board
        if setting.position[i][j] == 1:
            pygame.draw.circle(setting.small_boards_active, setting.red, setting.small_board_center_list[i][j], setting.small_board_radius-3,width=0)
        elif setting.position[i][j] == 2:
            pygame.draw.circle(setting.small_boards_active, setting.blue, setting.small_board_center_list[i][j], setting.small_board_radius-3,width=0) 
    #Blinking Effect on the small board
        if (setting.red_possible[i][j] == 'Y' 
                and setting.position[i][j] == 0
                and setting.k % 2 == 0 
                and (setting.next_game == board_size + 1 or setting.next_game == i)):
            pygame.draw.circle(setting.blinking, setting.red, setting.small_board_center_list[i][j], setting.small_board_radius-3,width=3)
        elif (setting.blue_possible[i][j] == 'Y' 
                and setting.position[i][j] == 0
                and setting.k % 2 == 1 
                and (setting.next_game == board_size + 1 or setting.next_game == i)):
            pygame.draw.circle(setting.blinking, setting.blue, setting.small_board_center_list[i][j], setting.small_board_radius-3,width=3)
        else:
            pygame.draw.circle(setting.blinking, setting.white, setting.small_board_center_list[i][j], setting.small_board_radius-3,width=3)

def snort_cycle(pos, board_size, i, j):
    #Big Board Instruction
    if ((((setting.big_board_center_list[i][0] - setting.small_board_radius) < pos[0]
        and pos[0] < (setting.big_board_center_list[i][0] + setting.small_board_radius))
        and ((setting.big_board_center_list[i][1] - setting.small_board_radius) < pos[1]
        and pos[1] < (setting.big_board_center_list[i][1] + setting.small_board_radius)))
            ):
        if setting.Win_con_op[i] == 1 and setting.k % 2 == 0:
            if setting.Big_board_position[(i+1) % board_size] == 2 or setting.Big_board_position[(i-1) % board_size] == 2:
                setting.Big_board_position[i] = 0
            else:
                setting.Big_board_position[i] = 1
                setting.next_game = board_size + 1
                setting.k = setting.k + 1
                setting.Big_board_possible_red[(i) % board_size] = 'N'
                setting.Big_board_possible_blue[(i) % board_size] = 'N'
                setting.Big_board_possible_blue[(i+1) % board_size] = 'N'
                setting.Big_board_possible_blue[(i-1) % board_size] = 'N'
                setting.Win_con_op[i] = 0
        elif setting.Win_con_op[i] == 2 and setting.k % 2 == 1: 
            if setting.Big_board_position[(i+1) % board_size] == 1 or setting.Big_board_position[(i-1) % board_size] == 1:
                setting.Big_board_position[i] = 0
            else:
                setting.Big_board_position[i] = 2
                setting.next_game = board_size + 1
                setting.k = setting.k + 1
                setting.Big_board_possible_blue[(i) % board_size] = 'N'
                setting.Big_board_possible_red[(i) % board_size] = 'N'
                setting.Big_board_possible_red[(i+1) % board_size] = 'N'
                setting.Big_board_possible_red[(i-1) % board_size] = 'N'
                setting.Win_con_op[i] = 0
    #Small Board Instructions
    elif ((setting.small_board_center_list[i][j][0] - setting.small_board_radius) < pos[0] 
        and pos[0] < (setting.small_board_center_list[i][j][0] + setting.small_board_radius) 
        and (setting.small_board_center_list[i][j][1] - setting.small_board_radius) < pos[1] 
        and pos[1] < (setting.small_board_center_list[i][j][1] + setting.small_board_radius) 
        ):
        if setting.k % 2 == 0 and setting.position[i][j] == 0 and (setting.next_game == i or setting.next_game == board_size + 1):
            if setting.position[i][(j-1) % board_size] == 2 or setting.position[i][(j+1) % board_size] == 2:
                setting.position[i][j] = 0
            else:
                setting.position[i][j] = 1
                setting.next_game = j
                setting.red_possible[i][j] = 'N'
                setting.blue_possible[i][j] = 'N'
                setting.blue_possible[i][j-1] = 'N'
                setting.blue_possible[i][j+1] = 'N'
                setting.k = setting.k + 1
        elif setting.k % 2 == 1 and setting.position[i][j] == 0 and (setting.next_game == i or setting.next_game == board_size + 1):
            if setting.position[i][(j-1) % board_size] == 1 or setting.position[i][(j+1) % board_size] == 1:
                setting.position[i][j] = 0
            else:
                setting.position[i][j] = 2
                setting.next_game = j
                setting.blue_possible[i][j] = 'N'
                setting.red_possible[i][j] = 'N'
                setting.red_possible[i][j-1] = 'N'
                setting.red_possible[i][j+1] = 'N'
                setting.k = setting.k + 1


def snort_path(pos, board_size, i, j):
    #Big Board Instruction
    if ((((setting.big_board_center_list[i][0] - setting.small_board_radius) < pos[0]
        and pos[0] < (setting.big_board_center_list[i][0] + setting.small_board_radius))
        and ((setting.big_board_center_list[i][1] - setting.small_board_radius) < pos[1]
        and pos[1] < (setting.big_board_center_list[i][1] + setting.small_board_radius)))
            ):
        if setting.Win_con_op[i] == 1 and setting.k % 2 == 0:
            if i == 0:
                if setting.Big_board_position[i+1] == 2:
                    setting.Big_board_position[i] = 0
                else:
                    setting.Big_board_position[i] = 1
                    setting.next_game = board_size + 1
                    setting.k = setting.k + 1 
                    setting.Big_board_possible_red[i] = 'N'
                    setting.Big_board_possible_blue[i] = 'N'
                    setting.Big_board_possible_blue[i+1] = 'N'
                    setting.Win_con_op[i] = 0
            elif i == (board_size - 1):
                if setting.Big_board_position[i-1] == 2:
                    setting.Big_board_position[i] = 0
                else:
                    setting.Big_board_position[i] = 1
                    setting.next_game = board_size + 1
                    setting.k = setting.k + 1
                    setting.Big_board_possible_red[i] = 'N'
                    setting.Big_board_possible_blue[i] = 'N'
                    setting.Big_board_possible_blue[i-1] = 'N'
                    setting.Win_con_op[i] = 0
            else:
                if setting.Big_board_position[i+1] == 2 or setting.Big_board_position[i-1] == 2:
                    setting.Big_board_position[i] = 0
                else:
                    setting.Big_board_position[i] = 1
                    setting.next_game = board_size + 1
                    setting.k = setting.k + 1
                    setting.Big_board_possible_red[i] = 'N'
                    setting.Big_board_possible_blue[i] = 'N'
                    setting.Big_board_possible_blue[i+1] = 'N'
                    setting.Big_board_possible_blue[i-1] = 'N'
                    setting.Win_con_op[i] = 0
        elif setting.Win_con_op[i] == 2 and setting.k % 2 == 1:
            if i == 0:
                if setting.Big_board_position[i+1] == 1:
                    setting.Big_board_position[i] = 0
                else:
                    setting.Big_board_position[i] = 2
                    setting.next_game = board_size + 1
                    setting.k = setting.k + 1 
                    setting.Big_board_possible_blue[i] = 'N'
                    setting.Big_board_possible_red[i] = 'N'
                    setting.Big_board_possible_red[i+1] = 'N'
                    setting.Win_con_op[i] = 0
            elif i == (board_size - 1):
                if setting.Big_board_position[i-1] == 1:
                    setting.Big_board_position[i] = 0
                else:
                    setting.Big_board_position[i] = 2
                    setting.next_game = board_size + 1
                    setting.k = setting.k + 1
                    setting.Big_board_possible_blue[i] = 'N'
                    setting.Big_board_possible_red[i] = 'N'
                    setting.Big_board_possible_red[i-1] = 'N'
                    setting.Win_con_op[i] = 0
            else:
                if setting.Big_board_position[i+1] == 1 or setting.Big_board_position[i-1] == 1:
                    setting.Big_board_position[i] = 0
                else:
                    setting.Big_board_position[i] = 2
                    setting.next_game = board_size + 1
                    setting.k = setting.k + 1
                    setting.Big_board_possible_blue[i] = 'N'
                    setting.Big_board_possible_red[i] = 'N'
                    setting.Big_board_possible_red[i+1] = 'N'
                    setting.Big_board_possible_red[i-1] = 'N'
                    setting.Win_con_op[i] = 0
    #Small Board Instructions
    elif ((setting.small_board_center_list[i][j][0] - setting.small_board_radius) < pos[0] 
        and pos[0] < (setting.small_board_center_list[i][j][0] + setting.small_board_radius) 
        and (setting.small_board_center_list[i][j][1] - setting.small_board_radius) < pos[1] 
        and pos[1] < (setting.small_board_center_list[i][j][1] + setting.small_board_radius) 
        ):
        if (setting.k % 2 == 0 
        and setting.position[i][j] == 0 
        and (setting.next_game == i or setting.next_game == board_size + 1)
        and setting.Big_board_position[i] == 0):
            if j == 0: #Left edge
                if setting.position[i][j+1] == 2: 
                    setting.position[i][j] = 0 
                else:
                    setting.position[i][j] = 1
                    setting.red_possible[i][j] = 'N'
                    setting.blue_possible[i][j] = 'N'
                    setting.blue_possible[i][j+1] = 'N'
                    setting.next_game = j
                    setting.k = setting.k + 1
            elif j == (board_size - 1): #Right edge
                if setting.position[i][j-1] == 2:
                    setting.position[i][j] = 0
                else:
                    setting.position[i][j] = 1
                    setting.next_game = j
                    setting.red_possible[i][j] = 'N'
                    setting.blue_possible[i][j] = 'N'
                    setting.blue_possible[i][j-1] = 'N'
                    setting.k = setting.k + 1
            else: #Normal
                if setting.position[i][j-1] == 2 or setting.position[i][j+1] == 2:
                    setting.position[i][j] = 0
                else:
                    setting.position[i][j] = 1
                    setting.next_game = j
                    setting.red_possible[i][j] = 'N'
                    setting.blue_possible[i][j] = 'N'
                    setting.blue_possible[i][j-1] = 'N'
                    setting.blue_possible[i][j+1] = 'N'
                    setting.k = setting.k + 1
        elif setting.k % 2 == 1 and setting.position[i][j] == 0 and (setting.next_game == i or setting.next_game == board_size + 1):
            if j == 0: #Left edge
                if setting.position[i][j+1] == 1: 
                    setting.position[i][j] = 0 
                else:
                    setting.position[i][j] = 2
                    setting.blue_possible[i][j] = 'N'
                    setting.red_possible[i][j] = 'N'
                    setting.red_possible[i][j+1] = 'N'
                    setting.next_game = j
                    setting.k = setting.k + 1
            elif j == (board_size - 1): #Right edge
                if setting.position[i][j-1] == 1:
                    setting.position[i][j] = 0
                else:
                    setting.position[i][j] = 2
                    setting.next_game = j
                    setting.blue_possible[i][j] = 'N'
                    setting.red_possible[i][j] = 'N'
                    setting.red_possible[i][j-1] = 'N'
                    setting.k = setting.k + 1
            else: #Normal
                if setting.position[i][j-1] == 1 or setting.position[i][j+1] == 1:
                    setting.position[i][j] = 0
                else:
                    setting.position[i][j] = 2
                    setting.next_game = j
                    setting.blue_possible[i][j] = 'N'
                    setting.red_possible[i][j] = 'N'
                    setting.red_possible[i][j-1] = 'N'
                    setting.red_possible[i][j+1] = 'N'
                    setting.k = setting.k + 1

def col_cycle(pos, board_size, i, j):
    #Big Board Instruction
    if ((((setting.big_board_center_list[i][0] - setting.small_board_radius) < pos[0]
        and pos[0] < (setting.big_board_center_list[i][0] + setting.small_board_radius))
        and ((setting.big_board_center_list[i][1] - setting.small_board_radius) < pos[1]
        and pos[1] < (setting.big_board_center_list[i][1] + setting.small_board_radius)))
            ):
        if setting.Win_con_op[i] == 1 and setting.k % 2 == 0:
            if setting.Big_board_position[(i+1) % board_size] == 2 or setting.Big_board_position[(i-1) % board_size] == 2:
                setting.Big_board_position[i] = 0
            else:
                setting.Big_board_position[i] = 1
                setting.next_game = board_size + 1
                setting.k = setting.k + 1
                setting.Big_board_possible_red[(i) % board_size] = 'N'
                setting.Big_board_possible_blue[(i) % board_size] = 'N'
                setting.Big_board_possible_red[(i+1) % board_size] = 'N'
                setting.Big_board_possible_red[(i-1) % board_size] = 'N'
                setting.Win_con_op[i] = 0
        elif setting.Win_con_op[i] == 2 and setting.k % 2 == 1: 
            if setting.Big_board_position[(i+1) % board_size] == 1 or setting.Big_board_position[(i-1) % board_size] == 1:
                setting.Big_board_position[i] = 0
            else:
                setting.Big_board_position[i] = 2
                setting.next_game = board_size + 1
                setting.k = setting.k + 1
                setting.Big_board_possible_blue[(i) % board_size] = 'N'
                setting.Big_board_possible_red[(i) % board_size] = 'N'
                setting.Big_board_possible_blue[(i+1) % board_size] = 'N'
                setting.Big_board_possible_blue[(i-1) % board_size] = 'N'
                setting.Win_con_op[i] = 0
    #Small Board Instructions
    elif ((setting.small_board_center_list[i][j][0] - setting.small_board_radius) < pos[0] 
        and pos[0] < (setting.small_board_center_list[i][j][0] + setting.small_board_radius) 
        and (setting.small_board_center_list[i][j][1] - setting.small_board_radius) < pos[1] 
        and pos[1] < (setting.small_board_center_list[i][j][1] + setting.small_board_radius) 
        ):
        if setting.k % 2 == 0 and setting.position[i][j] == 0 and (setting.next_game == i or setting.next_game == board_size + 1):
            if j == 0: #Left edge
                if setting.position[i][j+1] == 2 or setting.position[i][board_size - 1] == 2: 
                    setting.position[i][j] = 0 
                else:
                    setting.position[i][j] = 1
                    setting.red_possible[i][j] = 'N'
                    setting.blue_possible[i][j] = 'N'
                    setting.red_possible[i][j+1] = 'N'
                    setting.red_possible[i][board_size - 1] = 'N'
                    setting.next_game = j
                    setting.k = setting.k + 1
            elif j == (board_size - 1): #Right edge
                if setting.position[i][j-1] == 2 or setting.position[i][0] == 2:
                    setting.position[i][j] = 0
                else:
                    setting.position[i][j] = 1
                    setting.red_possible[i][j] = 'N'
                    setting.blue_possible[i][j] = 'N'
                    setting.red_possible[i][j-1] = 'N'
                    setting.red_possible[i][0] = 'N'
                    setting.next_game = j
                    setting.k = setting.k + 1
            else: #Normal
                if setting.position[i][j-1] == 2 or setting.position[i][j+1] == 2:
                    setting.position[i][j] = 0
                else:
                    setting.position[i][j] = 1
                    setting.red_possible[i][j] = 'N'
                    setting.blue_possible[i][j] = 'N'
                    setting.red_possible[i][j-1] = 'N'
                    setting.red_possible[i][j+1] = 'N'
                    setting.next_game = j
                    setting.k = setting.k + 1
        elif setting.k % 2 == 1 and setting.position[i][j] == 0 and (setting.next_game == i or setting.next_game == board_size + 1):
            if j == 0: #Left edge
                if setting.position[i][j+1] == 1 or setting.position[i][board_size - 1] == 1: 
                    setting.position[i][j] = 0 
                else:
                    setting.position[i][j] = 2
                    setting.blue_possible[i][j] = 'N'
                    setting.red_possible[i][j] = 'N'
                    setting.blue_possible[i][j+1] = 'N'
                    setting.blue_possible[i][board_size - 1] = 'N'
                    setting.next_game = j
                    setting.k = setting.k + 1
            elif j == (board_size - 1): #Right edge
                if setting.position[i][j-1] == 1 or setting.position[i][0] == 1:
                    setting.position[i][j] = 0
                else:
                    setting.position[i][j] = 2
                    setting.next_game = j
                    setting.blue_possible[i][j] = 'N'
                    setting.red_possible[i][j] = 'N'
                    setting.blue_possible[i][j-1] = 'N'
                    setting.blue_possible[i][0] = 'N'
                    setting.k = setting.k + 1
            else: #Normal
                if setting.position[i][j-1] == 1 or setting.position[i][j+1] == 1:
                    setting.position[i][j] = 0
                else:
                    setting.position[i][j] = 2
                    setting.next_game = j
                    setting.blue_possible[i][j] = 'N'
                    setting.red_possible[i][j] = 'N'
                    setting.blue_possible[i][j-1] = 'N'
                    setting.blue_possible[i][j+1] = 'N'
                    setting.k = setting.k + 1

def col_path(pos, board_size, i, j):
    #Big Board Instruction
    if ((((setting.big_board_center_list[i][0] - setting.small_board_radius) < pos[0]
        and pos[0] < (setting.big_board_center_list[i][0] + setting.small_board_radius))
        and ((setting.big_board_center_list[i][1] - setting.small_board_radius) < pos[1]
        and pos[1] < (setting.big_board_center_list[i][1] + setting.small_board_radius)))
            ):
        if setting.Win_con_op[i] == 1 and setting.k % 2 == 0:
            if i == 0:
                if setting.Big_board_position[i+1] == 2:
                    setting.Big_board_position[i] = 0
                else:
                    setting.Big_board_position[i] = 1
                    setting.next_game = board_size + 1
                    setting.k = setting.k + 1 
                    setting.Big_board_possible_red[i] = 'N'
                    setting.Big_board_possible_blue[i] = 'N'
                    setting.Big_board_possible_red[i+1] = 'N'
                    setting.Win_con_op[i] = 0
            elif i == (board_size - 1):
                if setting.Big_board_position[i-1] == 2:
                    setting.Big_board_position[i] = 0
                else:
                    setting.Big_board_position[i] = 1
                    setting.next_game = board_size + 1
                    setting.k = setting.k + 1
                    setting.Big_board_possible_red[i] = 'N'
                    setting.Big_board_possible_blue[i] = 'N'
                    setting.Big_board_possible_red[i-1] = 'N'
                    setting.Win_con_op[i] = 0
            else:
                if setting.Big_board_position[i+1] == 2 or setting.Big_board_position[i-1] == 2:
                    setting.Big_board_position[i] = 0
                else:
                    setting.Big_board_position[i] = 1
                    setting.next_game = board_size + 1
                    setting.k = setting.k + 1
                    setting.Big_board_possible_red[i] = 'N'
                    setting.Big_board_possible_blue[i] = 'N'
                    setting.Big_board_possible_red[i+1] = 'N'
                    setting.Big_board_possible_red[i-1] = 'N'
                    setting.Win_con_op[i] = 0
        elif setting.Win_con_op[i] == 2 and setting.k % 2 == 1:
            if i == 0:
                if setting.Big_board_position[i+1] == 1:
                    setting.Big_board_position[i] = 0
                else:
                    setting.Big_board_position[i] = 2
                    setting.next_game = board_size + 1
                    setting.k = setting.k + 1 
                    setting.Big_board_possible_blue[i] = 'N'
                    setting.Big_board_possible_red[i] = 'N'
                    setting.Big_board_possible_blue[i+1] = 'N'
                    setting.Win_con_op[i] = 0
            elif i == (board_size - 1):
                if setting.Big_board_position[i-1] == 1:
                    setting.Big_board_position[i] = 0
                else:
                    setting.Big_board_position[i] = 2
                    setting.next_game = board_size + 1
                    setting.k = setting.k + 1
                    setting.Big_board_possible_blue[i] = 'N'
                    setting.Big_board_possible_red[i] = 'N'
                    setting.Big_board_possible_blue[i-1] = 'N'
                    setting.Win_con_op[i] = 0
            else:
                if setting.Big_board_position[i+1] == 1 or setting.Big_board_position[i-1] == 1:
                    setting.Big_board_position[i] = 0
                else:
                    setting.Big_board_position[i] = 2
                    setting.next_game = board_size + 1
                    setting.k = setting.k + 1
                    setting.Big_board_possible_blue[i] = 'N'
                    setting.Big_board_possible_red[i] = 'N'
                    setting.Big_board_possible_blue[i+1] = 'N'
                    setting.Big_board_possible_blue[i-1] = 'N'
                    setting.Win_con_op[i] = 0
    #Small Board Instructions
    elif ((setting.small_board_center_list[i][j][0] - setting.small_board_radius) < pos[0] 
        and pos[0] < (setting.small_board_center_list[i][j][0] + setting.small_board_radius) 
        and (setting.small_board_center_list[i][j][1] - setting.small_board_radius) < pos[1] 
        and pos[1] < (setting.small_board_center_list[i][j][1] + setting.small_board_radius) 
        ):
        if setting.k % 2 == 0 and setting.position[i][j] == 0 and (setting.next_game == i or setting.next_game == board_size + 1):
            if j == 0: #Left edge
                if setting.position[i][j+1] == 2: 
                    setting.position[i][j] = 0 
                else:
                    setting.position[i][j] = 1
                    setting.red_possible[i][j] = 'N'
                    setting.blue_possible[i][j] = 'N'
                    setting.red_possible[i][j+1] = 'N'
                    setting.next_game = j
                    setting.k = setting.k + 1
            elif j == (board_size - 1): #Right edge
                if setting.position[i][j-1] == 2:
                    setting.position[i][j] = 0
                else:
                    setting.position[i][j] = 1
                    setting.next_game = j
                    setting.red_possible[i][j] = 'N'
                    setting.blue_possible[i][j] = 'N'
                    setting.red_possible[i][j-1] = 'N'
                    setting.k = setting.k + 1
            else: #Normal
                if setting.position[i][j-1] == 2 or setting.position[i][j+1] == 2:
                    setting.position[i][j] = 0
                else:
                    setting.position[i][j] = 1
                    setting.next_game = j
                    setting.red_possible[i][j] = 'N'
                    setting.blue_possible[i][j] = 'N'
                    setting.red_possible[i][j-1] = 'N'
                    setting.red_possible[i][j+1] = 'N'
                    setting.k = setting.k + 1
        elif setting.k % 2 == 1 and setting.position[i][j] == 0 and (setting.next_game == i or setting.next_game == board_size + 1):
            if j == 0: #Left edge
                if setting.position[i][j+1] == 1: 
                    setting.position[i][j] = 0 
                else:
                    setting.position[i][j] = 2
                    setting.blue_possible[i][j] = 'N'
                    setting.red_possible[i][j] = 'N'
                    setting.blue_possible[i][j+1] = 'N'
                    setting.next_game = j
                    setting.k = setting.k + 1
            elif j == (board_size - 1): #Right edge
                if setting.position[i][j-1] == 1:
                    setting.position[i][j] = 0
                else:
                    setting.position[i][j] = 2
                    setting.next_game = j
                    setting.blue_possible[i][j] = 'N'
                    setting.red_possible[i][j] = 'N'
                    setting.blue_possible[i][j-1] = 'N'
                    setting.k = setting.k + 1
            else: #Normal
                if setting.position[i][j-1] == 1 or setting.position[i][j+1] == 1:
                    setting.position[i][j] = 0
                else:
                    setting.position[i][j] = 2
                    setting.next_game = j
                    setting.blue_possible[i][j] = 'N'
                    setting.red_possible[i][j] = 'N'
                    setting.blue_possible[i][j-1] = 'N'
                    setting.blue_possible[i][j+1] = 'N'
                    setting.k = setting.k + 1

def cis_cycle(pos, board_size, i, j):
    #Big Board Instruction
    if ((((setting.big_board_center_list[i][0] - setting.small_board_radius) < pos[0]
        and pos[0] < (setting.big_board_center_list[i][0] + setting.small_board_radius))
        and ((setting.big_board_center_list[i][1] - setting.small_board_radius) < pos[1]
        and pos[1] < (setting.big_board_center_list[i][1] + setting.small_board_radius)))
            ):
        if setting.Win_con_op[i] == 1 and setting.k % 2 == 0:
            if ((setting.Big_board_position[(i+1) % board_size] == 1 or setting.Big_board_position[(i-1) % board_size] == 1)
                or (setting.Big_board_position[(i+1) % board_size] == 2 or setting.Big_board_position[(i-1) % board_size] == 2)):
                setting.Big_board_position[i] = 0
            else:
                setting.Big_board_position[i] = 1
                setting.next_game = board_size + 1
                setting.k = setting.k + 1
                setting.Big_board_possible_red[(i) % board_size] = 'N'
                setting.Big_board_possible_blue[(i) % board_size] = 'N'
                setting.Big_board_possible_red[(i+1) % board_size] = 'N'
                setting.Big_board_possible_red[(i-1) % board_size] = 'N'
                setting.Big_board_possible_blue[(i+1) % board_size] = 'N'
                setting.Big_board_possible_blue[(i-1) % board_size] = 'N'
                setting.Win_con_op[i] = 0
        elif (setting.Win_con_op[i] == 2 and setting.k % 2 == 1):
            if ((setting.Big_board_position[(i+1) % board_size] == 1 or setting.Big_board_position[(i-1) % board_size] == 1)
                or (setting.Big_board_position[(i+1) % board_size] == 2 or setting.Big_board_position[(i-1) % board_size] == 2)):
                setting.Big_board_position[i] = 0
            else:
                setting.Big_board_position[i] = 2
                setting.next_game = board_size + 1
                setting.k = setting.k + 1
                setting.Big_board_possible_red[(i) % board_size] = 'N'
                setting.Big_board_possible_blue[(i) % board_size] = 'N'
                setting.Big_board_possible_red[(i+1) % board_size] = 'N'
                setting.Big_board_possible_red[(i-1) % board_size] = 'N'
                setting.Big_board_possible_blue[(i+1) % board_size] = 'N'
                setting.Big_board_possible_blue[(i-1) % board_size] = 'N'
                setting.Win_con_op[i] = 0
    #Small Board Instructions
    elif ((setting.small_board_center_list[i][j][0] - setting.small_board_radius) < pos[0] 
        and pos[0] < (setting.small_board_center_list[i][j][0] + setting.small_board_radius) 
        and (setting.small_board_center_list[i][j][1] - setting.small_board_radius) < pos[1] 
        and pos[1] < (setting.small_board_center_list[i][j][1] + setting.small_board_radius) 
        ):
        if setting.k % 2 == 0 and setting.position[i][j] == 0 and (setting.next_game == i or setting.next_game == board_size + 1):
            if ((setting.position[i][(j-1) % board_size] == 1 or setting.position[i][(j+1) % board_size] == 1)
                or (setting.position[i][(j-1) % board_size] == 2 or setting.position[i][(j+1) % board_size] == 2)):
                setting.position[i][j] = 0
            else:
                setting.position[i][j] = 1
                setting.next_game = j
                setting.red_possible[i][j] = 'N'
                setting.blue_possible[i][j] = 'N'
                setting.red_possible[i][j-1] = 'N'
                setting.red_possible[i][j+1] = 'N'
                setting.blue_possible[i][j-1] = 'N'
                setting.blue_possible[i][j+1] = 'N'
                setting.k = setting.k + 1
        elif setting.k % 2 == 1 and setting.position[i][j] == 0 and (setting.next_game == i or setting.next_game == board_size + 1):
            if ((setting.position[i][(j-1) % board_size] == 1 or setting.position[i][(j+1) % board_size] == 1)
                or (setting.position[i][(j-1) % board_size] == 2 or setting.position[i][(j+1) % board_size] == 2)):
                setting.position[i][j] = 0
            else:
                setting.position[i][j] = 2
                setting.next_game = j
                setting.red_possible[i][j] = 'N'
                setting.blue_possible[i][j] = 'N'
                setting.red_possible[i][j-1] = 'N'
                setting.red_possible[i][j+1] = 'N'
                setting.blue_possible[i][j-1] = 'N'
                setting.blue_possible[i][j+1] = 'N'
                setting.k = setting.k + 1

def cis_path(pos, board_size, i, j):
    #Big Board Instruction
    if ((((setting.big_board_center_list[i][0] - setting.small_board_radius) < pos[0]
        and pos[0] < (setting.big_board_center_list[i][0] + setting.small_board_radius))
        and ((setting.big_board_center_list[i][1] - setting.small_board_radius) < pos[1]
        and pos[1] < (setting.big_board_center_list[i][1] + setting.small_board_radius)))
            ):
        if setting.Win_con_op[i] == 1 and setting.k % 2 == 0:
            if i == 0:
                if ((setting.Big_board_position[i+1] == 1) or (setting.Big_board_position[i+1] == 2)):
                    setting.Big_board_position[i] = 0
                else:
                    setting.Big_board_position[i] = 1
                    setting.next_game = board_size + 1
                    setting.k = setting.k + 1 
                    setting.Big_board_possible_red[i] = 'N'
                    setting.Big_board_possible_blue[i] = 'N'
                    setting.Big_board_possible_red[i+1] = 'N'
                    setting.Big_board_possible_blue[i+1] = 'N'
                    setting.Win_con_op[i] = 0
            elif i == (board_size - 1):
                if ((setting.Big_board_position[i-1] == 1) or (setting.Big_board_position[i-1] == 2)):
                    setting.Big_board_position[i] = 0
                else:
                    setting.Big_board_position[i] = 1
                    setting.next_game = board_size + 1
                    setting.k = setting.k + 1
                    setting.Big_board_possible_red[i] = 'N'
                    setting.Big_board_possible_red[i-1] = 'N'
                    setting.Big_board_possible_blue[i] = 'N'
                    setting.Big_board_possible_blue[i-1] = 'N'
                    setting.Win_con_op[i] = 0
            else:
                if ((setting.Big_board_position[i+1] == 1 or setting.Big_board_position[i-1] == 1)
                    or (setting.Big_board_position[i+1] == 2 or setting.Big_board_position[i-1] == 2)):
                    setting.Big_board_position[i] = 0
                else:
                    setting.Big_board_position[i] = 1
                    setting.next_game = board_size + 1
                    setting.k = setting.k + 1
                    setting.Big_board_possible_red[i] = 'N'
                    setting.Big_board_possible_red[i+1] = 'N'
                    setting.Big_board_possible_red[i-1] = 'N'
                    setting.Big_board_possible_blue[i] = 'N'
                    setting.Big_board_possible_blue[i+1] = 'N'
                    setting.Big_board_possible_blue[i-1] = 'N'
                    setting.Win_con_op[i] = 0
        elif (setting.Win_con_op[i] == 2 and setting.k % 2 == 1):
            if i == 0:
                if ((setting.Big_board_position[i+1] == 1) or (setting.Big_board_position[i+1] == 2)):
                    setting.Big_board_position[i] = 0
                else:
                    setting.Big_board_position[i] = 2
                    setting.next_game = board_size + 1
                    setting.k = setting.k + 1
                    setting.Big_board_possible_blue[i] = 'N'
                    setting.Big_board_possible_blue[i+1] = 'N'
                    setting.Big_board_possible_red[i] = 'N'
                    setting.Big_board_possible_red[i+1] = 'N'
                    setting.Win_con_op[i] = 0
            elif i == (board_size - 1):
                if ((setting.Big_board_position[i-1] == 1) or (setting.Big_board_position[i-1] == 2)):
                    setting.Big_board_position[i] = 0
                else:
                    setting.Big_board_position[i] = 2
                    setting.next_game = board_size + 1
                    setting.k = setting.k + 1
                    setting.Big_board_possible_blue[i] = 'N'
                    setting.Big_board_possible_blue[i-1] = 'N'
                    setting.Big_board_possible_red[i] = 'N'
                    setting.Big_board_possible_red[i-1] = 'N'
                    setting.Win_con_op[i] = 0
            else:
                if ((setting.Big_board_position[i+1] == 1 or setting.Big_board_position[i-1] == 1)
                    or (setting.Big_board_position[i+1] == 2 or setting.Big_board_position[i-1] == 2)):
                    setting.Big_board_position[i] = 0
                else:
                    setting.Big_board_position[i] = 2
                    setting.next_game = board_size + 1
                    setting.k = setting.k + 1
                    setting.Big_board_possible_blue[i] = 'N'
                    setting.Big_board_possible_blue[i+1] = 'N'
                    setting.Big_board_possible_blue[i-1] = 'N' 
                    setting.Big_board_possible_red[i] = 'N'
                    setting.Big_board_possible_red[i+1] = 'N'
                    setting.Big_board_possible_red[i-1] = 'N' 
                    setting.Win_con_op[i] = 0
    #Small Board Instructions
    elif ((setting.small_board_center_list[i][j][0] - setting.small_board_radius) < pos[0] 
        and pos[0] < (setting.small_board_center_list[i][j][0] + setting.small_board_radius) 
        and (setting.small_board_center_list[i][j][1] - setting.small_board_radius) < pos[1] 
        and pos[1] < (setting.small_board_center_list[i][j][1] + setting.small_board_radius) 
        ):
        if setting.k % 2 == 0 and setting.position[i][j] == 0 and (setting.next_game == i or setting.next_game == board_size + 1):
            if j == 0: #Left edge
                if ((setting.position[i][j+1] == 1) or (setting.position[i][j+1] == 2)):
                    setting.position[i][j] = 0 
                else:
                    setting.position[i][j] = 1
                    setting.red_possible[i][j] = 'N'
                    setting.red_possible[i][j+1] = 'N'
                    setting.blue_possible[i][j] = 'N'
                    setting.blue_possible[i][j+1] = 'N'
                    setting.next_game = j
                    setting.setting.k = setting.k + 1
                    setting.Win_con_op[i] = 0
            elif j == (board_size - 1): #Right edge
                if ((setting.position[i][j-1] == 1) or (setting.position[i][j-1] == 2)):
                    setting.position[i][j] = 0
                else:
                    setting.position[i][j] = 1
                    setting.next_game = j
                    setting.red_possible[i][j] = 'N'
                    setting.red_possible[i][j-1] = 'N'
                    setting.blue_possible[i][j] = 'N'
                    setting.blue_possible[i][j-1] = 'N'
                    setting.k = setting.k + 1
                    setting.Win_con_op[i] = 0
            else: #Normal
                if ((setting.position[i][j-1] == 1 or setting.position[i][j+1] == 1)
                    or (setting.position[i][j-1] == 2 or setting.position[i][j+1] == 2)):
                    setting.position[i][j] = 0
                else:
                    setting.position[i][j] = 1
                    setting.next_game = j
                    setting.red_possible[i][j] = 'N'
                    setting.red_possible[i][j-1] = 'N'
                    setting.red_possible[i][j+1] = 'N'
                    setting.blue_possible[i][j] = 'N'
                    setting.blue_possible[i][j-1] = 'N'
                    setting.blue_possible[i][j+1] = 'N'
                    setting.k = setting.k + 1 
                    setting.Win_con_op[i] = 0
        elif (setting.k % 2 == 1 and setting.position[i][j] == 0 and (setting.next_game == i or setting.next_game == board_size + 1)):
            if j == 0: #Left edge
                if ((setting.position[i][j+1] == 1)
                    or (setting.position[i][j+1] == 2)):
                    setting.position[i][j] = 0 
                else:
                    setting.position[i][j] = 2
                    setting.next_game = j
                    setting.blue_possible[i][j] = 'N'
                    setting.blue_possible[i][j+1] = 'N'
                    setting.red_possible[i][j] = 'N'
                    setting.red_possible[i][j+1] = 'N'
                    setting.k = setting.k + 1
                    setting.Win_con_op[i] = 0
            elif j == (board_size - 1): #Right edge
                if ((setting.position[i][j-1] == 1)
                    or (setting.position[i][j-1] == 2)):
                    setting.position[i][j] = 0
                else:
                    setting.position[i][j] = 2
                    setting.next_game = j
                    setting.blue_possible[i][j] = 'N'
                    setting.blue_possible[i][j-1] = 'N'
                    setting.red_possible[i][j] = 'N'
                    setting.red_possible[i][j-1] = 'N'
                    setting.k = setting.k + 1
                    setting.Win_con_op[i] = 0
            else: #Normal
                if ((setting.position[i][j-1] == 1 or setting.position[i][j+1] == 1)
                    or (setting.position[i][j-1] == 2 or setting.position[i][j+1] == 2)):
                    setting.position[i][j] = 0
                else:
                    setting.position[i][j] = 2
                    setting.next_game = j
                    setting.blue_possible[i][j] = 'N'
                    setting.blue_possible[i][j-1] = 'N'
                    setting.blue_possible[i][j+1] = 'N'
                    setting.red_possible[i][j] = 'N'
                    setting.red_possible[i][j-1] = 'N'
                    setting.red_possible[i][j+1] = 'N'
                    setting.k = setting.k + 1 
                    setting.Win_con_op[i] = 0

def snort_grid(pos, board_size, a, b, c, d):
    #Small Board Instruction
    if ((setting.small_center_list[a][b][c][d][0] - setting.small_radius) < pos[0]
        and pos[0] < (setting.small_center_list[a][b][c][d][0] + setting.small_radius)
        and (setting.small_center_list[a][b][c][d][1] - setting.small_radius) < pos[1]
        and pos[1] < (setting.small_center_list[a][b][c][d][1] + setting.small_radius)):
        if setting.k % 2 == 0 and setting.position[a][b][c][d] == 0 and (setting.next_game == (setting.n+1,setting.n+1) or setting.next_game == (a,b)):
            if c == 0: #Top Row
                if d == 0:  #Left Top Corner Case
                    if (setting.position[a][b][c][d+1] == 2 or setting.position[a][b][c+1][d] == 2):
                        setting.position[a][b][c][d] = 0
                    else:
                        setting.position[a][b][c][d] = 1
                        setting.red_possible[a][b][c][d] = 'N'
                        setting.blue_possible[a][b][c][d] = 'N'
                        setting.blue_possible[a][b][c][d+1] = 'N'
                        setting.blue_possible[a][b][c+1][d] = 'N'
                        setting.k = setting.k + 1
                        setting.next_game = (c,d)
                elif d == (board_size) - 1: #Right Top Corner
                    if (setting.position[a][b][c][d-1] == 2 or setting.position[a][b][c+1][d] == 2):
                        setting.position[a][b][c][d] = 0
                    else:
                        setting.position[a][b][c][d] = 1
                        setting.red_possible[a][b][c][d] = 'N'
                        setting.blue_possible[a][b][c][d] = 'N'
                        setting.blue_possible[a][b][c][d-1] = 'N'
                        setting.blue_possible[a][b][c+1][d] = 'N'
                        setting.k = setting.k + 1
                        setting.next_game = (c,d)
                else:
                    if (setting.position[a][b][c][d-1] == 2 
                        or setting.position[a][b][c][d+1] == 2 
                        or setting.position[a][b][c+1][d] == 2): 
                        setting.position[a][b][c][d] = 0
                    else:
                        setting.position[a][b][c][d] = 1
                        setting.red_possible[a][b][c][d] = 'N'
                        setting.blue_possible[a][b][c][d] = 'N'
                        setting.blue_possible[a][b][c][d-1] = 'N'
                        setting.blue_possible[a][b][c][d+1] = 'N'
                        setting.blue_possible[a][b][c+1][d] = 'N'
                        setting.k = setting.k + 1
                        setting.next_game = (c,d)
            elif c == (board_size) - 1: #Bottom Row
                if d == 0: #Left Bottom Corner
                    if setting.position[a][b][c][d+1] == 2 or setting.position[a][b][c-1][d] == 2:
                        setting.position[a][b][c][d] = 0
                    else:
                        setting.position[a][b][c][d] = 1
                        setting.red_possible[a][b][c][d] = 'N'
                        setting.blue_possible[a][b][c][d] = 'N'
                        setting.blue_possible[a][b][c][d+1] = 'N'
                        setting.blue_possible[a][b][c-1][d] = 'N'
                        setting.k = setting.k + 1
                        setting.next_game = (c,d)
                elif d == (board_size) - 1:#Right Bottom Corner
                    if setting.position[a][b][c][d-1] == 2 or setting.position[a][b][c-1][d] == 2:
                        setting.position[a][b][c][d] = 0
                    else:
                        setting.position[a][b][c][d] = 1
                        setting.red_possible[a][b][c][d] = 'N'
                        setting.blue_possible[a][b][c][d] = 'N'
                        setting.blue_possible[a][b][c][d-1] = 'N'
                        setting.blue_possible[a][b][c-1][d] = 'N'
                        setting.k = setting.k + 1
                        setting.next_game = (c,d)
                else:
                    if (setting.position[a][b][c][d-1] == 2 
                        or setting.position[a][b][c][d+1] == 2 
                        or setting.position[a][b][c-1][d] == 2): 
                        setting.position[a][b][c][d] = 0
                    else:
                        setting.position[a][b][c][d] = 1
                        setting.red_possible[a][b][c][d] = 'N'
                        setting.blue_possible[a][b][c][d] = 'N'
                        setting.blue_possible[a][b][c][d+1] = 'N'
                        setting.blue_possible[a][b][c][d-1] = 'N'
                        setting.blue_possible[a][b][c-1][d] = 'N'
                        setting.k = setting.k + 1
                        setting.next_game = (c,d)
            else:
                if d == 0:
                    if (setting.position[a][b][c][d+1] == 2 
                        or setting.position[a][b][c-1][d] == 2 
                        or setting.position[a][b][c+1][d] == 2):
                        setting.position[a][b][c][d] = 0
                    else:
                        setting.position[a][b][c][d] = 1
                        setting.red_possible[a][b][c][d] = 'N'
                        setting.blue_possible[a][b][c][d] = 'N'
                        setting.blue_possible[a][b][c][d+1] = 'N'
                        setting.blue_possible[a][b][c-1][d] = 'N'
                        setting.blue_possible[a][b][c+1][d] = 'N'
                        setting.k = setting.k + 1
                        setting.next_game = (c,d)
                elif d == (board_size) - 1:#Right Bottom Corner
                    if (setting.position[a][b][c][d-1] == 2 
                        or setting.position[a][b][c-1][d] == 2 
                        or setting.position[a][b][c+1][d] == 2):
                        setting.position[a][b][c][d] = 0
                    else:
                        setting.position[a][b][c][d] = 1
                        setting.red_possible[a][b][c][d] = 'N'
                        setting.blue_possible[a][b][c][d] = 'N'
                        setting.blue_possible[a][b][c][d-1] = 'N'
                        setting.blue_possible[a][b][c-1][d] = 'N'
                        setting.blue_possible[a][b][c+1][d] = 'N'
                        setting.k = setting.k + 1
                        setting.next_game = (c,d)
                else:
                    if (setting.position[a][b][c][d+1] == 2 
                        or setting.position[a][b][c][d-1] == 2 
                        or setting.position[a][b][c-1][d] == 2 
                        or setting.position[a][b][c+1][d] == 2):
                        setting.position[a][b][c][d] = 0
                    else:
                        setting.position[a][b][c][d] = 1
                        setting.red_possible[a][b][c][d] = 'N'
                        setting.blue_possible[a][b][c][d] = 'N'
                        setting.blue_possible[a][b][c][d-1] = 'N'
                        setting.blue_possible[a][b][c][d+1] = 'N'
                        setting.blue_possible[a][b][c-1][d] = 'N'
                        setting.blue_possible[a][d][c+1][d] = 'N'
                        setting.k = setting.k + 1
                        setting.next_game = (c,d)
        elif (setting.k % 2 == 1 and setting.position[a][b][c][d] == 0
            and (setting.next_game == (setting.n+1,setting.n+1) or setting.next_game == (a,b))):
            if c == 0: #Top Row
                if d == 0:  #Left Top Corner Case
                    if (setting.position[a][b][c][d+1] == 1 or setting.position[a][b][c+1][d] == 1):
                        setting.position[a][b][c][d] = 0
                    else:
                        setting.position[a][b][c][d] = 2
                        setting.red_possible[a][b][c][d] = 'N'
                        setting.blue_possible[a][b][c][d] = 'N'
                        setting.red_possible[a][b][c][d+1] = 'N'
                        setting.red_possible[a][b][c+1][d] = 'N'
                        setting.k = setting.k + 1
                        setting.next_game = (c,d)
                elif d == (board_size) - 1: #Right Top Corner
                    if (setting.position[a][b][c][d-1] == 1 or setting.position[a][b][c+1][d] == 1):
                        setting.position[a][b][c][d] = 0
                    else:
                        setting.position[a][b][c][d] = 2
                        setting.red_possible[a][b][c][d] = 'N'
                        setting.blue_possible[a][b][c][d] = 'N'
                        setting.red_possible[a][b][c][d-1] = 'N'
                        setting.red_possible[a][b][c+1][d] = 'N'
                        setting.k = setting.k + 1
                        setting.next_game = (c,d)
                else:
                    if (setting.position[a][b][c][d-1] == 1 
                        or setting.position[a][b][c][d+1] == 1 
                        or setting.position[a][b][c+1][d] == 1): 
                        setting.position[a][b][c][d] = 0
                    else:
                        setting.position[a][b][c][d] = 2
                        setting.red_possible[a][b][c][d] = 'N'
                        setting.blue_possible[a][b][c][d] = 'N'
                        setting.red_possible[a][b][c][d-1] = 'N'
                        setting.red_possible[a][b][c][d+1] = 'N'
                        setting.red_possible[a][b][c+1][d] = 'N'
                        setting.k = setting.k + 1
                        setting.next_game = (c,d)
            elif c == (board_size) - 1: #Bottom Row
                if d == 0: #Left Bottom Corner
                    if setting.position[a][b][c][d+1] == 1 or setting.position[a][b][c-1][d] == 1:
                        setting.position[a][b][c][d] = 0
                    else:
                        setting.position[a][b][c][d] = 2
                        setting.red_possible[a][b][c][d] = 'N'
                        setting.blue_possible[a][b][c][d] = 'N'
                        setting.red_possible[a][b][c][d+1] = 'N'
                        setting.red_possible[a][b][c-1][d] = 'N'
                        setting.k = setting.k + 1
                        setting.next_game = (c,d)
                elif d == (board_size) - 1:#Right Bottom Corner
                    if setting.position[a][b][c][d-1] == 1 or setting.position[a][b][c-1][d] == 1:
                        setting.position[a][b][c][d] = 0
                    else:
                        setting.position[a][b][c][d] = 2
                        setting.red_possible[a][b][c][d] = 'N'
                        setting.blue_possible[a][b][c][d] = 'N'
                        setting.red_possible[a][b][c][d-1] = 'N'
                        setting.red_possible[a][b][c-1][d] = 'N'
                        setting.k = setting.k + 1
                        setting.next_game = (c,d)
                else:
                    if (setting.position[a][b][c][d-1] == 1 
                        or setting.position[a][b][c][d+1] == 1 
                        or setting.position[a][b][c-1][d] == 1): 
                        setting.position[a][b][c][d] = 0
                    else:
                        setting.position[a][b][c][d] = 2
                        setting.red_possible[a][b][c][d] = 'N'
                        setting.blue_possible[a][b][c][d] = 'N'
                        setting.red_possible[a][b][c][d+1] = 'N'
                        setting.red_possible[a][b][c][d-1] = 'N'
                        setting.red_possible[a][b][c-1][d] = 'N'
                        setting.k = setting.k + 1
                        setting.next_game = (c,d)
            else:
                if d == 0:
                    if (setting.position[a][b][c][d+1] == 1 
                        or setting.position[a][b][c-1][d] == 1 
                        or setting.position[a][b][c+1][d] == 1):
                        setting.position[a][b][c][d] = 0
                    else:
                        setting.position[a][b][c][d] = 2
                        setting.red_possible[a][b][c][d] = 'N'
                        setting.blue_possible[a][b][c][d] = 'N'
                        setting.red_possible[a][b][c][d+1] = 'N'
                        setting.red_possible[a][b][c-1][d] = 'N'
                        setting.red_possible[a][b][c+1][d] = 'N'
                        setting.k = setting.k + 1
                        setting.next_game = (c,d)
                elif d == (board_size) - 1: #Right Bottom Corner
                    if (setting.position[a][b][c][d-1] == 1 
                        or setting.position[a][b][c-1][d] == 1 
                        or setting.position[a][b][c+1][d] == 1):
                        setting.position[a][b][c][d] = 0
                    else:
                        setting.position[a][b][c][d] = 2
                        setting.red_possible[a][b][c][d] = 'N'
                        setting.blue_possible[a][b][c][d] = 'N'
                        setting.red_possible[a][b][c][d-1] = 'N'
                        setting.red_possible[a][b][c-1][d] = 'N'
                        setting.red_possible[a][b][c+1][d] = 'N'
                        setting.k = setting.k + 1
                        setting.next_game = (c,d)
                else:
                    if (setting.position[a][b][c][d+1] == 1 
                        or setting.position[a][b][c][d-1] == 1 
                        or setting.position[a][b][c-1][d] == 1 
                        or setting.position[a][b][c+1][d] == 1):
                        setting.position[a][b][c][d] = 0
                    else:
                        setting.position[a][b][c][d] = 2
                        setting.red_possible[a][b][c][d] = 'N'
                        setting.blue_possible[a][b][c][d] = 'N'
                        setting.red_possible[a][b][c][d-1] = 'N'
                        setting.red_possible[a][b][c][d+1] = 'N'
                        setting.red_possible[a][b][c-1][d] = 'N'
                        setting.red_possible[a][d][c+1][d] = 'N'
                        setting.k = setting.k + 1
                        setting.next_game = (c,d)
    #Big Board Instruction:
    if (setting.Big_board_position[a][b] == 0
        and (setting.small_center_list[a][b][0][0][0] < pos[0]
        and pos[0] < setting.small_center_list[a][b][board_size-1][board_size-1][0]
        and setting.small_center_list[a][b][0][0][1] < pos[1]
        and pos[1] < setting.small_center_list[a][b][board_size-1][board_size-1][1]
        and (((setting.small_center_list[a][b][c][d][0] - setting.small_radius) > pos[0]
        or pos[0] > (setting.small_center_list[a][b][c][d][0] + setting.small_radius))
        and ((setting.small_center_list[a][b][c][d][1] - setting.small_radius) > pos[1]
        or pos[1] > (setting.small_center_list[a][b][c][d][1] + setting.small_radius))
        ))):   
        if setting.Win_con_op[a][b] == 1 and setting.k % 2 == 0:
            if a == 0:
                if b == 0: #Top Row
                    if setting.Big_board_position[a][b+1] == 2 or setting.Big_board_position[a+1][b] == 2:
                        setting.Big_board_position[a][b] = 0
                    else:
                        setting.Big_board_position[a][b] = 1
                        setting.Big_board_possible_red[a][b] = 'N'
                        setting.Big_board_possible_blue[a][b] = 'N'
                        setting.Big_board_possible_blue[a][b+1] = 'N'
                        setting.Big_board_possible_blue[a+1][b] = 'N'
                        setting.k = setting.k + 1
                        setting.Win_con_op[a][b] = 0
                elif b == (board_size) - 1:
                    if setting.Big_board_position[a][b-1] == 2 or setting.Big_board_position[a+1][b] == 2:
                        setting.Big_board_position[a][b] = 0
                    else:
                        setting.Big_board_position[a][b] = 1
                        setting.Big_board_possible_red[a][b] = 'N'
                        setting.Big_board_possible_blue[a][b] = 'N'
                        setting.Big_board_possible_blue[a][b-1] = 'N'
                        setting.Big_board_possible_blue[a+1][b] = 'N'
                        setting.k = setting.k + 1
                        setting.Win_con_op[a][b] = 0
                else:
                    if (setting.Big_board_position[a][b-1] == 2 
                            or setting.Big_board_position[a][b+1] == 2 
                            or setting.Big_board_position[a+1][b] == 2): 
                        setting.Big_board_position[a][b] = 0
                    else:
                        setting.Big_board_position[a][b] = 1
                        setting.Big_board_possible_red[a][b] = 'N'
                        setting.Big_board_possible_blue[a][b] = 'N'
                        setting.Big_board_possible_blue[a][b-1] = 'N'
                        setting.Big_board_possible_blue[a][b+1] = 'N'
                        setting.Big_board_possible_blue[a+1][b] = 'N'
                        setting.k = setting.k + 1
                        setting.Win_con_op[a][b] = 0
            elif a == (board_size) - 1: #Bottom Row
                if b == 0:
                    if setting.Big_board_position[a][b+1] == 2 or setting.Big_board_position[a-1][b] == 2:
                        setting.Big_board_position[a][b] = 0
                    else:
                        setting.Big_board_position[a][b] = 1
                        setting.Big_board_possible_red[a][b] = 'N'
                        setting.Big_board_possible_blue[a][b] = 'N'
                        setting.Big_board_possible_blue[a][b+1] = 'N'
                        setting.Big_board_possible_blue[a-1][b] = 'N'
                        setting.k = setting.k + 1
                        setting.Win_con_op[a][b] = 0
                elif b == (board_size) - 1:
                    if setting.Big_board_position[a][b-1] == 2 or setting.Big_board_position[a-1][b] == 2:
                        setting.Big_board_position[a][b] = 0
                    else:
                        setting.Big_board_position[a][b] = 1
                        setting.Big_board_possible_red[a][b] = 'N'
                        setting.Big_board_possible_blue[a][b] = 'N'
                        setting.Big_board_possible_blue[a][b-1] = 'N'
                        setting.Big_board_possible_blue[a-1][b] = 'N'
                        setting.k = setting.k + 1
                        setting.Win_con_op[a][b] = 0
                else:
                    if (setting.Big_board_position[a][b-1] == 2 
                        or setting.Big_board_position[a][b+1] == 2
                        or setting.Big_board_position[a-1][b] == 2):
                        setting.Big_board_position[a][b] = 0
                    else:
                        setting.Big_board_position[a][b] = 1
                        setting.Big_board_possible_red[a][b] = 'N'
                        setting.Big_board_possible_blue[a][b] = 'N'
                        setting.Big_board_possible_blue[a][b-1] = 'N'
                        setting.Big_board_possible_blue[a][b+1] = 'N'
                        setting.Big_board_possible_blue[a-1][b] = 'N'
                        setting.k = setting.k + 1
                        setting.Win_con_op[a][b] = 0
            else:   
                if b == 0:
                    if (setting.Big_board_position[a][b+1] == 2 
                        or setting.Big_board_position[a-1][b] == 2
                        or setting.Big_board_position[a+1][b] == 2):
                        setting.Big_board_position[a][b] = 0
                    else:
                        setting.Big_board_position[a][b] = 1
                        setting.Big_board_possible_red[a][b] = 'N'
                        setting.Big_board_possible_blue[a][b] = 'N'
                        setting.Big_board_possible_blue[a][b+1] = 'N'
                        setting.Big_board_possible_blue[a-1][b] = 'N'
                        setting.Big_board_possible_blue[a+1][b] = 'N'
                        setting.k = setting.k + 1
                        setting.Win_con_op[a][b] = 0
                elif b == (board_size) - 1:
                    if (setting.Big_board_position[a][b-1] == 2 
                        or setting.Big_board_position[a-1][b] == 2
                        or setting.Big_board_position[a+1][b] == 2):
                        setting.Big_board_position[a][b] = 0
                    else:
                        setting.Big_board_position[a][b] = 1
                        setting.Big_board_possible_red[a][b] = 'N'
                        setting.Big_board_possible_blue[a][b] = 'N'
                        setting.Big_board_possible_blue[a][b-1] = 'N'
                        setting.Big_board_possible_blue[a-1][b] = 'N'
                        setting.Big_board_possible_blue[a+1][b] = 'N'
                        setting.k = setting.k + 1
                        setting.Win_con_op[a][b] = 0
                else:
                    if (setting.Big_board_position[a][b+1] == 2
                        or setting.Big_board_position[a][b-1] == 2 
                        or setting.Big_board_position[a-1][b] == 2
                        or setting.Big_board_position[a+1][b] == 2):
                        setting.Big_board_position[a][b] = 0
                    else:
                        setting.Big_board_position[a][b] = 1
                        setting.Big_board_possible_red[a][b] = 'N'
                        setting.Big_board_possible_blue[a][b] = 'N'
                        setting.Big_board_possible_blue[a][b+1] = 'N'
                        setting.Big_board_possible_blue[a][b-1] = 'N'
                        setting.Big_board_possible_blue[a+1][b] = 'N'
                        setting.Big_board_possible_blue[a-1][b] = 'N'
                        setting.k = setting.k + 1
                        setting.Win_con_op[a][b] = 0
        elif (setting.Win_con_op[a][b] == 2 and setting.k % 2 == 1):
            if a == 0:
                if b == 0: #Top Row
                    if setting.Big_board_position[a][b+1] == 1 or setting.Big_board_position[a+1][b] == 1:
                        setting.Big_board_position[a][b] = 0
                    else:
                        setting.Big_board_position[a][b] = 2
                        setting.Big_board_possible_red[a][b] = 'N'
                        setting.Big_board_possible_blue[a][b] = 'N'
                        setting.Big_board_possible_red[a][b+1] = 'N'
                        setting.Big_board_possible_red[a+1][b] = 'N'
                        setting.k = setting.k + 1
                        setting.Win_con_op[a][b] = 0
                elif b == (board_size) - 1:
                    if setting.Big_board_position[a][b-1] == 1 or setting.Big_board_position[a+1][b] == 1:
                        setting.Big_board_position[a][b] = 0
                    else:
                        setting.Big_board_position[a][b] = 2
                        setting.Big_board_possible_red[a][b] = 'N'
                        setting.Big_board_possible_blue[a][b] = 'N'
                        setting.Big_board_possible_red[a][b-1] = 'N'
                        setting.Big_board_possible_red[a+1][b] = 'N'
                        setting.k = setting.k + 1
                        setting.Win_con_op[a][b] = 0
                else:
                    if (setting.Big_board_position[a][b-1] == 1 
                            or setting.Big_board_position[a][b+1] == 1 
                            or setting.Big_board_position[a+1][b] == 1): 
                        setting.Big_board_position[a][b] = 0
                    else:
                        setting.Big_board_position[a][b] = 2
                        setting.Big_board_possible_red[a][b] = 'N'
                        setting.Big_board_possible_blue[a][b] = 'N'
                        setting.Big_board_possible_red[a][b-1] = 'N'
                        setting.Big_board_possible_red[a][b+1] = 'N'
                        setting.Big_board_possible_red[a+1][b] = 'N'
                        setting.k = setting.k + 1
                        setting.Win_con_op[a][b] = 0
            elif a == (board_size) - 1: #Bottom Row
                if b == 0:
                    if setting.Big_board_position[a][b+1] == 1 or setting.Big_board_position[a-1][b] == 1:
                        setting.Big_board_position[a][b] = 0
                    else:
                        setting.Big_board_position[a][b] = 2
                        setting.Big_board_possible_red[a][b] = 'N'
                        setting.Big_board_possible_blue[a][b] = 'N'
                        setting.Big_board_possible_red[a][b+1] = 'N'
                        setting.Big_board_possible_red[a-1][b] = 'N'
                        setting.k = setting.k + 1
                        setting.Win_con_op[a][b] = 0
                elif b == (board_size) - 1:
                    if setting.Big_board_position[a][b-1] == 1 or setting.Big_board_position[a-1][b] == 1:
                        setting.Big_board_position[a][b] = 0
                    else:
                        setting.Big_board_position[a][b] = 2
                        setting.Big_board_possible_red[a][b] = 'N'
                        setting.Big_board_possible_blue[a][b] = 'N'
                        setting.Big_board_possible_red[a][b-1] = 'N'
                        setting.Big_board_possible_red[a-1][b] = 'N'
                        setting.k = setting.k + 1
                        setting.Win_con_op[a][b] = 0
                else:
                    if (setting.Big_board_position[a][b-1] == 1 
                        or setting.Big_board_position[a][b+1] == 1
                        or setting.Big_board_position[a-1][b] == 1):
                        setting.Big_board_position[a][b] = 0
                    else:
                        setting.Big_board_position[a][b] = 2
                        setting.Big_board_possible_red[a][b] = 'N'
                        setting.Big_board_possible_blue[a][b] = 'N'
                        setting.Big_board_possible_red[a][b-1] = 'N'
                        setting.Big_board_possible_red[a][b+1] = 'N'
                        setting.Big_board_possible_red[a-1][b] = 'N'
                        setting.k = setting.k + 1
                        setting.Win_con_op[a][b] = 0
            else:   
                if b == 0:
                    if (setting.Big_board_position[a][b+1] == 1 
                        or setting.Big_board_position[a-1][b] == 1
                        or setting.Big_board_position[a+1][b] == 1):
                        setting.Big_board_position[a][b] = 0
                    else:
                        setting.Big_board_position[a][b] = 2
                        setting.Big_board_possible_red[a][b] = 'N'
                        setting.Big_board_possible_blue[a][b] = 'N'
                        setting.Big_board_possible_red[a][b+1] = 'N'
                        setting.Big_board_possible_red[a-1][b] = 'N'
                        setting.Big_board_possible_red[a+1][b] = 'N'
                        setting.k = setting.k + 1
                        setting.Win_con_op[a][b] = 0
                elif b == (board_size) - 1:
                    if (setting.Big_board_position[a][b-1] == 1 
                        or setting.Big_board_position[a-1][b] == 1
                        or setting.Big_board_position[a+1][b] == 1):
                        setting.Big_board_position[a][b] = 0
                    else:
                        setting.Big_board_position[a][b] = 2
                        setting.Big_board_possible_red[a][b] = 'N'
                        setting.Big_board_possible_blue[a][b] = 'N'
                        setting.Big_board_possible_red[a][b-1] = 'N'
                        setting.Big_board_possible_red[a-1][b] = 'N'
                        setting.Big_board_possible_red[a+1][b] = 'N'
                        setting.k = setting.k + 1
                        setting.Win_con_op[a][b] = 0
                else:
                    if (setting.Big_board_position[a][b+1] == 1
                        or setting.Big_board_position[a][b-1] == 1 
                        or setting.Big_board_position[a-1][b] == 1
                        or setting.Big_board_position[a+1][b] == 1):
                        setting.Big_board_position[a][b] = 0
                    else:
                        setting.Big_board_position[a][b] = 2
                        setting.Big_board_possible_red[a][b] = 'N'
                        setting.Big_board_possible_blue[a][b] = 'N'
                        setting.Big_board_possible_red[a][b+1] = 'N'
                        setting.Big_board_possible_red[a][b-1] = 'N'
                        setting.Big_board_possible_red[a+1][b] = 'N'
                        setting.Big_board_possible_red[a-1][b] = 'N'
                        setting.k = setting.k + 1
                        setting.Win_con_op[a][b] = 0