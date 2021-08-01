import pygame
import time

# Initializing Pygame
pygame.init()

# Initializing surface
surface = pygame.display.set_mode((750, 550))

# Initialing Color
color = (255, 0, 0)

# Drawing Rectangle
background_image = pygame.image.load("table.jpg")
font1 = pygame.font.Font('freesansbold.ttf', 25)
font2 = pygame.font.Font('freesansbold.ttf', 25)
textX1 = 315
textY1 = 10

textX2 = 315
textY2 = 40


def show_score(x1, y1, x2, y2):
    scoredisplay1 = font1.render("PLAYER-1 :" + str(SCOREP1), True, (255, 0, 0))
    scoredisplay2 = font1.render("PLAYER-2 :" + str(SCOREP2), True, (0, 0, 139))
    surface.blit(scoredisplay1, (x1, y1))
    surface.blit(scoredisplay2, (x2, y2))


X1 = 10
Y1 = 20
width1 = 10
height1 = 70
change1 = 0
SCOREP1 = 0


def player1(a, b, c, d):
    pygame.draw.rect(surface, color, pygame.Rect(a, b, c, d))


X2 = 730
Y2 = 460
width2 = 10
height2 = 70
change2 = 0
SCOREP2 = 0


def player2(a, b, c, d):
    pygame.draw.rect(surface, (0, 0, 139), pygame.Rect(a, b, c, d))


# coordinates of centre of circle
Rx = 30
Ry = 55
R = 10  # radius of circle
changeR = 0.35
slope = (11 / 6)
collideX = 30
collideY = 55


def ball(rx, ry, r):
    pygame.draw.circle(surface, (0, 255, 0), (rx, ry), r)


running = True

while running:
    surface.fill((0, 0, 0))
    surface.blit(background_image, (0, 0))
    for event in pygame.event.get():  # this will keep looking for all the events happening in pygame window module
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                print("down pressed!")
                change1 = 0.5

            if event.key == pygame.K_w:
                print("up press")
                change1 = -0.5

            if event.key == pygame.K_DOWN:
                print("down pressed!")
                change2 = 0.5

            if event.key == pygame.K_UP:
                print("up press")
                change2 = -0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s or event.key == pygame.K_w or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                print("key release")
                change1 = 0
                change2 = 0
    Y1 = Y1 + change1
    Y2 = Y2 + change2
    RX = Rx
    RY = Ry

    Rx = Rx + changeR
    Ry = ((slope) * (Rx - RX)) + RY
    if Ry >= 550:
        collideY = 550
        collideX = Rx
        Ry = 550
        slope = -slope
    if Ry <= 0:
        collideY = 0
        collideX = Rx
        Ry = 0
        slope = -slope

    if Rx >= 720 and (Y2 + 70) >= Ry and Ry >= Y2:
        collideY = Ry
        collideX = 740
        Rx = 720
        slope = -slope
        changeR = -0.35
    if Rx <= 30 and (Y1 + 70) >= Ry and Ry >= Y1:
        collideY = Ry
        collideX = 10
        Rx = 30
        slope = -slope
        changeR = 0.35
    if Rx >= 750:
        SCOREP1 = SCOREP1 + 1
        print("PLAYER 1 :", SCOREP1, " PLAYER 2 :", SCOREP2)
        Rx = 720
        Ry = Y2 + (height2 / 2)
        time.sleep(2)
    if Rx <= 0:
        SCOREP2 = SCOREP2 + 1
        print("PLAYER 1 :", SCOREP1, " PLAYER 2 :", SCOREP2)
        Rx = 30
        Ry = Y1 + (height1 / 2)
        time.sleep(2)
    if Y1 >= 480:
        Y1 = 480

    if Y1 <= 0:
        Y1 = 0

    if Y2 >= 480:
        Y2 = 480

    if Y2 <= 0:
        Y2 = 0
    player1(X1, Y1, width1, height1)
    player2(X2, Y2, width2, height2)
    ball(Rx, Ry, R)
    show_score(textX1, textY1, textX2, textY2)

    # pygame.draw.circle(surface, (0, 255, 0), (30, 55), 10)

    pygame.display.update()
