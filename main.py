import pygame
import os
import sys
import random

pygame.init()
arrow = pygame.image.load('Tank-GTA2.png')
DEFAULT_IMAGE_SIZE = (50, 50)

# Scale the image to your needed size
arrow = pygame.transform.scale(arrow, DEFAULT_IMAGE_SIZE)
screen = pygame.display.set_mode((500, 500))
flag = True
x1, y1 = 0, 0
while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x1 += 10
                arrow = pygame.transform.rotate(arrow, 90)
            if event.key == pygame.K_LEFT:
                x1 -= 10
                arrow = pygame.transform.rotate(arrow, 90)
            if event.key == pygame.K_DOWN:
                y1 += 10
                arrow = pygame.transform.rotate(arrow, 90)
            if event.key == pygame.K_UP:
                y1 -= 10
        screen.blit(arrow, (x1, y1))
        pygame.display.flip()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
