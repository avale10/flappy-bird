import pygame

pygame.init()

black = (0,0,0)
limegreen = (50,205,50)
blue = (36,255,247)

size = (500,700)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Flappy Bird")

done= False
clock = pygame.time.Clock()

x = 350
y = 250

#define global variables to control speed
x_speed = 0
y_speed = 0

#define function to draw circle
def ball1(x,y):
    pygame.draw.circle(screen,black,(x,y),20)
def ball2(x,y):
    pygame.draw.circle(screen,limegreen,(x,y),15)


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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed = 5

    screen.fill(blue)
    #call function to draw the ball
    ball1(x,y)
    ball2(x,y)
    #adjust vertical y position
    y += y_speed
    x += x_speed

    pygame.display.flip()
    clock.tick(60)


pygame.quit()
