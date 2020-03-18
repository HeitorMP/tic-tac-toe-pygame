import pygame

pygame.init()
#teste

def draw_playfield():
    width_horizon = 20
    height_horizon = 400
    x_horizon = 175
    y_horizon = 50

    width_vert = 400
    height_vert = 20
    x_vert = 50
    y_vert = 175

    pygame.draw.rect(main_window, (255, 0, 0), (x_horizon, y_horizon, width_horizon, height_horizon))
    pygame.draw.rect(main_window, (255, 0, 0), ((x_horizon + 140), y_horizon, width_horizon, height_horizon))
    pygame.draw.rect(main_window, (255, 0, 0), (x_vert, y_vert, width_vert, height_vert))
    pygame.draw.rect(main_window, (255, 0, 0), (x_vert, (y_vert + 130), width_vert, height_vert))


def checkVictory(flist):
    print(flist)
    temp_colum = [0, 0, 0]

    if (flist[0][0] == flist[1][1] and flist[1][1] == flist[2][2] and flist[0][0] != 0):
        return True
    elif (flist[0][2] == flist[1][1] and flist[1][1] == flist[2][0] and flist[0][2] != 0):
        return True
    for lines in range(0, 3):
        if (flist[lines] == [1, 1, 1] or flist[lines] == [2, 2, 2]):
            return True
        else:
            for coluns in range(0, 3):
                temp_colum[coluns] = flist[coluns][lines]
            if (temp_colum == [1, 1, 1] or temp_colum == [2, 2, 2]):
                return True


main_window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("HMP tic-tac-toe")

playfield = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
column = 0
line = 0

playerOturn = False
turns = 0
invalid = True
game_over = False

spritex = 0
spritey = 0

click = False
mouse_x = 0
mouse_y = 0

### Sprites
playerX_sprite = pygame.image.load("x.png").convert_alpha()
playerO_sprite = pygame.image.load("o.png").convert_alpha()

###### MAIN LOOP ######
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            click = True

    # Desenha o playfield
    draw_playfield()

    if click:
        if mouse_x < 45 or mouse_y < 48:
            invalid = True
        elif mouse_x < 174 and mouse_y < 174:
            spritex = 70
            spritey = 70
            line = 0
            column = 0
            invalid = False
        elif mouse_x < 314 and mouse_y < 174:
            spritex = 215
            spritey = 70
            line = 0
            column = 1
            invalid = False
        elif mouse_x < 448 and mouse_y < 174:
            spritex = 360
            spritey = 70
            line = 0
            column = 2
            invalid = False
        elif mouse_x < 174 and mouse_y < 303:
            spritex = 70
            spritey = 200
            line = 1
            column = 0
            invalid = False
        elif mouse_x < 314 and mouse_y < 303:
            spritex = 215
            spritey = 200
            line = 1
            column = 1
            invalid = False
        elif mouse_x < 448 and mouse_y < 303:
            spritex = 360
            spritey = 200
            line = 1
            column = 2
            invalid = False
        elif mouse_x < 174 and mouse_y < 450:
            spritex = 70
            spritey = 350
            line = 2
            column = 0
            invalid = False
        elif mouse_x < 314 and mouse_y < 450:
            spritex = 215
            spritey = 350
            line = 2
            column = 1
            invalid = False
        elif mouse_x < 448 and mouse_y < 450:
            spritex = 360
            spritey = 350
            line = 2
            column = 2
            invalid = False
        else:
            invalid = True


    # posiciona os sprites
    if turns % 2 == 0:
        playerOturn = True
    else:
        playerOturn = False

    # 1 = O
    # 2 = X
    if playerOturn and invalid is False and playfield[line][column] == 0:
        playfield[line][column] = 1
        turns += 1
        main_window.blit(playerO_sprite, (spritex,spritey))
    elif playerOturn is False and invalid is False and playfield[line][column] == 0:
        playfield[line][column] = 2
        turns += 1
        main_window.blit(playerX_sprite, (spritex, spritey))

    game_over = checkVictory(playfield)
    if game_over:
        print("game_over")
        run = False

    pygame.display.update()

run_game_over = True
while game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = False
    pygame.display.update()

pygame.quit()
