# coding:utf-8
# Author:The Crazy Turtle
# Date:2021/03/24

import pygame
import packages.pic
import packages.button_block
import pygame.freetype
import random

FPS = 30
WHITE = 255, 255, 255
BLACK = 0, 0, 0
BLOCK_GREY = 204, 204, 204
GOLD = 255, 230, 85
ORANGE = 247, 163, 111
BLUE = 83, 169, 212
GRASS_GREEN = 233, 245, 230
WIDTH, HEIGHT = 1200, 800
MAX_LEN = 10
BAR_WIDTH = 60
BAR_TOP = 100
screen_size = WIDTH, HEIGHT
balls_r = 20
bar_r = 10
balls_num = 1
balls_start_num = 0
bottom = HEIGHT - 100

pygame.init()
screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
icon = pygame.image.load("icon.png").convert_alpha()
pygame.display.set_caption("Galton Plate")
pygame.display.set_icon(icon)
font_1 = pygame.freetype.Font(r"C:\Windows\Fonts\tt0769m_.ttf", 36)
font_2 = pygame.freetype.Font(r"C:\Windows\Fonts\tt0769m_.ttf", 60)
fps_clock = pygame.time.Clock()
wood_background = packages.pic.Balls("wood_background.png", screen, (WIDTH, HEIGHT))

screen.fill(WHITE)
balls = []
bars = []
bars_num = []
# ball:[image,[speed_x,speed_y],[pos_x,pos_y]]
# balls[0][0]   [0][1][0/1]     [0][2][0/1]
# pos_x+=speed_x    -->     balls[0][2][0/1]+=balls[0][1][0/1]
for j in range(0, MAX_LEN, 1):
    for k in range(0, j, 1):
        bar = [packages.pic.Balls("barriers.png", screen, (2 * bar_r, 2 * bar_r)),
               [WIDTH / 2 - BAR_WIDTH * 2 * (k - (j - 1) / 2) - bar_r, BAR_TOP + j * BAR_WIDTH]]
        bars.append(bar)
# create barriers
for j in range(0, MAX_LEN+2, 1):
    bars_num.append(0)


def draw():
    global balls_start_num, balls, bars_num
    wood_background.create((0, 0))
    # the ball on falling
    for i in range(balls_start_num, balls_num-1):
        balls[i][0].create(balls[i][2])
        delta_y = BAR_TOP + BAR_WIDTH * (MAX_LEN - 1/2) - balls[i][2][1] - 2 * balls_r
        if delta_y - BAR_WIDTH * (MAX_LEN - 1/2) > 0:
            balls[i][1][1] += 3
        elif delta_y < 0:
            balls[i][1][0] = 0
        elif delta_y % BAR_WIDTH < 9:
            balls[i][1][0] = (2 * int(random.random() + 1 / 2) - 1) * balls[i][1][1]
        balls[i][2][0] += balls[i][1][0]
        balls[i][2][1] += balls[i][1][1]
    if balls[balls_start_num][2][1] > bottom:
        bars_num[int((balls[balls_start_num][2][0]-(WIDTH-(MAX_LEN+1)*BAR_WIDTH*2)/2)/(BAR_WIDTH*2))+1] += 1
        balls[balls_start_num][2][1] = bottom   # - balls_r * balls_start_num
        balls_start_num += 1
    for i in range(0, MAX_LEN+2, 1):
        font1_surface, font1_rect = font_1.render(str(bars_num[i]), fgcolor=BLACK, bgcolor=WHITE)
        screen.blit(font1_surface, ((WIDTH-(MAX_LEN+1)*BAR_WIDTH*2)/2+BAR_WIDTH*2*i,
                                    HEIGHT - font1_rect[3]))
    for i in range(0, balls_start_num):
        balls[i][0].create(balls[i][2])
    for bar_ in bars:
        bar_[0].create(bar_[1])


def main():
    global balls, balls_num
    mouse_pos = [0, 0]
    ball = [packages.pic.Balls("balls.png", screen, (2*balls_r, 2*balls_r)),
            [0, 0], [WIDTH/2 - balls_r, 50]]
    balls.append(ball)
    balls[0][0].create(balls[0][2])
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and balls[balls_num-1][2][1]:
                mouse_pos[0], mouse_pos[1] = event.pos[0], event.pos[1]
                balls_num += 1
                ball = [packages.pic.Balls("balls.png", screen, (balls_r * 2, balls_r * 2)),
                        [0, 0], [WIDTH/2 - balls_r, 50]]
                balls.append(ball)
        draw()
        pygame.display.update()
        fps_clock.tick(FPS)
    main()


if __name__ == "__main__":
    main()
