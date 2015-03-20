import pygame
import sys
import time
from pygame.locals import *

pygame.init()

# variables definitions
img_x = 1
img_y = 1
img_movement = "down"

# colours definitions
black = (0, 0, 0)

# object definitions
pygame.display.set_caption("3chess")
setDisplay = pygame.display.set_mode((600, 480))
img = pygame.image.load("/home/maciej/Copy/Pictures/Ikony/lol.jpg")
img = pygame.transform.scale(img, (90, 90))


while True:

    setDisplay.fill(black)

    # define movements
    if img_movement == "down":
        img_y += 1
    if img_movement == "up":
        img_y -= 1

    # define events
    if img_y > 390:
        img_movement = "up"
    if img_y < 0:
        img_movement = "down"
        
    # blit img
    setDisplay.blit(img, (img_x,img_y))

    for event in pygame.event.get():
        # print all events in console
        print event
        # define quit action
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
