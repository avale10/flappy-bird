import pygame

import random

pygame.init()

#loading images
imageUp = pygame.image.load('Nyan-Cat-up.png')
imageUp = pygame.transform.scale(imageUp, (40,40))

imageDown = pygame.image.load('Nyan-Cat.png')
imageDown = pygame.transform.scale(imageDown, (40,40))

#imageDead = pygame.image.load('Flappy_down.png')
#imageDead = pygame.transform.scale(imageDead, (28,23))


black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
skyblue = (0,191,255)
orange = (255,215,0)
gray = (112,138,144)
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
xloc=600
yloc=0
xsize = 100
ysize = random.randint(0,400)
space = 75
obspeed = 2.5
#add global tracker of score
score = 0 


#def obstacles(xloc,yloc,xsize,ysize):
#   pygame.draw.rect(screen,green, [xloc,yloc,xsize,ysize])
#   pygame.draw.rect(screen,green, [xloc,int(yloc+ysize+space), xsize, ysize+500])
def obstacles(xloc,yloc,xsize,ysize):
    imgTop = pygame.image.load('matchstick.png')
    imgTop = pygame.transform.rotate(imgTop, 180)
    imgTop = pygame.transform.scale(imgTop, (xsize,ysize))
    imgBottom = pygame.image.load('matchstick.png')
    imgBottom = pygame.transform.scale(imgBottom, (xsize, 800 - ysize))
    screen.blit(imgTop, (xloc, yloc))
    screen.blit(imgBottom, (xloc, int(yloc + ysize + space)))
 

    #passing in iage of current flappy
def ball1(x,y,image):
    #pygame.draw.circle(screen,black,(x,y),20)
    screen.blit(image, (x, y))


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

#global image object
image = imageUp
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                #change image up
                image = imageUp
                y_speed = -10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                #change image down
                image = imageDown
                y_speed = 5

    #replace the white sky with skyblue
    #screen.fill(white)
    screen.fill(skyblue)
    imageB = pygame.image.load('naynback9_shop_preview.png')
    imageB = pygame.transform.scale(imageB, (400,600))
    screen.blit(imageB,(0,0))
    imageF = pygame.image.load('nyan_floor.png')
    imageF = pygame.transform.scale(imageF, (400,700))
    screen.blit(imageF,(0,0))

    obstacles(xloc,yloc,xsize,ysize)
 
    ball1(x,y,image)
    #ball2(x,y)

    Score(score)

    y += y_speed
    xloc -= obspeed
 

    if y > ground:
        #gameover()
        obspeed = 0
        y_speed = 0
        

    #if we hit obstacles in the top block
    if x+10 > xloc and y-10 < ysize and x-5 < xsize+xloc:
        #gameover()
        obspeed = 0
        y_speed = 6
        
       

    #if we hit obstacles in the bottom block
    if x+10 > xloc and y+10 > ysize+space and x-5 < xsize+xloc:
        #gameover()
        obspeed = 0
        y_speed = 6
     

    #if obstacle location X is
    if xloc < -80:
        xloc = 700
        ysize = random.randint(0,600)

    #check if obstacle was passed to adding to score
    if x > xloc and x < xloc+3:
        score = score + 1


    pygame.display.flip()
    clock.tick(60)


pygame.quit()
