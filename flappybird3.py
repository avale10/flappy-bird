import pygame


pygame.init()



black = (0,0,0)
limegreen = (50,205,50)
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

#define global variable position for the ground
#since vertical 'size' equals 500, defined above, and
#ball size is 20 as defined in 'ball' defining function
#ans -3 pixel correction
ground = 500


def ball1(x,y):
    pygame.draw.circle(screen,black,(x,y),20)
def ball2(x,y):
    pygame.draw.circle(screen,limegreen,(x,y),15)

#define function to handle game over event
def gameover():
    font = pygame.font.SysFont(None,25)
    text = font.render("Game Over ",True,black)
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
    #call function to draw the ball
    ball1(x,y)
    ball2(x,y)
    #adjust vertical y position
    y += y_speed
 

    #once 'y' is changed check if ground is touched hence game over
    if y > ground:
        gameover()
        #to stop the ball
        y_speed = 0
        x_speed = 0

    pygame.display.flip()
    clock.tick(60)


pygame.quit()
