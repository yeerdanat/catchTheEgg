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

egg_seq=0

#initial coordinates and increment
x=2000
y=2000
incX=0
incY=0





timer = pygame.USEREVENT+1
pygame.time.set_timer(timer, 4000)


run=True
while run:

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

    pygame.display.update()

    for event in pygame.event.get():
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
            

    clock.tick(60)