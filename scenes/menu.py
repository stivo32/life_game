from random import randint

import pygame
from pygame.locals import *

from scene import Scene
from state import State


class Menu(Scene):
    def __init__(self, app):
        self.app = app
        self.app.screen = pygame.display.set_mode((640, 480))
        self.app.background = (0, 0, 0)
        self.objects = []

    def update(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                self.app.background = [randint(0, 255) for _ in range(3)]
                self.app.screen.fill(self.app.background)
            elif event.button == 2:
                self.app.change_state(State.game)



class Menu2(Scene):
    def __init__(self, app):
        self.app = app
        self.app.screen = pygame.display.set_mode((720, 580))
        self.app.background = (0, 0, 0)
        self.objects = []

    def update(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                self.app.background = [randint(0, 255) for _ in range(3)]
            elif event.button == 2:
                self.app.change_state(State.menu)
        self.app.screen.fill(self.app.background)