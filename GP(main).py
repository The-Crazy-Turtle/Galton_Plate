# coding:utf-8
# Author:The Crazy Turtle
# Date:2021/03/24

import pygame
import packages.pic
import packages.button_block
import pygame.freetype
import random
import matplotlib
import matplotlib.pyplot as plt

# sqlite3 ?

FPS = 30
WHITE = 255, 255, 255
BLACK = 0, 0, 0
BLOCK_GREY = 204, 204, 204
GOLD = 255, 230, 85
ORANGE = 247, 163, 111
BLUE = 83, 169, 212
GRASS_GREEN = 233, 245, 230
WIDTH, HEIGHT = 1000, 700
MAX_LEN = 20
BAR_WIDTH = 25
BAR_TOP = 60
screen_size = WIDTH, HEIGHT
balls_r = 5
bar_r = 5
balls_num = 0
balls_total_num = 0
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
matplotlib.rcParams['font.sans-serif'] = ['SimHei']

screen.fill(WHITE)
balls = []
bars = []
bars_num = []
# ball:[image,[speed_x,speed_y],[pos_x,pos_y]]
# balls[0][0]   [0][1][0/1]     [0][2][0/1]
# pos_x+=speed_x    -->     balls[0][2][0/1]+=balls[0][1][0/1]
for j in range(0, MAX_LEN, 1):
    bars.append([])
    for k in range(0, j, 1):
        bar = [packages.pic.Balls("barriers.png", screen, (2 * bar_r, 2 * bar_r)),
               [WIDTH / 2 - BAR_WIDTH * (j - 1) + 2 * k * BAR_WIDTH - bar_r, BAR_TOP + j * BAR_WIDTH]]
        bars[j].append(bar)
# create barriers
for j in range(0, MAX_LEN, 1):
    bars_num.append(0)
LEFT = bars[MAX_LEN - 1][0][1][0] - BAR_WIDTH * 2 + bar_r
# messages
add_surface, add_rect = font_1.render("Add:",
                                      fgcolor=BLACK, bgcolor=WHITE)
# create arrow
arrow = packages.pic.Balls("arrow.png", screen, (int(1.5 * add_rect[3]), add_rect[3]))

# button
button_run = packages.button_block.Buttons(screen, (50, 80), (60, 40),
                                           "Run",
                                           bgcolor=BLUE, fgcolor=ORANGE,
                                           font_size=30)
button_finish = packages.button_block.Buttons(screen, (50, 140), (60, 40),
                                              "Finish",
                                              bgcolor=BLOCK_GREY, fgcolor=ORANGE,
                                              font_size=24)
button_draw = packages.button_block.Buttons(screen, (50, 200), (60, 40),
                                            "Draw",
                                            bgcolor=BLOCK_GREY, fgcolor=ORANGE,
                                            font_size=24)


def draw(mouse_pos, text=''):
    global balls_start_num, balls, bars_num
    wood_background.create((0, 0))  # background
    # the ball on falling
    for i in range(balls_start_num, balls_num - 1):  # change balls' speed
        balls[i][0].create(balls[i][2])
        delta_y = BAR_TOP + BAR_WIDTH * (MAX_LEN - 1 / 2) - balls[i][2][1] - 2 * balls_r
        if delta_y - BAR_WIDTH * (MAX_LEN - 1 / 2) > 0:
            balls[i][1][1] += 3
        elif delta_y < 0:
            balls[i][1][0] = 0
        elif (delta_y + BAR_WIDTH + balls[i][1][1]) % BAR_WIDTH < (delta_y + BAR_WIDTH) % BAR_WIDTH:
            balls[i][1][0] = (2 * int(random.random() + 1 / 2) - 1) * balls[i][1][1]
        balls[i][2][0] += balls[i][1][0]
        balls[i][2][1] += balls[i][1][1]
    if balls[balls_start_num][2][1] > bottom:  # see if the ball is on the ground
        bars_num[int((balls[balls_start_num][2][0] + balls_r - LEFT) / (BAR_WIDTH * 2))] += 1
        balls[balls_start_num][2][1] = bottom  # - balls_r * balls_start_num
        balls_start_num += 1
    for i in range(0, MAX_LEN, 1):  # show data
        font1_surface, font1_rect = font_1.render(str(bars_num[i]),
                                                  fgcolor=BLACK, bgcolor=WHITE)
        screen.blit(font1_surface, (LEFT + BAR_WIDTH * (2 * i + 1),
                                    HEIGHT - font1_rect[3]))
        if bars_num[i] != 0:
            balls[0][0].create((LEFT + BAR_WIDTH * (2 * i + 1), bottom))
    total_surface, total_rect = font_1.render("Total Balls Number : " + str(balls_total_num - 1),
                                              fgcolor=BLACK, bgcolor=WHITE)
    screen.blit(total_surface, (WIDTH - total_rect[2] - 20, 20))
    for bar_ in bars:  # show bars
        for bar__ in bar_:
            bar__[0].create(bar__[1])

    # the input box, font1 is "Add" message
    screen.blit(add_surface, (20, 20))
    pygame.draw.rect(screen, BLOCK_GREY, (20 + add_rect[2], 20,
                                          100, add_rect[3]))

    # show input, font2 is input
    if text != "":
        font2_surface, font2_rect = font_1.render(text,
                                                  fgcolor=BLACK, bgcolor=BLOCK_GREY)
        screen.blit(font2_surface,
                    (25 + add_rect[2], 20 + add_rect[3] / 2 - font2_rect[3] / 2))

    # show arrow
    arrow.create((125 + add_rect[2], 20))

    # check add
    button_run.show()
    button_run.colli_check(mouse_pos)
    button_finish.show()
    button_finish.colli_check(mouse_pos)
    button_draw.show()
    button_draw.colli_check(mouse_pos)


def finish(add_num):
    global bars_num, balls_total_num
    for now_1 in range(0, add_num):
        balls_now = 0
        for now_2 in range(0, MAX_LEN - 1):
            balls_now += int(random.random() + 1 / 2) - 1 / 2
        bars_num[int(balls_now + MAX_LEN / 2)] += 1
    balls_total_num += add_num
    return 0


def add(add_num):  # add balls
    global balls_num, balls, balls_total_num
    balls_num += 1
    balls_total_num += 1
    ball = [packages.pic.Balls("balls.png", screen, (balls_r * 2, balls_r * 2)),
            [0, 0], [WIDTH / 2 - balls_r, 10]]
    balls.append(ball)
    return add_num - 1


def main():
    global balls
    add_num = 0
    mouse_pos = [0, 0]
    add(1)
    balls[0][0].create(balls[0][2])
    run = True
    text = [[]]
    x = []
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and balls[balls_num - 1][2][1]:
                if button_run.colli_check(event.pos):
                    mouse_pos[0], mouse_pos[1] = event.pos[0], event.pos[1]
                    num = 0  # record input number in "add" box
                    for number in text[0]:
                        num = num * 10 + (ord(number) - ord('0'))
                    add_num += num
                elif button_finish.colli_check(event.pos):
                    add_num = finish(add_num)
                elif button_draw.colli_check(event.pos):
                    for i in range(0, MAX_LEN, 1):
                        x.append(i)
                    plt.plot(x, bars_num, "black", marker='.', ms=10, label="伽尔顿板")
                    plt.title("伽尔顿板", fontdict={'family': 'SimHei', 'size': 20})
                    plt.xlabel("小球数", fontdict={'family': 'SimHei', 'size': 16})
                    plt.ylabel("位置", fontdict={'family': 'SimHei', 'size': 16})

                    # upper left 将图例a显示到左上角
                    plt.legend(loc="upper left", prop={'family': 'SimHei', 'size': 16})

                    ax = plt.gca()
                    ax.spines['right'].set_color('none')  # right边框属性设置为none 不显示
                    ax.spines['top'].set_color('none')  # top边框属性设置为none 不显示
                    plt.show()
                else:
                    # increase ball
                    add(1)
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = [0, 0]
            elif event.type == pygame.KEYDOWN:  # contain "Add"
                if event.key == pygame.K_BACKSPACE and text[0] != []:
                    text[0].pop()
                elif '0' <= event.unicode <= '9':
                    text[0].append(event.unicode)
        if add_num > 0:
            add_num = add(add_num)
        draw(mouse_pos, "".join(text[0]))
        pygame.display.update()
        fps_clock.tick(FPS)
    main()


if __name__ == "__main__":
    main()
