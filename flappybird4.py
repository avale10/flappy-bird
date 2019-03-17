import pygame

#to use the random function
import random

pygame.init()



black = (0,0,0)
limegreen = (50,205,50)

#define new color green
green = (0,255,0)
#define new color RED
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

#x axis location for obstacle
xloc=400

#y axis location for obstacle
yloc=0

#how wide we want obstacle
xsize = 70

#how randomly tall it is
ysize = random.randint(0,400)

#space between two blocks
space = 150

#the speed of the obstacles as they move across the screen
#pixels per frame/flip
obspeed = 2.5

#we proceed to define our obstacles
def obstacles(xloc,yloc,xsize,ysize):
    pygame.draw.rect(screen,green, [xloc,yloc,xsize,ysize])
    pygame.draw.rect(screen,green, [xloc,int(yloc+ysize+space), xsize, ysize+400])


def ball1(x,y):
    pygame.draw.circle(screen,black,(x,y),20)
def ball2(x,y):
    pygame.draw.circle(screen,limegreen,(x,y),15)

#define function to handle game over event
def gameover():
    font = pygame.font.SysFont(None,25)
    #we update font color
    text = font.render("Game Over ",True,red)
    screen.blit(text, [150,250])

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
    #time to draw obstacles
    obstacles(xloc,yloc,xsize,ysize)
 
    ball1(x,y)
    ball2(x,y)
    #adjust vertical y position
    y += y_speed
    #time to redifine per refresh new x location
    xloc -= obspeed
 

    #once 'y' is changed check if ground is touched hence game over
    if y > ground:
        gameover()
        #if we hit the ground the obstacle stops
        obspeed = 0
        x_speed = 0

    pygame.display.flip()
    clock.tick(60)


pygame.quit()

