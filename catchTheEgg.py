import pygame 
import random

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((763, 500))

pygame.display.set_caption('Catch the egg! Game')
icon = pygame.image.load('images/wolf.png')
pygame.display.set_icon(icon)

font_score = pygame.font.Font('fonts/score.ttf', 55)
font = pygame.font.SysFont(None, 50)

bg = pygame.image.load('images/bg.jpg')
bg= pygame.transform.scale(bg, (763,500))


bg_sound = pygame.mixer.Sound('music/music.mp3')
bg_sound.play(-1)

#exporting wolf positions
lb=pygame.image.load('images/left-bottom.png')
lb=pygame.transform.scale(lb, (433, 246))
lt=pygame.image.load('images/left-top.png')
lt=pygame.transform.scale(lt, (433, 246))
rt=pygame.image.load('images/right-top.png')
rt=pygame.transform.scale(rt, (433, 246))
rb=pygame.image.load('images/right-bottom.png')
rb=pygame.transform.scale(rb, (433, 246))

#initial position
current_or='lt'


egg = pygame.image.load('images/egg.png')
egg = pygame.transform.scale(egg, (22,30))
egg = pygame.transform.rotate(egg, 25)
mt=pygame.image.load('images/mistake.png')
mt=pygame.transform.scale(mt,(40,40))
bomb = pygame.image.load('images/bombs.png')
bomb = pygame.transform.scale(bomb, (22,30))

egg_seq=0
bomb_seq=0

#initial coordinates and increment
x=2000
y=2000
incX=0
incY=0

#bomb coordinates
xb=2000
yb=2000
incXb=0
incYb=0

bombs=False
bestScore=0
score=0
mistakes=0
buff = 60 #acceleration with levels

timer = pygame.USEREVENT+1
pygame.time.set_timer(timer, 4000)
timerbomb = pygame.USEREVENT+1
pygame.time.set_timer(timerbomb, 7000)

def score_show(score):

    if score<10:
        score='000'+str(score)
    elif score<100:
        score='00'+str(score)
    elif score<1000:
        score='0'+str(score)
    else:
        score=str(score)

    text = font_score.render(score, True, (0,0,0))
    screen.blit(text, (510, 10))

def mistakes_show(mistakes):   
        if mistakes>=1:
            for i in range(1, mistakes+1):
                screen.blit(mt, (460+i*45, 70))

levelsMenu=False
game_paused=False

run=True
while run:
    if game_paused == True:
        screen.fill((52,78,91))
        text = font.render('Press SPACE to continue', True, (255,255,255))
        screen.blit(text, (170,110))
        

        textLvl = font.render('Change the Level', True, (255,255,255))
        lvlRect= textLvl.get_rect(topleft = (230,220))
        screen.blit(textLvl, lvlRect)
        mouse = pygame.mouse.get_pos() 

        textQuit = font.render('Quit the game', True, (255,255,255))
        quitRect=textQuit.get_rect(topleft=(264, 330))
        screen.blit(textQuit, quitRect)


        if (lvlRect.collidepoint(mouse)) and (pygame.mouse.get_pressed()[0]):
            levelsMenu=True

        if (quitRect.collidepoint(mouse)) and (pygame.mouse.get_pressed()[0]):
            run = False
            pygame.quit()

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            game_paused=False

        if levelsMenu:
            screen.fill((52,78,91))
    
            text = font.render('Choose the level', True, (255,255,255))
            screen.blit(text, (240,60))
            textEasy = font.render('Easy level', True, (255,255,255))
            easyRect = textEasy.get_rect(topleft=(120, 160))
            screen.blit(textEasy, easyRect)
            textMedium = font.render('Medium level', True, (255,255,255))
            medRect = textMedium.get_rect(topleft=(120, 260))
            screen.blit(textMedium, medRect)
            textHard = font.render('Hard level', True, (255,255,255))
            hardRect = textHard.get_rect(topleft=(120, 360))
            screen.blit(textHard, hardRect)

            if (easyRect.collidepoint(mouse)) and (pygame.mouse.get_pressed()[0]):
                buff=60
                score=0
                mistakes=0
                bombs=False
                levelsMenu=False
                game_paused=False
            if (medRect.collidepoint(mouse)) and (pygame.mouse.get_pressed()[0]):
                buff=120
                score=0
                mistakes=0
                bombs=False
                levelsMenu=False
                game_paused=False
            if (hardRect.collidepoint(mouse)) and (pygame.mouse.get_pressed()[0]):
                buff=150
                score=0
                mistakes=0
                bombs=True
                levelsMenu=False
                game_paused=False
    else:

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            if current_or=='rb' or current_or=='lb':
                current_or='lb'
            else:
                current_or='lt'
        if key[pygame.K_RIGHT]:
            if current_or=='rb' or current_or=='lb':
                current_or='rb'
            else:
                current_or='rt'
        if key[pygame.K_UP]:
            if current_or=='rb' or current_or=='rt':
                current_or='rt'
            else:
                current_or='lt'
        if key[pygame.K_DOWN]:
            if current_or=='rb' or current_or=='rt':
                current_or='rb'
            else:
                current_or='lb'


        screen.blit(bg, (0, 0))
        if current_or=='lt':
            screen.blit(lt, (120, 190))
        elif current_or =='lb':
            screen.blit(lb, (120, 190))
        elif current_or=='rt':
            screen.blit(rt, (200, 190))
        else:
            screen.blit(rb, (200, 190))
        
        screen.blit(egg, (x,y))
        x+=incX
        y+=incY

        screen.blit(bomb, (xb,yb))
        xb+=incXb
        yb+=incYb

        if mistakes<4 and x!=2000 and ((egg_seq==1 and x>123.2 and y>198.8 and current_or=='lt') or (egg_seq==2 and x>130 and y>313.1 and current_or=='lb') or (egg_seq==3 and x<584.5 and y>198.1 and current_or=='rt') or (egg_seq==4 and x<595 and y>306.6 and current_or=='rb')):     
            x=2000
            y=2000
            incX=0
            incY=0 
            score+=1
        if x!=2000 and ((egg_seq==1 and x>123.2 and y>198.8 and current_or!='lt') or ( egg_seq==2 and x>130 and y>313.1 and current_or!='lb') or (egg_seq==3 and x<584.5 and y>198.1 and current_or!='rt') or (egg_seq==4 and x<595 and y>306.6 and current_or!='rb')):
            x=2000
            y=2000
            incX=0
            incY=0
            mistakes+=1
        if mistakes<4 and xb!=2000 and ((bomb_seq==1 and xb>123.2 and yb>198.8 and current_or=='lt') or (bomb_seq==2 and xb>130 and yb>313.1 and current_or=='lb') or (bomb_seq==3 and xb<584.5 and yb>198.1 and current_or=='rt') or (bomb_seq==4 and xb<595 and yb>306.6 and current_or=='rb')):     
            xb=2000
            yb=2000
            incXb=0
            incYb=0 
            score-=1
        if ((bomb_seq==1 and xb>123.2 and yb>198.8 and current_or!='lt') or (bomb_seq==2 and xb>130 and yb>313.1 and current_or!='lb') or (bomb_seq==3 and xb<584.5 and yb>198.1 and current_or!='rt') or (bomb_seq==4 and xb<595 and yb>306.6 and current_or!='rb')):     
            xb=2000
            yb=2000
            incXb=0
            incYb=0 

        score_show(score)
        mistakes_show(mistakes)

        if mistakes>3 or score<0:
            screen.fill((92, 92, 92))
            text = font.render('You lost', True, (255,255,255))
            text_score = font.render("Score: "+ str(score), True, (255,255,255))
            if score>bestScore:
                bestScore=score
            text_bestscore= font.render("Best Score: "+str(bestScore), True, (255,255,255))
            text_restart= font.render("play again", True, (255,255,255))
            restart_rect=text_restart.get_rect(topleft=(295,360))
            screen.blit(text, (310, 150)) 
            screen.blit(text_score, (310, 200))
            screen.blit(text_bestscore, (275, 250))
            screen.blit(text_restart, restart_rect)
            pygame.display.update()
            mouse = pygame.mouse.get_pos()   
            if (restart_rect.collidepoint(mouse)) and (pygame.mouse.get_pressed()[0]):
                score=0
                mistakes=0    

    pygame.display.update()

    for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    game_paused= True
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == timer:
                egg_seq=random.randrange(1,5)
                if egg_seq ==1:
                    x=40
                    y=145
                    incX=1.7
                    incY=1.1
                if egg_seq ==2:
                    x=40
                    y=255
                    incX=1.7
                    incY=1.1
                if egg_seq ==3:
                    x=690
                    y=130
                    incX=-1.7
                    incY=1.1
                if egg_seq ==4:
                    x=690
                    y=245
                    incX=-1.7
                    incY=1.1
            if event.type==timerbomb:
                if bombs==True:
                    bomb_seq=random.randrange(1,5)
                    if bomb_seq ==1:
                        xb=40
                        yb=145
                        incXb=1.7
                        incYb=1.1
                    if bomb_seq ==2:
                        xb=40
                        yb=255
                        incXb=1.7
                        incYb=1.1
                    if bomb_seq ==3:
                        xb=690
                        yb=130
                        incXb=-1.7
                        incYb=1.1
                    if bomb_seq ==4:
                        xb=690
                        yb=245
                        incXb=-1.7
                        incYb=1.1
    clock.tick(buff)