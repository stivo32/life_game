from random import randint

import pygame
from pygame.constants import *

from .scene import Scene
from state import State


BLUE = (0, 0, 255)


class ColorChanger(Scene):
    def __init__(self, app):
        self.app = app
        self.width = 720
        self.height = 560
        self.app.screen = pygame.display.set_mode((640, 640))
        pygame.display.set_caption('Game')
        self.objects = []

    def update(self, event: pygame.event.Event):
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.draw.circle(self.app.screen, BLUE, event.pos, randint(15, 40))
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                self.app.change_state(State.menu)
