# a package for building barriers
# coding:utf-8
# Author:The Crazy Turtle
# Date:2021/03/13

import pygame


class Balls:
    def __init__(self, image, surface, size):
        self.WIN = surface
        self.size = size
        self.image = image
        self.pos = [0, 0]
        self.pic = pygame.transform.smoothscale(pygame.image.load(self.image),
                                                self.size)

    def create(self, pos):
        self.pos = pos
        self.WIN.blit(self.pic, self.pos)
