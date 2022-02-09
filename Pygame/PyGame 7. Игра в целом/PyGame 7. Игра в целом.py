# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random


def move(xm, ym):
    global PLAYER_X, PLAYER_Y, CAMERA_X, CAMERA_Y
    x = xm
    y = ym
    x += PLAYER_X
    y += PLAYER_Y
    if LEVEL[y % N][x % M] != 1:
        PLAYER_X = x
        PLAYER_Y = y
        CAMERA_X -= xm * WB
        CAMERA_Y -= ym * WH
        return True
    return False

def f_x(x):
    return x + 1

def f_y(y):
    return y + 1

LEVEL = [
    '0001110000',
    '0011010111',
    '0110011100',
    '1100200000',
    '1001010100',
    '1111111100',
    '0010010000',
    '0110110101',
    '0100000011',
    '0100000110'

]

LEVEL = list(map(lambda x: x.strip(), open(input(), 'r').readlines()))
WB = 50
WH = 50
M = len(LEVEL[0])
N = len(LEVEL)
WIDTH = (M + 2) *  WB
HEIGHT = (N + 2) * WH
FPS = 30


# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PLAYER_X = 0
PLAYER_Y = 0
CAMERA_X = 0
CAMERA_Y = 0


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((WB, WH))
        self.image.fill(RED)
        player_img = pygame.image.load('mar.png').convert()
        self.image = player_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (PLAYER_X * WB + WB // 2, PLAYER_Y * WH + WH // 2)

    def update(self):
        self.rect.center = (f_x(PLAYER_X) * WB + WB // 2 + CAMERA_X, f_y(PLAYER_Y) * WH + WH // 2 + CAMERA_Y)


class Block(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((WB, WH))
        if color == 0:
            player_img = pygame.image.load('grass.png').convert()
            self.image = player_img
            self.image.set_colorkey(BLACK)
        elif color == 1:
            player_img = pygame.image.load('blockk.png').convert()
            self.image = player_img
            self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x * WB + WB // 2, y * WH + WH // 2)
        self.x = x
        self.y = y

    def update(self):
        self.rect.center = (f_x((self.x % M +  CAMERA_X // WB) % M) * WB + WB // 2, f_y((self.y + CAMERA_Y // WH) % N) * WH + WH // 2)


# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()


# Цикл игры
running = True
for y in range(len(LEVEL)):
    LEVEL[y] = list(map(int, list(LEVEL[y])))
    for x in range(len(LEVEL[0])):
        if LEVEL[y][x] == 2:
            PLAYER_X = x
            PLAYER_Y = y
            all_sprites.add(Block(0, x, y))
        else:
            all_sprites.add(Block(LEVEL[y][x], x, y))

player = Player()
all_sprites.add(player)


while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # If pressed key is ESC quit program
            if event.key == pygame.K_UP:
                move(0, -1)
            if event.key == pygame.K_DOWN:
                move(0, 1)
            if event.key == pygame.K_LEFT:
                move(-1, 0)
            if event.key == pygame.K_RIGHT:
                move(1, 0)

    # Обновление
    all_sprites.update()

    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
