from paddle import Paddle
from ball import Ball
from collections import namedtuple 
import random
import pygame

pygame.init()

pygame.display.set_caption("My Pong")
# create a surface
WIDTH = 800
HEIGHT = 400
BORDER = 15
VELOCITY = 10
FPS = 30

Constants = namedtuple("Constants", ["WIDTH", "HEIGHT", "BORDER", "VELOCITY", "FPS"])
CONSTS = Constants(WIDTH, HEIGHT, BORDER, VELOCITY, FPS)


screen = pygame.display.set_mode((WIDTH, HEIGHT))

#  add solid background: r, g, b
screen.fill((0,0,0))
pygame.display.update()

# Draw walls as rectangles
# rect(surface, color, rect)
# Rect((x, y), (width, height))
wcolor = pygame.Color("white")
bgcolor = pygame.Color("black")
# top wall
pygame.draw.rect(screen, wcolor, pygame.Rect((0,0), (WIDTH, BORDER)))

# left wall
pygame.draw.rect(screen, wcolor, pygame.Rect((0,0), (BORDER, HEIGHT)))

# Bottom
pygame.draw.rect(screen, wcolor, pygame.Rect((0,HEIGHT-BORDER), (WIDTH, BORDER)))

# Ball init
x0 = WIDTH - Ball.RADIUS
y0 = HEIGHT // 2
vx0 = -VELOCITY
vy0 = random.randint(-VELOCITY, VELOCITY+1)

b0 = Ball(x0, y0, vx0, vy0, screen, wcolor, bgcolor, CONSTS)
b0.show(wcolor)

pygame.display.update()

# define a variable to control the main loop
running = True
clock = pygame.time.Clock()
# main loop
while running:
    # event handling, gets all event from the event queue
    for event in pygame.event.get():
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
                running = False
        pygame.display.update()
        clock.tick(FPS)
        # Ball
        b0.update()
     
     