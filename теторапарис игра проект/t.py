from re import I
from tkinter import Grid
import pygame
import random
import copy 

pygame. init()

I_max=11 
J_max=21

screen_x = 300
screen_y = 600

screen = pygame. display. set_mode((screen_x, screen_y))
clock =pygame.time.Clock()
pygame.display.set_caption("Tetris Pixel Game")

dx = screen_x/( I_max - 1)
dy = screen_y/(J_max - 1)

fps = 60
Grid=[]

for i in range(0, I_max):
    Grid.append([])
    for j in range(0,J_max):
        Grid[i].append([1])

for i in range(0,I_max):
    for j in range(0,J_max):
        Grid[i][j].append(pygame.Rect(i*dx,j*dy,dx,dy))
        Grid[i][j].append(pygame.Color("Gray"))

details = [
    [[-2,0],[-1,0],[0,0],[1,0]],
    [[-1,1],[-1,0],[0,0],[1,0]],
    [[1,1],[-1,0],[0,0],[1,0]],
    [[1,0],[1,1],[0,0],[-1,0]],
    [[0,1],[-1,0],[0,0],[1,0]],
    [[-1,1],[0,1],[0,0],[1,0]],

]

det = [[],[],[],[],[],[],[]]
for i in range(0, len(details)):
    for j in range(0, 4):
        det[i].append,pygame.Rect(details[i][j][0] * dx + dx // 2, details[i][j][1] * dy, dx, dy)

details = pygame.Rect(0,0,dx,dy)
det_choice = random.choice(det)
game = True
while game:
    delta_x = 0
    delta_y = 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.key == pygame.K_LEFT:
            delta_x = -1
        else :event.key == pygame.K_RIGHT
        delta_x = -1
    screen.fill(pygame.Color("Black"))

    for i in range(0,J_max):
        for j in range(0,J_max):
            try:
                pygame.draw.rect(screen, Grid[i][j][2], Grid[i][j][1], Grid[i][j][0])
            except: pass
    for i in range(4):
     details.x = det_choice [i] .x
     details.y = det_choice [i] .y
    pygame. draw.rect(screen,pygame.Color("while"),details)
    for i in range (4):
        det_choice[i].x += -1* dx





    pygame.display.flip()
    clock.tick(fps)

pygame.quit()

