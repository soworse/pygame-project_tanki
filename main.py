import os
import sys
import pygame

clock = pygame.time.Clock()
WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 600, 600
DEFAULT_IMAGE_SIZE = (100, 100)

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


class F_screen(pygame.sprite.Sprite):
    def __init__(self, *group):
        super(F_screen
              , self).__init__(*group)
        self.image = load_image('old-video-game-background-2451118.jpg')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0


class Hero(pygame.sprite.Sprite):
    def __init__(self, *group):
        super(Hero, self).__init__(*group)
        self.image = load_image('tankT.png')
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self, vx, vy):
        self.rect.x += vx
        self.rect.y += vy

    def turn(self, a):
        if a == 0:
            self.image = load_image('tankT.png')
            self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        elif a == 90:
            self.image = load_image('tankR.png')
            self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)

        elif a == 180:
            self.image = load_image('tankB.png')
            self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        else:
            self.image = load_image('tankL.png')
            self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)


def start_screen():
    intro_text = ["FASHION TANKI", 'press any button to start']
    fon = pygame.transform.scale(load_image('old-video-game-background-2451118.jpg'), (700, 700))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 350
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(50)


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    start_screen()
    all_sprites = pygame.sprite.Group()
    print(all_sprites)
    hero = Hero(all_sprites)
    running = True
    pos_ = 0, 0
    while running:
        pygame.mouse.set_visible(0)
        screen.fill('white')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    hero.update(-10, 0)
                    hero.turn(270)
                if event.key == pygame.K_RIGHT:
                    hero.update(10, 0)
                    hero.turn(90)
                if event.key == pygame.K_UP:
                    hero.update(0, -10)
                    hero.turn(0)
                if event.key == pygame.K_DOWN:
                    hero.update(0, 10)
                    hero.turn(180)
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()


main()
