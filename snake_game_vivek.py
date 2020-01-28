import pygame
import sys
import time
import random


pygame.init()


size = width, height = 640, 320
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake Game")


red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
purple = (255,0,255)
blue = (255,0,0)


clock= pygame.time.Clock()


snakey = 10
snakePos = [100, 50]
snakeBod = [[100, 50], [90, 50], [80, 50]]
foodPos = [400, 50]
foodLoc = True
direction = 'RIGHT'
changeto = ''
score = 0



def gameOver():
    gameEnd = pygame.font.SysFont('monaco', 72)
    snakeTouch = gameEnd.render("Game Over", True, red)
    snakeTouch1 = snakeTouch.get_rect()
    snakeTouch1.midtop = (320, 25)
    screen.blit(snakeTouch, snakeTouch1)
    showScore(0)
    pygame.display.flip()
    time.sleep(4)
    pygame.quit()
    sys.exit()



def showScore(choice=1):
    scoreFont = pygame.font.SysFont('monaco', 32)
    scoreSurface = scoreFont.render("Score  :  {0}".format(score), True, black)
    scoreRect = scoreSurface.get_rect()
    if choice == 1:
        scoreRect.midtop = (80, 10)
    else:
        scoreRect.midtop = (320, 100)
    screen.blit(scoreSurface, scoreRect)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                changeto = 'LEFT'
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                changeto = 'UP'
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                changeto = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))


    if changeto == 'RIGHT' and direction != 'LEFT':
        direction = changeto
    if changeto == 'LEFT' and direction != 'RIGHT':
        direction = changeto
    if changeto == 'UP' and direction != 'DOWN':
        direction = changeto
    if changeto == 'DOWN' and direction != 'UP':
        direction = changeto


    if direction == 'RIGHT':
        snakePos[0] += snakey
    if direction == 'LEFT':
        snakePos[0] -= snakey
    if direction == 'DOWN':
        snakePos[1] += snakey
    if direction == 'UP':
        snakePos[1] -= snakey


    snakeBod.insert(0, list(snakePos))
    if snakePos == foodPos:
        foodLoc = False
        score += 1
    else:
        snakeBod.pop()
    if foodLoc == False:
        foodPos = [random.randrange(1, width // 10) * snakey, random.randrange(1, height // 10) * snakey]
        foodLoc = True

    screen.fill(white)
    for pos in snakeBod:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], snakey, snakey))
    pygame.draw.rect(screen, blue, pygame.Rect(foodPos[0], foodPos[1], snakey, snakey))


    if snakePos[0] >= width or snakePos[0] < 0:
        gameOver()
    if snakePos[1] >= height or snakePos[1] < 0:
        gameOver()


    for block in snakeBod[1:]:
        if snakePos == block:
            gameOver()

    showScore()
    pygame.display.flip()
    clock.tick(20)
pygame.QUIT()
