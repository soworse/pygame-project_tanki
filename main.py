import pygame
import os
import sys
import random

pygame.init()
arrow = pygame.image.load('Tank-GTA2.png')
DEFAULT_IMAGE_SIZE = (150, 50)
a = 0
old_a = -1
# Scale the image to your needed size
arrow = pygame.transform.scale(arrow, DEFAULT_IMAGE_SIZE)
screen = pygame.display.set_mode((500, 500))
flag = True
x1, y1 = 0, 0
while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        print(old_a)
        print(a)    
        if event.type == pygame.KEYDOWN:
            old_a = a
            if event.key == pygame.K_RIGHT:
                x1 += 10
                a = 1
            if event.key == pygame.K_LEFT:
                x1 -= 10
                a = 2
            if event.key == pygame.K_DOWN:
                y1 += 10
                a = 3
            if event.key == pygame.K_UP:
                a = 4
                y1 -= 10

        if old_a == 1 and a == 2:
            arrow = pygame.transform.rotate(arrow, 180)
        if old_a == 1 and a == 3:
            arrow = pygame.transform.rotate(arrow, -90)
        if old_a == 1 and a == 4:
            arrow = pygame.transform.rotate(arrow, 90)
        if old_a == 2 and a == 1:
            arrow = pygame.transform.rotate(arrow, 180)
        if old_a == 2 and a == 3:
            arrow = pygame.transform.rotate(arrow, 90)
        if old_a == 2 and a == 4:
            arrow = pygame.transform.rotate(arrow, -90)
        if old_a == 3 and a == 1:
            arrow = pygame.transform.rotate(arrow, 90)
        if old_a == 3 and a == 2:
            arrow = pygame.transform.rotate(arrow, -90)
        if old_a == 3 and a == 4:
            arrow = pygame.transform.rotate(arrow, 180)
        if old_a == 4 and a == 1:
            arrow = pygame.transform.rotate(arrow, 90)
        if old_a == 4 and a == 2:
            arrow = pygame.transform.rotate(arrow, -90)
        if old_a == 4 and a == 3:
            arrow = pygame.transform.rotate(arrow, 180)

        screen.blit(arrow, (x1, y1))
        pygame.display.flip()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
