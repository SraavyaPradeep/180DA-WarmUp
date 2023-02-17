import paho.mqtt.client as mqtt
import pygame
import random
from pygame.locals import (
    RLEACCEL, 
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT

)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
running = True
color = (35,75,87)
white = (255, 255, 255)
totalHeight = SCREEN_HEIGHT/3
inp = 0
score = 0

class R(pygame.sprite.Sprite):
    def __init__(self):
        super(R, self).__init__()
        self.surf = pygame.image.load("Rock.png").convert()
        self.surf.set_colorkey(white, RLEACCEL)
class P(pygame.sprite.Sprite):
    def __init__(self):
        super(P, self).__init__()
        self.surf = pygame.image.load("Paper.png").convert()
        self.surf.set_colorkey(white, RLEACCEL)
class S(pygame.sprite.Sprite):
    def __init__(self):
        super(S, self).__init__()
        self.surf = pygame.image.load("Scissors.png").convert()
        self.surf.set_colorkey(white, RLEACCEL)

pygame.init()
arial = pygame.font.Font('arial.ttf', 20)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(color)
scissor = S()
rock = R()
paper = P()


words = arial.render('RPS!', True, color, white)
wBounds = words.get_rect().center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/5)
answer = arial.render(' ', True, color, white)
aBounds = answer.get_rect().center = (SCREEN_WIDTH/2, (SCREEN_HEIGHT)*4/5)
def change(val, val2, command):
    if (command == 1):
        if (val == 1):
            return 'Rock'
        elif (val == 2):
            return 'Paper'
        else:
            return 'Scissors'
    else:
        if (val == val2):
            return 'Tie!'
        elif ((val == 1 and val2 == 3) or 
              (val > val2 and val-1 == val2)):
            return 'You Win!'
        else:
            return 'Computer Wins!'
sWord = arial.render('Score -> 0', True, color, white)
sBound = sWord.get_rect()









while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if (pos[1]>totalHeight):
                inp = int(pos[0]/(7*SCREEN_WIDTH/20)) + 1
                comp = random.randint(1,3)
                myChoice = change(inp, 0, 1)
                compChoice = change(inp, comp, 2)
                words = arial.render('You chose ' + myChoice, True, color, white)
                answer = arial.render('Computer chose ' + change(comp, 0, 1) + '.' + compChoice, True, color, white)
                aBounds = (SCREEN_WIDTH/2, (SCREEN_HEIGHT)*4/5)
                print('You chose ' + myChoice + ', Computer chose', change(comp, 0, 1) + '.', compChoice)
                if (compChoice == 'You Win!'):
                    score = score + 1
                sWord = arial.render('Score -> ' + str(score), True, color, white)
        elif event.type == K_UP:
            pass

    screen.blit(rock.surf, (0, totalHeight))
    screen.blit(words, wBounds)

    screen.blit(paper.surf, (7*SCREEN_WIDTH/20, totalHeight))


    screen.blit(sWord, sBound)
    screen.blit(scissor.surf, (7*SCREEN_WIDTH/10, totalHeight))

    screen.blit(answer, aBounds)
#======
    pygame.display.flip()
