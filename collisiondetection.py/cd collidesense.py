#Collision Detection (Eat the blocks!) with a sweet tune
#By Mohinder Talafuse
#To begin, type (fn. + f5) for Windows, (f5 only) for Mac
#To terminate game, press (esc.)
#To move, use (WASD) or (ArrowKeys);
#Click to make food;
#Press (x) to teleport to a random location
#84 lines w/o whitespace, 96 total, BEGINNER
#The source code can be seen below (python 3.8, pygame 1.9.6):
import pygame, sys, random
from pygame.locals import*

pygame.init()
mainClock = pygame.time.Clock()

WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), pygame.FULLSCREEN)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20
player = pygame.Rect(300, 100, 50, 50)
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE),
                             random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6 #Lower for a slower moving game, higher for a faster moving game (Changes fast, I recommend that you don't go over 14 or under 2)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == K_a:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == K_d:
                moveLeft = False
                moveRight = True
            if event.key == K_UP or event.key == K_w:
                moveDown = False
                moveUp = True
            if event.key == K_DOWN or event.key == K_s:
                moveUp = False
                moveDown = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            if event.key == K_UP or event.key == K_w:
                moveUp = False
            if event.key == K_DOWN or event.key == K_s:
                moveDown = False
            if event.key == K_x:
                player.top = random.randint(0, WINDOWHEIGHT - player.height)
                player.left = random.randint(0, WINDOWWIDTH - player.width)

        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0], event.pos[1], FOODSIZE, FOODSIZE))

    foodCounter += 1
    if foodCounter >= NEWFOOD:
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE),
                                 random.randint(0, WINDOWHEIGHT - FOODSIZE),
                                 FOODSIZE, FOODSIZE))

    windowSurface.fill(WHITE)

    if moveDown and player.bottom < WINDOWHEIGHT:
        player.top += MOVESPEED
    if moveUp and player.top > 0:
        player.top -= MOVESPEED
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED 
    if moveRight and player.right < WINDOWWIDTH:
        player.right += MOVESPEED

    pygame.draw.rect(windowSurface, RED, player)

    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)

    for i in range(len(foods)):
        pygame.draw.rect(windowSurface, GREEN, foods[i])

    pygame.display.update()
    mainClock.tick(40)
        
        
