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


# 0. define callbacks - functions that run when events happen.
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("gamep2/test", qos=1)
    client.publish("gamep1/test", 0, qos=1)

# The callback of the client when it disconnects.
def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected Disconnect")
    else:
        print("Expected Disconnect")
# The default message callback.
# (you can create separate callbacks per subscribed topic)
def on_message(client, userdata, message):
    #print("Received message: " + str(message.payload) + " on topic " + message.topic + " with QoS " + str(message.qos))
    comp = int(message.payload)
    user = int(input("Choose Rock: 1, Paper: 2, or Scissors: 3 \n"))
    win = ""
    if (user == comp):
        win = ("Tie")
    if (user == 1):
        if (comp == 2):
            win = ("You Wins!")
        elif (comp == 3):
            win = ("Player 2 Wins!")
    elif (user == 2):
        if (comp == 3):
            win = ("You Wins!")
        elif (comp == 1):
            win = ("Player 2 Wins!")
    elif (user == 3):
        if (comp == 1):
            win = ("You Wins!")
        elif (comp == 2):
            win = ("Player 2 Wins!")
    else:
        print("Incorrect Input please try again.")
    client.publish("gamep2/test", win, qos=1)

# 1. create a client instance.
client = mqtt.Client()
# add additional client options (security, certifications, etc.)
# many default options should be good to start off.
# add callbacks to client.
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
# 2. connect to a broker using one of the connect*() functions.
# client.connect_async("test.mosquitto.org")
client.connect_async("mqtt.eclipseprojects.io")
# client.connect("test.mosquitto.org", 1883, 60)
# client.connect("mqtt.eclipse.org")
# 3. call one of the loop*() functions to maintain network traffic flow with the broker.


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
                on_message("gamep1/test", 0,inp)
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
    pygame.display.flip()

client.loop_start()
# client.loop_forever()
while True: # perhaps add a stopping condition using some break or something.
    pass # do your non-blocked other stuff here, like receive IMU data or something.
# use subscribe() to subscribe to a topic and receive messages.
# use publish() to publish messages to the broker.
# use disconnect() to disconnect from the broker.
client.loop_stop()
client.disconnect()

