import pygame
import random
import time
########################### EAN DEN THES NA VLEPEIS TA PLOIA TOY ANTIPALOU
########################### KANE COMMENT TI GRAMMI 284
pygame.init()
###### time delay between rounds #########
xrono_anamonis = 0.1
#########################################
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
bright_red=(255,0,0)
bright_green=(0,255,0)
computer_ships=[]
gameDisplay = pygame.display.set_mode((1400,700))
gameDisplay.fill(white)
clock=pygame.time.Clock()
##################################################################################################################################################################################
def message_display(text,x,y):

    pygame.draw.rect(gameDisplay, white, (x-600,y-30,1200,60))
    smallText = pygame.font.SysFont("arial",40) #grammatoseira kai megethos
    TextSurf, TextRect = text_objects(text, smallText)
    TextRect.center=(x,y)
    
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()

def text_objects(text,font):
    textSurface = font.render(text, True, black)
    return textSurface,textSurface.get_rect()

########################################################################################################################################################################################################
def grammes():
    for i in range (70,600,50):
        pygame.draw.line(gameDisplay, black,(i,40),(i,540),5)
    for i in range (40,550,50):
        pygame.draw.line(gameDisplay, black,(70,i),(570,i),5)
    for i in range (800,1350,50):
        pygame.draw.line(gameDisplay, black,(i,40),(i,540),5)
    for i in range (40,550,50):
        pygame.draw.line(gameDisplay, black,(800,i),(1300,i),5)
####################################################################################################################################################################################################
def enemy_ships(): #dinei enan pinaka me tis egkures theseis twn 5 ploiwn
    enemy_ship_pos_x=[0]
    enemy_ship_pos_y=[0]
    z=0
    while z<5:
        valid_pos=0
        x=random.randrange(80,530,50)
        y = random.randrange(50,500,50)

        while x in enemy_ship_pos_x:
            x=random.randrange(80,530,50)
        enemy_ship_pos_x.append(x)
     
        while y in enemy_ship_pos_y:
            y = random.randrange(50,500,50)
        enemy_ship_pos_y.append(y)

        if z == 0:
            ship1=[[enemy_ship_pos_x[1],enemy_ship_pos_y[1]]]
            turn=True
            for i in range(1,2):
                while turn:   
                    x = random.randrange(1,4)
                    turn=False
                if x == 1:
                    ship1.append([(enemy_ship_pos_x[i] + 50), enemy_ship_pos_y[i]])
                elif x ==2:
                    ship1.append([enemy_ship_pos_x[i], (enemy_ship_pos_y[i] + 50)])      #[[230,30],[230,42]]
                elif x==3:
                    ship1.append([(enemy_ship_pos_x[i] - 50), enemy_ship_pos_y[i]])
                else:
                    ship1.append([enemy_ship_pos_x[i], (enemy_ship_pos_y[i] - 50)])
            for i in range(2):
                for j in range(2):
                    if ship1[i][j] < 0:
                        valid_pos=1
                        z=-1
                if 80 > ship1[i][0] or ship1[i][0] >530 or ship1[i][1]<50 or ship1[i][1]>500:
                    valid_pos=1
                    z=-1
        elif z==1:
            ship2=[[enemy_ship_pos_x[2],enemy_ship_pos_y[2]]]
            turn=True
            for i in range (1,3):
                while turn:   
                    x = random.randrange(1,4)
                    turn=False
                if x == 1:
                    ship2.append([(enemy_ship_pos_x[2] + i*50), enemy_ship_pos_y[2]])
                elif x ==2:
                    ship2.append([enemy_ship_pos_x[2], (enemy_ship_pos_y[2] + i*50)])
                elif x==3:
                    ship2.append([(enemy_ship_pos_x[2] - i*50), enemy_ship_pos_y[2]])
                else:
                    ship2.append([enemy_ship_pos_x[2], (enemy_ship_pos_y[2] - i*50)])
            for i in range (3):
                if ship2[i] in ship1:
                    valid_pos=2
                    z=0
                if 80 > ship2[i][0] or ship2[i][0] >530 or ship2[i][1]<50 or ship2[i][1]>500:
                    valid_pos=2
                    z=0
                for j in range(2):
                    if ship2[i][j] < 0:
                        valid_pos=2
                        z=0           
        elif z==2:
            ship3=[[enemy_ship_pos_x[3],enemy_ship_pos_y[3]]]
            turn=True
            for i in range (1,3):
                while turn:   
                    x = random.randrange(1,4)
                    turn=False
                if x == 1:
                    ship3.append([(enemy_ship_pos_x[3] + i*50), enemy_ship_pos_y[3]])
                elif x ==2:
                    ship3.append([enemy_ship_pos_x[3], (enemy_ship_pos_y[3] + i*50)])
                elif x==3:
                    ship3.append([(enemy_ship_pos_x[3] - i*50), enemy_ship_pos_y[3]])
                else:
                    ship3.append([(enemy_ship_pos_x[3] - i*50), enemy_ship_pos_y[3]])
            for i in range(3):
                if ship3[i] in ship2 or ship3[i] in ship1:
                    valid_pos=3
                    z=1
                if 80 > ship3[i][0] or ship3[i][0] >530 or ship3[i][1]<50 or ship3[i][1]>500:
                    valid_pos=3
                    z=1
                for j in range(2) :
                    if ship3[i][j] < 0:
                        valid_pos=3
                        z=1
        elif z==3:
            ship4=[[enemy_ship_pos_x[4],enemy_ship_pos_y[4]]]
            turn=True
            for i in range (1,4):
                while turn:   
                    x = random.randrange(1,4)
                    turn=False
                if x == 1:
                    ship4.append([(enemy_ship_pos_x[4] + i*50), enemy_ship_pos_y[4]])
                elif x ==2:
                    ship4.append([enemy_ship_pos_x[4], (enemy_ship_pos_y[4] + i*50)])
                elif x==3:
                    ship4.append([(enemy_ship_pos_x[4] - i*50), enemy_ship_pos_y[4]])
                else:
                    ship4.append([enemy_ship_pos_x[4], (enemy_ship_pos_y[4] - i*50)])
            for i in range(4):
                if ship4[i] in ship1 or ship4[i] in ship2 or ship4[i] in ship3 :
                    valid_pos=4
                    z=2
                if 80 > ship4[i][0] or ship4[i][0] >530 or ship4[i][1]<50 or ship4[i][1]>500:
                    valid_pos=4
                    z=2
                for j in range(2):
                    if ship4[i][j] < 0:
                        valid_pos=4
                        z=2
        elif z==4:
            ship5=[[enemy_ship_pos_x[5],enemy_ship_pos_y[5]]]
            turn=True
            for i in range (1,5):
                while turn:   
                    x = random.randrange(1,4)
                    turn=False
                if x == 1:
                    ship5.append([(enemy_ship_pos_x[5] + i*50), enemy_ship_pos_y[5]])
                elif x ==2:
                    ship5.append([enemy_ship_pos_x[5], (enemy_ship_pos_y[5] + i*50)])
                elif x==3:
                    ship5.append([(enemy_ship_pos_x[5] - i*50), enemy_ship_pos_y[5]])
                else:
                    ship5.append([enemy_ship_pos_x[5], (enemy_ship_pos_y[5] - i*50)])
            for i in range(5):
                if ship5[i] in ship1 or ship5[i] in ship2 or ship5[i] in ship3 or ship5[i] in ship4:
                    valid_pos=5
                    z=3
                if 80 > ship5[i][0] or ship5[i][0] >530 or ship5[i][1]<50 or ship5[i][1]>500:
                    valid_pos=5
                    z=3
                for j in range(2):
                    if ship5[i][j] < 0:
                        valid_pos=5
                        z=3

        if valid_pos == 1:
            enemy_ship_pos_x.pop()
            enemy_ship_pos_y.pop()
            ship1.pop()
            ship1.pop()
        elif valid_pos == 2:
            enemy_ship_pos_x.pop()
            enemy_ship_pos_y.pop()
            ship2.pop()
            ship2.pop()
            ship2.pop()
        elif valid_pos== 3:
            enemy_ship_pos_x.pop()
            enemy_ship_pos_y.pop()
            ship3.pop()
            ship3.pop()
            ship3.pop()
        elif valid_pos == 4:
            enemy_ship_pos_x.pop()
            enemy_ship_pos_y.pop()
            ship4.pop()
            ship4.pop()
            ship4.pop()
            ship4.pop()
        elif valid_pos == 5:
            enemy_ship_pos_x.pop()
            enemy_ship_pos_y.pop()
            ship5.pop()
            ship5.pop()
            ship5.pop()
            ship5.pop()
            ship5.pop()
            
        z+=1
    return ship1,ship2,ship3,ship4,ship5
####################################################################################################################################################################################################
def rects():
    position_list = []
    for i in range(80,560,50):
        pygame.draw.rect(gameDisplay, blue, (i,50,30,30))
        position_list.append((i,50,30,30))

        for j in range (100,550,50):
            pygame.draw.rect(gameDisplay,blue, (i,j,30,30))
            position_list.append((i,j,30,30))
    return position_list
####################################################################################################################################################################################################
def button1(x1,y1,w1,h1,mouse,click):
    for i in range(len(x1)):
        if x1[i]+w1[i] > mouse[0] and mouse[0] > x1[i] and y1[i] + h1[i] > mouse[1] and mouse[1] >y1[i]:
            if click[0]==1:
                return [x1[i], y1[i]]
    return[0,0]
####################################################################################################################################################################################################
gameExit = False 
def game_loop():
    gameDisplay.fill(white)
    pygame.display.update()
    loop_one_time=True
############### player
    position_list2 = rects2()
    player_who_plays = 1
    all_shoots=[]
    my_ships=[]
########################
    for i in range(len(position_list2)):
        my_ships.append([position_list2[i][0],position_list2[i][1]])
    print (player_ships)
    
    while not gameExit:
        pygame.display.update()
        while loop_one_time:
            grammes()
            x,y,z,c,v = enemy_ships()
            enemy_location_ships = []
            enemy_location_ships.append(x)
            enemy_location_ships.append(y)
            enemy_location_ships.append(z)
            enemy_location_ships.append(c)
            enemy_location_ships.append(v)
            loop_one_time=False
            searching = False  
            periptwsi = 1
            position_list=rects()
            x1=[]
            y1=[]
            w1=[]
            h1=[]
            for i in range(len(player_ships)):
                for j in range(len(player_ships[i])):
                    pygame.draw.rect(gameDisplay, green, (player_ships[i][j][0],player_ships[i][j][1],30,30))
########### prepei na diagrafei meta i katw grammi
      #              pygame.draw.rect(gameDisplay, green, (enemy_location_ships[i][j][0],enemy_location_ships[i][j][1],30,30))
            for i in range (len(position_list)):
                x1.append(position_list[i][0])
                y1.append(position_list[i][1])
                w1.append(position_list[i][2])
                h1.append(position_list[i][3])
            score_computer = 0
            score_player = 0
            guess=[]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                legal_move = button1(x1,y1,w1,h1,mouse,click)
                if legal_move != [0,0]:
                    if legal_move in guess:
                        print ("to ksanapatises")
                    else:
                        guess.append(legal_move)
                        zzz=0
                        for i in range(5):
                            if zzz==1:
                                break                       
                            for j in range(len(enemy_location_ships[i])):
                                if legal_move == enemy_location_ships[i][j]:
                                    message_display("Success! You got one!", 500,600)
                                    pygame.draw.rect(gameDisplay,red, (legal_move[0],legal_move[1],30,30))
                                    zzz=1
                                    score_player += 1
                                    break
                                else:
                                    pygame.draw.rect(gameDisplay,white, (legal_move[0],legal_move[1],30,30))
                                    message_display("Better luck next time...", 500,600)

                        time.sleep(xrono_anamonis)
########################################################### AI
                        while True:
                            shoot_success = False    
                            if searching == False:
                                shoot = random.choice(my_ships)
                                while shoot in all_shoots:
                                    shoot = random.choice(my_ships)
                                    print ("pali opou na nai varas re pc")
                                all_shoots.append(shoot)
                                for i in range(len(player_ships)):
                                    for j in range(len(player_ships[i])):
                                        if shoot == player_ships[i][j]:
                                            shoot_success = True
                                            searching = True
                                            shoot_searching = shoot
                            
                            elif searching == True:
                                if periptwsi == 1:
                                    shoot = [shoot_searching[0]+50,shoot_searching[1]]
                                    if shoot in all_shoots or not (shoot in my_ships):
                                        print ("pali opou na nai varas re pc")
                                        periptwsi = 18
                                        continue
                                    else:
                                        all_shoots.append(shoot)
                                        for i in range(len(player_ships)):
                                            for j in range(len(player_ships[i])):
                                                if shoot == player_ships[i][j]:
                                                    shoot_success = True
                                        if shoot_success == True:
                                            periptwsi = 2
                                        else:
                                            periptwsi = 18
                                        
                                elif periptwsi == 2:
                                    shoot = [shoot_searching[0]+100,shoot_searching[1]]
                                    if shoot in all_shoots or not (shoot in my_ships):
                                        print ("pali opou na nai varas re pc")
                                        periptwsi = 12
                                        continue
                                    else:
                                        all_shoots.append(shoot)
                                        for i in range(len(player_ships)):
                                            for j in range(len(player_ships[i])):
                                                if shoot == player_ships[i][j]:
                                                    shoot_success = True
                                        if shoot_success == True:
                                            periptwsi = 3
                                        else:
                                            periptwsi = 12
                                        
                                elif periptwsi == 3:
                                    shoot = [shoot_searching[0]+150,shoot_searching[1]]
                                    if shoot in all_shoots or not (shoot in my_ships):
                                        print ("pali opou na nai varas re pc")
                                        periptwsi = 8
                                        continue
                                    else:
                                        all_shoots.append(shoot)
                                        for i in range(len(player_ships)):
                                            for j in range(len(player_ships[i])):
                                                if shoot == player_ships[i][j]:
                                                    shoot_success = True
                                        if shoot_success == True:
                                            periptwsi = 4
                                        else:
                                            periptwsi = 8

                                elif periptwsi == 4:
                                    shoot = [shoot_searching[0]+200,shoot_searching[1]]
                                    if shoot in all_shoots or not (shoot in my_ships):
                                        print ("pali opou na nai varas re pc")
                                        periptwsi = 6
                                        continue
                                    else:
                                        all_shoots.append(shoot)
                                        for i in range(len(player_ships)):
                                            for j in range(len(player_ships[i])):
                                                if shoot == player_ships[i][j]:
                                                    shoot_success = True
                                        if shoot_success == True:
                                            searching = False
                                            periptwsi = 1
                                        else:
                                            periptwsi = 6

                                elif periptwsi == 6:
                                    shoot = [shoot_searching[0]-50,shoot_searching[1]]
                                    if shoot in all_shoots or not (shoot in my_ships):
                                        print ("pali opou na nai varas re pc")
                                        searching = False
                                        periptwsi = 1
                                        continue
                                    else:
                                        all_shoots.append(shoot)
                                        for i in range(len(player_ships)):
                                            for j in range(len(player_ships[i])):
                                                if shoot == player_ships[i][j]:
                                                    shoot_success = True
                                        if shoot_success == True:
                                            searching = False
                                            periptwsi = 1
                                        else:
                                            searching = False
                                            periptwsi = 1

                                elif periptwsi == 8:
                                    shoot = [shoot_searching[0]-50,shoot_searching[1]]
                                    if shoot in all_shoots or not (shoot in my_ships):
                                        print ("pali opou na nai varas re pc")
                                        searching = False
                                        periptwsi = 1
                                        continue
                                    else:
                                        all_shoots.append(shoot)
                                        for i in range(len(player_ships)):
                                            for j in range(len(player_ships[i])):
                                                if shoot == player_ships[i][j]:
                                                    shoot_success = True
                                        if shoot_success == True:
                                            periptwsi = 10
                                        else:
                                            searching = False
                                            periptwsi = 1

                                elif periptwsi == 10:
                                    shoot = [shoot_searching[0]-100,shoot_searching[1]]
                                    if shoot in all_shoots or not (shoot in my_ships):
                                        print ("pali opou na nai varas re pc")
                                        searching = False
                                        periptwsi = 1
                                        continue
                                    else:
                                        all_shoots.append(shoot)
                                        for i in range(len(player_ships)):
                                            for j in range(len(player_ships[i])):
                                                if shoot == player_ships[i][j]:
                                                    shoot_success = True
                                        if shoot_success == True:
                                            searching = False
                                            pwriptwsi = 1
                                        else:
                                            periptwsi = 1
                                            searching = False

                                elif periptwsi == 12:
                                    shoot = [shoot_searching[0]-50,shoot_searching[1]]
                                    if shoot in all_shoots or not (shoot in my_ships):
                                        print ("pali opou na nai varas re pc")
                                        searching = False
                                        periptwsi = 1
                                        continue
                                    else:
                                        all_shoots.append(shoot)
                                        for i in range(len(player_ships)):
                                            for j in range(len(player_ships[i])):
                                                if shoot == player_ships[i][j]:
                                                    shoot_success = True
                                        if shoot_success == True:
                                            periptwsi = 14
                                        else:
                                            searching = False
                                            periptwsi = 1


                                elif periptwsi == 14:
                                    shoot = [shoot_searching[0]-100,shoot_searching[1]]
                                    if shoot in all_shoots or not (shoot in my_ships):
                                        print ("pali opou na nai varas re pc")
                                        searching = False
                                        periptwsi = 1
                                        continue
                                    else:
                                        all_shoots.append(shoot)
                                        for i in range(len(player_ships)):
                                            for j in range(len(player_ships[i])):
                                                if shoot == player_ships[i][j]:
                                                    shoot_success = True
                                        if shoot_success == True:
                                            periptwsi = 15
                                        else:
                                            searching = False
                                            periptwsi = 1

                                elif periptwsi == 15:
                                    shoot = [shoot_searching[0]-150,shoot_searching[1]]
                                    if shoot in all_shoots or not (shoot in my_ships):
                                        print ("pali opou na nai varas re pc")
                                        searching = False
                                        periptwsi = 1
                                        continue
                                    else:
                                        all_shoots.append(shoot)
                                        for i in range(len(player_ships)):
                                            for j in range(len(player_ships[i])):
                                                if shoot == player_ships[i][j]:
                                                    shoot_success = True
                                        if shoot_success == True:
                                            searching = False
                                            pwriptwsi = 1
                                        else:
                                            searching = False
                                            periptwsi = 1
#########################################################################
                                elif periptwsi == 18:
                                    shoot = [shoot_searching[0],shoot_searching[1]+50]
                                    if shoot in all_shoots or not (shoot in my_ships):
                                        print ("pali opou na nai varas re pc")
                                        periptwsi = 19
                                        continue
                                    else:
                                        all_shoots.append(shoot)
                                        for i in range(len(player_ships)):
                                            for j in range(len(player_ships[i])):
                                                if shoot == player_ships[i][j]:
                                                    shoot_success = True
                                        if shoot_success == True:
                                            periptwsi = 20
                                        else:
                                            periptwsi = 19

                                elif periptwsi == 20:
                                    shoot = [shoot_searching[0],shoot_searching[1]+100]
                                    if shoot in all_shoots or not (shoot in my_ships):
                                        print ("pali opou na nai varas re pc")
                                        periptwsi = 26
                                        continue
                                    else:
                                        all_shoots.append(shoot)
                                        for i in range(len(player_ships)):
                                            for j in range(len(player_ships[i])):
                                                if shoot == player_ships[i][j]:
                                                    shoot_success = True
                                        if shoot_success == True:
                                            periptwsi = 21
                                        else:
                                            periptwsi = 26

                                elif periptwsi == 21:
                                    shoot = [shoot_searching[0],shoot_searching[1]+150]
                                    if shoot in all_shoots or not (shoot in my_ships):
                                        print ("pali opou na nai varas re pc")
                                        periptwsi = 45
                                        continue
                                    else:
                                        all_shoots.append(shoot)
                                        for i in range(len(player_ships)):
                                            for j in range(len(player_ships[i])):
                                                if shoot == player_ships[i][j]:
                                                    shoot_success = True
                                        if shoot_success == True:
                                            periptwsi = 22
                                        else:
                                            periptwsi = 45

                                elif periptwsi == 22:
                                    shoot = [shoot_searching[0],shoot_searching[1]+200]
                                    if shoot in all_shoots or not (shoot in my_ships):
                                        print ("pali opou na nai varas re pc")
                                        periptwsi = 24
                                        continue
                                    else:
                                        all_shoots.append(shoot)
                                        for i in range(len(player_ships)):
                                            for j in range(len(player_ships[i])):
                                                if shoot == player_ships[i][j]:
                                                    shoot_success = True
                                        if shoot_success == True:
                                            periptwsi = 1
                                            searvhing = False
                                        else:
                                            periptwsi = 24

                                elif periptwsi == 24:
                                    shoot = [shoot_searching[0],shoot_searching[1]-50]
                                    if shoot in all_shoots or not (shoot in my_ships):
                                        print ("pali opou na nai varas re pc")
                                        periptwsi = 1
                                        searching = False
                                        continue
                                    else:
                                        all_shoots.append(shoot)
                                        for i in range(len(player_ships)):
                                            for j in range(len(player_ships[i])):
                                                if shoot == player_ships[i][j]:
                                                    shoot_success = True
                                        if shoot_success == True:
                                            periptwsi = 1
                                            searching = False
                                        else:
                                            periptwsi = 1
                                            Searching = False

                                elif periptwsi == 45:
                                    shoot = [shoot_searching[0],shoot_searching[1]-50]
                                    if shoot in all_shoots or not (shoot in my_ships):
                                        print ("pali opou na nai varas re pc")
                                        periptwsi = 1
                                        searching = False
                                        continue
                                    else:
                                        all_shoots.append(shoot)
                                        for i in range(len(player_ships)):
                                            for j in range(len(player_ships[i])):
                                                if shoot == player_ships[i][j]:
                                                    shoot_success = True
                                        if shoot_success == True:
                                            periptwsi = 47
                                        else:
                                            periptwsi = 1
                                            searching = False

                                elif periptwsi == 47:
                                    shoot = [shoot_searching[0],shoot_searching[1]+50]
                                    if shoot in all_shoots or not (shoot in my_ships):
                                        print ("pali opou na nai varas re pc")
                                        periptwsi = 1
                                        searching = False
                                        continue
                                    else:
                                        all_shoots.append(shoot)
                                        for i in range(len(player_ships)):
                                            for j in range(len(player_ships[i])):
                                                if shoot == player_ships[i][j]:
                                                    shoot_success = True
                                        if shoot_success == True:
                                            periptwsi = 1
                                            searching = False
                                        else:
                                            periptwsi = 1
                                            searching = False

                                elif periptwsi == 26:
                                    shoot = [shoot_searching[0],shoot_searching[1]-50]
                                    if shoot in all_shoots or not (shoot in my_ships):
                                        print ("pali opou na nai varas re pc")
                                        periptwsi = 1
                                        searching = False
                                        continue
                                    else:
                                        all_shoots.append(shoot)
                                        for i in range(len(player_ships)):
                                            for j in range(len(player_ships[i])):
                                                if shoot == player_ships[i][j]:
                                                    shoot_success = True
                                        if shoot_success == True:
                                            periptwsi = 28
                                        else:
                                            periptwsi = 1
                                            searching = False

                                elif periptwsi == 28:
                                    shoot = [shoot_searching[0],shoot_searching[1]-100]
                                    if shoot in all_shoots or not (shoot in my_ships):
                                        print ("pali opou na nai varas re pc")
                                        periptwsi = 1
                                        searching = False
                                        continue
                                    else:
                                        all_shoots.append(shoot)
                                        for i in range(len(player_ships)):
                                            for j in range(len(player_ships[i])):
                                                if shoot == player_ships[i][j]:
                                                    shoot_success = True
                                        if shoot_success == True:
                                            periptwsi = 29
                                        else:
                                            periptwsi = 1
                                            searching = False

                                elif periptwsi == 29:
                                    shoot = [shoot_searching[0],shoot_searching[1]-150]
                                    if shoot in all_shoots or not (shoot in my_ships):
                                        print ("pali opou na nai varas re pc")
                                        periptwsi = 1
                                        searching = false
                                        continue
                                    else:
                                        all_shoots.append(shoot)
                                        for i in range(len(player_ships)):
                                            for j in range(len(player_ships[i])):
                                                if shoot == player_ships[i][j]:
                                                    shoot_success = True
                                        if shoot_success == True:
                                            periptwsi = 1
                                            searching = False
                                        else:
                                            periptwsi = 1
                                            searching = False
#######################################################################
                                elif periptwsi == 19:
                                    shoot = [shoot_searching[0]-50,shoot_searching[1]]
                                    if shoot in all_shoots or not (shoot in my_ships):
                                        print ("pali opou na nai varas re pc")
                                        periptwsi = 38
                                        continue
                                    else:
                                        all_shoots.append(shoot)
                                        for i in range(len(player_ships)):
                                            for j in range(len(player_ships[i])):
                                                if shoot == player_ships[i][j]:
                                                    shoot_success = True
                                        if shoot_success == True:
                                            periptwsi = 32
                                        else:
                                            periptwsi = 38

                                elif periptwsi == 32:
                                    shoot = [shoot_searching[0]-100,shoot_searching[1]]
                                    if shoot in all_shoots or not (shoot in my_ships):
                                        print ("pali opou na nai varas re pc")
                                        periptwsi = 1
                                        searching = False
                                        continue
                                    else:
                                        all_shoots.append(shoot)
                                        for i in range(len(player_ships)):
                                            for j in range(len(player_ships[i])):
                                                if shoot == player_ships[i][j]:
                                                    shoot_success = True
                                        if shoot_success == True:
                                            periptwsi = 33
                                        else:
                                            periptwsi = 1
                                            searching = False

                                elif periptwsi == 33:
                                    shoot = [shoot_searching[0]-150,shoot_searching[1]]
                                    if shoot in all_shoots or not (shoot in my_ships):
                                        print ("pali opou na nai varas re pc")
                                        periptwsi = 1
                                        searching = False
                                        continue
                                    else:
                                        all_shoots.append(shoot)
                                        for i in range(len(player_ships)):
                                            for j in range(len(player_ships[i])):
                                                if shoot == player_ships[i][j]:
                                                    shoot_success = True
                                        if shoot_success == True:
                                            periptwsi = 35
                                        else:
                                            periptwsi = 1
                                            searching = False

                                elif periptwsi == 35:
                                    shoot = [shoot_searching[0]-200,shoot_searching[1]]
                                    if shoot in all_shoots or not (shoot in my_ships):
                                        print ("pali opou na nai varas re pc")
                                        periptwsi = 1
                                        searching = False
                                        continue
                                    else:
                                        all_shoots.append(shoot)
                                        for i in range(len(player_ships)):
                                            for j in range(len(player_ships[i])):
                                                if shoot == player_ships[i][j]:
                                                    shoot_success = True
                                        if shoot_success == True:
                                            periptwsi = 1
                                            searching = False
                                        else:
                                            periptwsi = 1
                                            searching = False
#############################################################################
                                elif periptwsi == 38:
                                    shoot = [shoot_searching[0],shoot_searching[1]-50]
                                    if shoot in all_shoots or not (shoot in my_ships):
                                        print ("pali opou na nai varas re pc")
                                        periptwsi = 1
                                        searching = False
                                        continue
                                    else:
                                        all_shoots.append(shoot)
                                        for i in range(len(player_ships)):
                                            for j in range(len(player_ships[i])):
                                                if shoot == player_ships[i][j]:
                                                    shoot_success = True
                                        if shoot_success == True:
                                            periptwsi = 39

                                elif periptwsi == 39:
                                    shoot = [shoot_searching[0],shoot_searching[1]-100]
                                    if shoot in all_shoots or not (shoot in my_ships):
                                        print ("pali opou na nai varas re pc")
                                        periptwsi = 1
                                        searching = False
                                        continue
                                    else:
                                        all_shoots.append(shoot)
                                        for i in range(len(player_ships)):
                                            for j in range(len(player_ships[i])):
                                                if shoot == player_ships[i][j]:
                                                    shoot_success = True
                                        if shoot_success == True:
                                            periptwsi = 41
                                        else:
                                            periptwsi = 1
                                            searching = False

                                elif periptwsi == 41:
                                    shoot = [shoot_searching[0],shoot_searching[1]-150]
                                    if shoot in all_shoots or not (shoot in my_ships):
                                        print ("pali opou na nai varas re pc")
                                        periptwsi = 1
                                        searching = False
                                        continue
                                    else:
                                        all_shoots.append(shoot)
                                        for i in range(len(player_ships)):
                                            for j in range(len(player_ships[i])):
                                                if shoot == player_ships[i][j]:
                                                    shoot_success = True
                                        if shoot_success == True:
                                            periptwsi = 43
                                        else:
                                            periptwsi = 1
                                            searching = False

                                elif periptwsi == 43:
                                    shoot = [shoot_searching[0],shoot_searching[1]-200]
                                    if shoot in all_shoots or not (shoot in my_ships):
                                        print ("pali opou na nai varas re pc")
                                        periptwsi = 1
                                        searching = False
                                        continue
                                    else:
                                        all_shoots.append(shoot)
                                        for i in range(len(player_ships)):
                                            for j in range(len(player_ships[i])):
                                                if shoot == player_ships[i][j]:
                                                    shoot_success = True
                                        if shoot_success == True:
                                            periptwsi = 1
                                            searching = False
                                        else:
                                            periptwsi = 1
                                            searching = False

#################################### NA DEI AMA PETUHE ########################################
                            if shoot_success == True:
                                pygame.draw.rect(gameDisplay,red, (shoot[0],shoot[1],30,30))
                                score_computer += 1
                                break
                            else:
                                print (shoot,"\n")
                                print (my_ships)
                                pygame.draw.rect(gameDisplay,white, (shoot[0],shoot[1],30,30))
                                break

########################################################### AI

            if score_player == 17:
                print ("nikises")
                gameDisplay.fill(white)
                message_display("You Won!!!",700,300)
                time.sleep(4)
                pygame.quit()
                quit()
            elif score_computer == 17:
                print ("exases")
                gameDisplay.fill(white)
                message_display("You Lost :(",700,300)
                time.sleep(4)
                pygame.quit()
                quit()


def rects2():
    position_list = []
    for i in range(810,1290,50):
        pygame.draw.rect(gameDisplay, blue, (i,50,30,30))
        position_list.append([i,50,30,30])

        for j in range (100,550,50):
            pygame.draw.rect(gameDisplay,blue, (i,j,30,30))
            position_list.append([i,j,30,30])

    return position_list

def place_ships_player():
    again = False
    place = True
    pos = 1
    placed_ships = 0
    player_ship1= []
    player_ship2= []
    player_ship3= []
    player_ship4= []
    player_ship5= []
    player_ships=[]
    gameDisplay.fill(white)
    position_list2=rects2()
    grammes()
    
    while place:
        x2=[]
        y2=[]
        w2=[]
        h2=[]
        for i in range (len(position_list2)):
            x2.append(position_list2[i][0])
            y2.append(position_list2[i][1])
            w2.append(position_list2[i][2])
            h2.append(position_list2[i][3])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return place_ships_player()  
                
            message_display("Press 'r' to restart the positioning of ALL ships!",700,660)
            place = True
            if placed_ships == 0:
                message_display("Please place 2-square ship by clicking the start and the end of it",700,600)
            elif placed_ships == 1:
                message_display("Please place the first 3-square ship by clicking the start and the end of it",700,600)
            elif placed_ships == 2:
                message_display("Please place the second 3-square ship by clicking the start and the end of it",700,600)
            elif placed_ships == 3:
                message_display("Please place 4-square ship by clicking the start and the end of it",700,600)
            elif placed_ships == 4:
                message_display("Please place 5-square ship by clicking the start and the end of it",700,600)
            elif placed_ships == 5 :
                return player_ships
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                legal_move_player = button1(x2,y2,w2,h2,mouse,click)
  #              print (legal_move_player)
                if placed_ships == 0 and pos == 1 and legal_move_player != [0,0]:
                    player_ship1.append(legal_move_player)
                    pygame.draw.rect(gameDisplay, red, (legal_move_player[0],legal_move_player[1],30,30))
                    pos = 2
                elif placed_ships == 0 and pos ==2 and legal_move_player != [0,0]:
                    if legal_move_player [0] == player_ship1[0][0] + 50 and legal_move_player [1] == player_ship1[0][1] or legal_move_player [0] ==  player_ship1[0][0] -50 and legal_move_player[1] == player_ship1[0][1] or legal_move_player[0] == player_ship1[0][0] and legal_move_player[1] == player_ship1[0][1] + 50 or legal_move_player[0] == player_ship1[0][0] and legal_move_player[1] == player_ship1[0][1] - 50:
                        player_ship1.append(legal_move_player)
                        pygame.draw.rect(gameDisplay, red, (legal_move_player[0],legal_move_player[1],30,30))
                        placed_ships = 1
                        pos = 1
                        player_ships.append(player_ship1)
            #            print (player_ship1)
                    else:
                        print ("Incorrect placement")

                elif placed_ships == 1 and pos == 1 and legal_move_player != [0,0]:
                    if legal_move_player in player_ships[0]:
                        print ("ti kaeis ekei re")
                    else:
                        player_ship2.append(legal_move_player)
                        pygame.draw.rect(gameDisplay, red, (legal_move_player[0],legal_move_player[1],30,30))
                        pos = 2
                elif placed_ships == 1 and pos ==2 and legal_move_player != [0,0]:
                    if legal_move_player [0] == player_ship2[0][0] + 100 and legal_move_player [1] == player_ship2[0][1] or legal_move_player [0] ==  player_ship2[0][0] -100 and legal_move_player[1] == player_ship2[0][1] or legal_move_player[0] == player_ship2[0][0] and legal_move_player[1] == player_ship2[0][1] + 100 or legal_move_player[0] == player_ship2[0][0] and legal_move_player[1] == player_ship2[0][1] - 100:
                        player_ship2.append(legal_move_player)
                        pygame.draw.rect(gameDisplay, red, (legal_move_player[0],legal_move_player[1],30,30))
                        if legal_move_player [0] == player_ship2[0][0] + 100 and legal_move_player [1] == player_ship2[0][1]:
                            pygame.draw.rect(gameDisplay, red, (legal_move_player[0]-50,legal_move_player[1],30,30))
                            player_ship2.append([legal_move_player[0]-50,legal_move_player[1]])
                        elif legal_move_player [0] ==  player_ship2[0][0] -100 and legal_move_player[1] == player_ship2[0][1]:
                            pygame.draw.rect(gameDisplay, red, (legal_move_player[0]+50,legal_move_player[1],30,30))
                            player_ship2.append([legal_move_player[0]+50,legal_move_player[1]])
                        elif legal_move_player[0] == player_ship2[0][0] and legal_move_player[1] == player_ship2[0][1] + 100:
                            pygame.draw.rect(gameDisplay, red, (legal_move_player[0],legal_move_player[1]-50,30,30))
                            player_ship2.append([legal_move_player[0],legal_move_player[1]-50])
                        elif legal_move_player[0] == player_ship2[0][0] and legal_move_player[1] == player_ship2[0][1] - 100:
                            pygame.draw.rect(gameDisplay, red, (legal_move_player[0],legal_move_player[1]+50,30,30))
                            player_ship2.append([legal_move_player[0],legal_move_player[1]+50])
                        player_ships.append(player_ship2)
                        placed_ships = 2
                        pos = 1

### elegxos an peftei to ena ploio panw sto allo
                        if placed_ships == 2:
                            positions_taken2=[]
                            for i in range(len(player_ships)-1):
                                for j in range(len(player_ships[i])):
                                    for k in range(len(player_ship2)):
                                        if player_ship2[k] == player_ships[i][j]:

                                            placed_ships = 1
                                            positions_taken2.append(player_ships[i][j])
                                            again = True
                                            pygame.draw.rect(gameDisplay, blue, (player_ship2[0][0],player_ship2[0][1],30,30))
                                            pygame.draw.rect(gameDisplay, blue, (player_ship2[1][0],player_ship2[1][1],30,30))                                                
                                            pygame.draw.rect(gameDisplay, blue, (player_ship2[2][0],player_ship2[2][1],30,30))
                                            for i in range(len(positions_taken2)):
                                                pygame.draw.rect(gameDisplay, red, (positions_taken2[i][0],positions_taken2[i][1],30,30))
                                                                       
                        if again == True:
                            player_ships.pop()
                            player_ship2=[]
                            again = False                            
################################ews edw                        
                    else:
                        print ("Incorrect placement")

                elif placed_ships == 2 and pos == 1 and legal_move_player != [0,0]:
                    if legal_move_player in player_ships[0] or legal_move_player in player_ships[1]:
                        print ("ti kaeis ekei re")
                    else:
                        player_ship3.append(legal_move_player)
                        pygame.draw.rect(gameDisplay, red, (legal_move_player[0],legal_move_player[1],30,30))
                        pos = 2
                elif placed_ships == 2 and pos ==2 and legal_move_player != [0,0]:
                    if legal_move_player [0] == player_ship3[0][0] + 100 and legal_move_player [1] == player_ship3[0][1] or legal_move_player [0] ==  player_ship3[0][0] -100 and legal_move_player[1] == player_ship3[0][1] or legal_move_player[0] == player_ship3[0][0] and legal_move_player[1] == player_ship3[0][1] + 100 or legal_move_player[0] == player_ship3[0][0] and legal_move_player[1] == player_ship3[0][1] - 100:
                        player_ship3.append(legal_move_player)
                        pygame.draw.rect(gameDisplay, red, (legal_move_player[0],legal_move_player[1],30,30))
                        if legal_move_player [0] == player_ship3[0][0] + 100 and legal_move_player [1] == player_ship3[0][1]:
                            pygame.draw.rect(gameDisplay, red, (legal_move_player[0]-50,legal_move_player[1],30,30))
                            player_ship3.append([legal_move_player[0]-50,legal_move_player[1]])
                        elif legal_move_player [0] ==  player_ship3[0][0] -100 and legal_move_player[1] == player_ship3[0][1]:
                            pygame.draw.rect(gameDisplay, red, (legal_move_player[0]+50,legal_move_player[1],30,30))
                            player_ship3.append([legal_move_player[0]+50,legal_move_player[1]])
                        elif legal_move_player[0] == player_ship3[0][0] and legal_move_player[1] == player_ship3[0][1] + 100:
                            pygame.draw.rect(gameDisplay, red, (legal_move_player[0],legal_move_player[1]-50,30,30))
                            player_ship3.append([legal_move_player[0],legal_move_player[1]-50])
                        elif legal_move_player[0] == player_ship3[0][0] and legal_move_player[1] == player_ship3[0][1] - 100:
                            pygame.draw.rect(gameDisplay, red, (legal_move_player[0],legal_move_player[1]+50,30,30))
                            player_ship3.append([legal_move_player[0],legal_move_player[1]+50])
                        placed_ships = 3
                        pos = 1
                        player_ships.append(player_ship3)
                        if placed_ships == 3:
                            positions_taken3=[]
                            for i in range(len(player_ships)-1):
                                for j in range(len(player_ships[i])):
                                    for k in range(len(player_ship3)):
                                        if player_ship3[k] == player_ships[i][j]:
                                            print ("den mporeis")
                                            placed_ships = 2
                                            positions_taken3.append(player_ships[i][j])
                                            again = True
                        
                        if again == True:
                            pygame.draw.rect(gameDisplay, blue, (player_ship3[0][0],player_ship3[0][1],30,30))
                            pygame.draw.rect(gameDisplay, blue, (player_ship3[1][0],player_ship3[1][1],30,30))                                                
                            pygame.draw.rect(gameDisplay, blue, (player_ship3[2][0],player_ship3[2][1],30,30))
                            for i in range(len(positions_taken3)):
                                pygame.draw.rect(gameDisplay, red, (positions_taken3[i][0],positions_taken3[i][1],30,30))
                            player_ships.pop()
                            player_ship3=[]
                            again = False
                    else:
                        print ("Incorrect placement")                    

                elif placed_ships == 3 and pos == 1 and legal_move_player != [0,0]:
                    if legal_move_player in player_ships[0] or legal_move_player in player_ships[1] or legal_move_player in player_ships[2]:
                        print ("ti kaeis ekei re")
                    else:
                        player_ship4.append(legal_move_player)
                        pygame.draw.rect(gameDisplay, red, (legal_move_player[0],legal_move_player[1],30,30))
                        pos = 2
                elif placed_ships == 3 and pos ==2 and legal_move_player != [0,0]:
                    if legal_move_player [0] == player_ship4[0][0] + 150 and legal_move_player [1] == player_ship4[0][1] or legal_move_player [0] ==  player_ship4[0][0] -150 and legal_move_player[1] == player_ship4[0][1] or legal_move_player[0] == player_ship4[0][0] and legal_move_player[1] == player_ship4[0][1] + 150 or legal_move_player[0] == player_ship4[0][0] and legal_move_player[1] == player_ship4[0][1] - 150:
                        player_ship4.append(legal_move_player)
                        pygame.draw.rect(gameDisplay, red, (legal_move_player[0],legal_move_player[1],30,30))
                        if legal_move_player [0] == player_ship4[0][0] + 150 and legal_move_player [1] == player_ship4[0][1]:
                            pygame.draw.rect(gameDisplay, red, (legal_move_player[0]-100,legal_move_player[1],30,30))
                            player_ship4.append([legal_move_player[0]-100,legal_move_player[1]])
                            pygame.draw.rect(gameDisplay, red, (legal_move_player[0]-50,legal_move_player[1],30,30))
                            player_ship4.append([legal_move_player[0]-50,legal_move_player[1]])
                        elif legal_move_player [0] ==  player_ship4[0][0] -150 and legal_move_player[1] == player_ship4[0][1]:
                            pygame.draw.rect(gameDisplay, red, (legal_move_player[0]+100,legal_move_player[1],30,30))
                            player_ship4.append([legal_move_player[0]+100,legal_move_player[1]])
                            pygame.draw.rect(gameDisplay, red, (legal_move_player[0]+50,legal_move_player[1],30,30))
                            player_ship4.append([legal_move_player[0]+50,legal_move_player[1]])
                        elif legal_move_player[0] == player_ship4[0][0] and legal_move_player[1] == player_ship4[0][1] + 150:
                            pygame.draw.rect(gameDisplay, red, (legal_move_player[0],legal_move_player[1]-100,30,30))
                            player_ship4.append([legal_move_player[0],legal_move_player[1]-100])
                            pygame.draw.rect(gameDisplay, red, (legal_move_player[0],legal_move_player[1]-50,30,30))
                            player_ship4.append([legal_move_player[0],legal_move_player[1]-50])
                        elif legal_move_player[0] == player_ship4[0][0] and legal_move_player[1] == player_ship4[0][1] - 150:
                            pygame.draw.rect(gameDisplay, red, (legal_move_player[0],legal_move_player[1]+100,30,30))
                            player_ship4.append([legal_move_player[0],legal_move_player[1]+100])
                            pygame.draw.rect(gameDisplay, red, (legal_move_player[0],legal_move_player[1]+50,30,30))
                            player_ship4.append([legal_move_player[0],legal_move_player[1]+50])
                        placed_ships = 4
                        pos = 1
                        player_ships.append(player_ship4)

                        if placed_ships == 4:
                            positions_taken4=[]
                            for i in range(len(player_ships)-1):
                                for j in range(len(player_ships[i])):
                                    for k in range(len(player_ship4)):
                                        if player_ship4[k] == player_ships[i][j]:
                                            print ("den mporeis")
                                            placed_ships = 3
                                            positions_taken4.append(player_ships[i][j])
                                            again = True
                        
                        if again == True:
                            pygame.draw.rect(gameDisplay, blue, (player_ship4[0][0],player_ship4[0][1],30,30))
                            pygame.draw.rect(gameDisplay, blue, (player_ship4[1][0],player_ship4[1][1],30,30))                                                
                            pygame.draw.rect(gameDisplay, blue, (player_ship4[2][0],player_ship4[2][1],30,30))
                            pygame.draw.rect(gameDisplay, blue, (player_ship4[3][0],player_ship4[3][1],30,30))
                            for i in range(len(positions_taken4)):
                                pygame.draw.rect(gameDisplay, red, (positions_taken4[i][0],positions_taken4[i][1],30,30))
                            player_ships.pop()
                            player_ship4=[]
                            again = False                        
                    else:
                        print ("Incorrect placement")                

                elif placed_ships == 4 and pos == 1 and legal_move_player != [0,0]:
                    if legal_move_player in player_ships[0] or legal_move_player in player_ships[1] or legal_move_player in player_ships[2] or legal_move_player in player_ships[3]:
                        print ("ti kaeis ekei re")
                    else:
                        player_ship5.append(legal_move_player)
                        pygame.draw.rect(gameDisplay, red, (legal_move_player[0],legal_move_player[1],30,30))
                        pos = 2
                elif placed_ships == 4 and pos ==2 and legal_move_player != [0,0]:
                    if legal_move_player [0] == player_ship5[0][0] + 200 and legal_move_player [1] == player_ship5[0][1] or legal_move_player [0] ==  player_ship5[0][0] -200 and legal_move_player[1] == player_ship5[0][1] or legal_move_player[0] == player_ship5[0][0] and legal_move_player[1] == player_ship5[0][1] + 200 or legal_move_player[0] == player_ship5[0][0] and legal_move_player[1] == player_ship5[0][1] - 200:
                        player_ship5.append(legal_move_player)
                        pygame.draw.rect(gameDisplay, red, (legal_move_player[0],legal_move_player[1],30,30))
                        if legal_move_player [0] == player_ship5[0][0] + 200 and legal_move_player [1] == player_ship5[0][1]:
                            pygame.draw.rect(gameDisplay, red, (legal_move_player[0]-100,legal_move_player[1],30,30))
                            player_ship5.append([legal_move_player[0]-100,legal_move_player[1]])
                            pygame.draw.rect(gameDisplay, red, (legal_move_player[0]-50,legal_move_player[1],30,30))
                            player_ship5.append([legal_move_player[0]-50,legal_move_player[1]])
                            pygame.draw.rect(gameDisplay, red, (legal_move_player[0]-150,legal_move_player[1],30,30))
                            player_ship5.append([legal_move_player[0]-150,legal_move_player[1]])
                        elif legal_move_player [0] ==  player_ship5[0][0] -200 and legal_move_player[1] == player_ship5[0][1]:
                            pygame.draw.rect(gameDisplay, red, (legal_move_player[0]+100,legal_move_player[1],30,30))
                            player_ship5.append([legal_move_player[0]+100,legal_move_player[1]])
                            pygame.draw.rect(gameDisplay, red, (legal_move_player[0]+50,legal_move_player[1],30,30))
                            player_ship5.append([legal_move_player[0]+50,legal_move_player[1]])
                            pygame.draw.rect(gameDisplay, red, (legal_move_player[0]+150,legal_move_player[1],30,30))
                            player_ship5.append([legal_move_player[0]+150,legal_move_player[1]])
                        elif legal_move_player[0] == player_ship5[0][0] and legal_move_player[1] == player_ship5[0][1] + 200:
                            pygame.draw.rect(gameDisplay, red, (legal_move_player[0],legal_move_player[1]-100,30,30))
                            player_ship5.append([legal_move_player[0],legal_move_player[1]-100])
                            pygame.draw.rect(gameDisplay, red, (legal_move_player[0],legal_move_player[1]-50,30,30))
                            player_ship5.append([legal_move_player[0],legal_move_player[1]-50])
                            pygame.draw.rect(gameDisplay, red, (legal_move_player[0],legal_move_player[1]-150,30,30))
                            player_ship5.append([legal_move_player[0],legal_move_player[1]-150])
                        elif legal_move_player[0] == player_ship5[0][0] and legal_move_player[1] == player_ship5[0][1] - 200:
                            pygame.draw.rect(gameDisplay, red, (legal_move_player[0],legal_move_player[1]+100,30,30))
                            player_ship5.append([legal_move_player[0],legal_move_player[1]+100])
                            pygame.draw.rect(gameDisplay, red, (legal_move_player[0],legal_move_player[1]+50,30,30))
                            player_ship5.append([legal_move_player[0],legal_move_player[1]+50])
                            pygame.draw.rect(gameDisplay, red, (legal_move_player[0],legal_move_player[1]+150,30,30))
                            player_ship5.append([legal_move_player[0],legal_move_player[1]+150])
                        player_ships.append(player_ship5)
                        placed_ships = 5
                        pos = 1

                        if placed_ships == 5:
                            positions_taken5=[]
                            for i in range(len(player_ships)-1):
                                for j in range(len(player_ships[i])):
                                    for k in range(len(player_ship5)):
                                        if player_ship5[k] == player_ships[i][j]:
                                            print ("den mporeis")
                                            positions_taken5.append(player_ships[i][j])
                                            placed_ships = 4     
                                            again = True
                        
                        if again == True:
                            pygame.draw.rect(gameDisplay, blue, (player_ship5[0][0],player_ship5[0][1],30,30))
                            pygame.draw.rect(gameDisplay, blue, (player_ship5[1][0],player_ship5[1][1],30,30))                                                
                            pygame.draw.rect(gameDisplay, blue, (player_ship5[2][0],player_ship5[2][1],30,30))
                            pygame.draw.rect(gameDisplay, blue, (player_ship5[3][0],player_ship5[3][1],30,30))
                            pygame.draw.rect(gameDisplay, blue, (player_ship5[4][0],player_ship5[4][1],30,30))
                            for i in range(len(positions_taken5)):
                                pygame.draw.rect(gameDisplay, red, (positions_taken5[i][0],positions_taken5[i][1],30,30))
                            player_ships.pop()
                            player_ship5=[]
                            again = False                        
                    else:
                        print ("Incorrect placement")                     
    pygame.display.update()
    clock.tick(100)               


player_ships = place_ships_player()
game_loop()
pygame.quit()
quit()
