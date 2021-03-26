# coding:utf-8
# Author:The Crazy Turtle
# Date:2021/03/13

import pygame
import pygame.freetype

pygame.init()
font_1 = pygame.freetype.Font(r"C:\Windows\Fonts\tt0769m_.ttf", 36)


class Buttons:
    def __init__(self, screen, center_pos, size, text, bgcolor, fgcolor, font_size=24):
        self.screen = screen
        self.pos = center_pos
        self.size = size
        self.text = text
        self.bgcolor = bgcolor
        self.fgcolor = fgcolor
        self.font_size = font_size
        self.font = pygame.freetype.Font(r"C:\Windows\Fonts\tt0769m_.ttf", self.font_size)

    def show(self):
        global font_1
        pygame.draw.rect(self.screen, self.bgcolor,
                         (self.pos[0]-int(self.size[0]/2),
                          self.pos[1]-int(self.size[1]/2),
                          self.size[0], self.size[1]))
        button_text_surface, button_text_rect = self.font.render(self.text,
                                                                 fgcolor=self.fgcolor,
                                                                 bgcolor=self.bgcolor)
        self.screen.blit(button_text_surface,
                         (self.pos[0]-int(button_text_rect[2]/2),
                          self.pos[1]-int(button_text_rect[3]/2)))

    def colli_check(self, mouse_pos):
        button_text_surface, button_text_rect = self.font.render(self.text,
                                                                 fgcolor=self.fgcolor,
                                                                 bgcolor=(150, 150, 150))
        if self.pos[0]-int(self.size[0]/2) < mouse_pos[0] < self.pos[0]+int(self.size[0]/2):
            if self.pos[1]-int(self.size[1]/2) < mouse_pos[1] < self.pos[1]+int(self.size[1]/2):
                pygame.draw.rect(self.screen, (150, 150, 150),
                                 (self.pos[0] - int(self.size[0] / 2),
                                  self.pos[1] - int(self.size[1] / 2),
                                  self.size[0], self.size[1]))
                self.screen.blit(button_text_surface,
                                 (self.pos[0] - int(button_text_rect[2] / 2),
                                  self.pos[1] - int(button_text_rect[3] / 2)))
                return 1
        return 0
