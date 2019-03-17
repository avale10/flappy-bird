import pygame

import random

pygame.init()



black = (0,0,0)
limegreen = (50,205,50)
green = (0,255,0)
red = (255,0,0)
blue = (36,255,247)
size = (400,600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Flappy Bird")

done= False
clock = pygame.time.Clock()

x = 195
y = 230
x_speed = 0
y_speed = 0
ground = 500
xloc=900
yloc=0
xsize = 70
ysize = random.randint(0,400)
space = 150
obspeed = 2.5
#add global tracker of score
score = 0 


def obstacles(xloc,yloc,xsize,ysize):
    pygame.draw.rect(screen,green, [xloc,yloc,xsize,ysize])
    pygame.draw.rect(screen,green, [xloc,int(yloc+ysize+space), xsize, ysize+500])


def ball1(x,y):
    pygame.draw.circle(screen,black,(x,y),20)
def ball2(x,y):
    pygame.draw.circle(screen,limegreen,(x,y),15)


def gameover():
    font = pygame.font.SysFont(None,25)
    text = font.render("Game Over ",True,red)
    screen.blit(text, [150,250])

#function to write score being kept
def Score(score):
    font = pygame.font.SysFont(None,75)
    #we use str to convert score value to string for display
    text = font.render("Score: "+str(score),True,black)
    #top left corner coordinates
    screen.blit(text, [0,0])

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_speed = -10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                y_speed = 5


    screen.fill(blue)
    obstacles(xloc,yloc,xsize,ysize)
 
    ball1(x,y)
    ball2(x,y)

    #if the ball is between two obstacles
    Score(score)

    y += y_speed
    xloc -= obspeed
 

    if y > ground:
        gameover()
        obspeed = 0
        y_speed = 0
        ground(ground)

    #if we hit obstacles in the top block
    if x+20 > xloc and y-20 < ysize and x-15 < xsize+xloc:
        gameover()
        obspeed = 0
        y_speed = 6
        ground(ground)
       

    #if we hit obstacles in the bottom block
    if x+20 > xloc and y+20 > ysize+space and x-15 < xsize+xloc:
        gameover()
        obspeed = 0
        y_speed = 6
     

    #if obstacle location X is
    if xloc < -80:
        xloc = 700
        ysize = random.randint(0,400)

    #check if obstacle was passed to adding to score
    if x > xloc and x < xloc+3:
        score = score + 1


    pygame.display.flip()
    clock.tick(60)


pygame.quit()
