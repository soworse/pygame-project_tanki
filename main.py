import os
import sys

import pygame

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 600, 600

pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(WINDOW_SIZE)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Hero(pygame.sprite.Sprite):
    def __init__(self, *group):
        super(Hero, self).__init__(*group)
        self.image = load_image('tank.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.dig = 0

    def update(self, vx, vy):
        self.rect.x += vx
        self.rect.y += vy

    def turn(self, a):
        self.image = pygame.transform.rotate(self.image, abs(a - self.dig))
        self.dig = a
        print(self.dig, '     ', a)


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)

    all_sprites = pygame.sprite.Group()

    hero = Hero(all_sprites)

    running = True
    pos_ = 0, 0
    while running:
        pygame.mouse.set_visible(0)
        screen.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    hero.update(-10, 0)
                    hero.turn(0)
                if event.key == pygame.K_RIGHT:
                    hero.update(10, 0)
                    hero.turn(180)
                if event.key == pygame.K_UP:
                    hero.update(0, -10)
                    hero.turn(90)
                if event.key == pygame.K_DOWN:
                    hero.update(0, 10)
                    hero.turn(270)
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()


main()
