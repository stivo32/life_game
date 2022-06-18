from random import randint

import pygame
from pygame import MOUSEBUTTONDOWN

from .scene import Scene
from state import State


BLUE = (0, 0, 255)


class ColorChanger(Scene):
    def __init__(self, app):
        self.app = app
        self.objects = []

    def update(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                print(event)
                print(event.__dict__)
                pygame.draw.circle(self.app.screen, BLUE, event.pos, randint(15, 40))
            elif event.button == 3:
                self.app.change_state(State.menu)
