from random import randint
from typing import Optional

import pygame
from pygame.locals import *

from .scene import Scene
from state import State
from buttons.start_button import StartButton


class Menu(Scene):
    def __init__(self, app):
        self.app = app
        self.width = 640
        self.height = 480
        self.app.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Menu')
        self.start_button = StartButton(self)
        self.objects = [self.start_button]
        self.clickables = [self.start_button]

    def update(self, event: Optional[pygame.event.Event] = None):
        self.app.screen.fill(self.app.background)
        self.draw_objects()
        if event is None:
            return
        if event.type == MOUSEBUTTONDOWN:
            self.click_update(event)

    def draw_objects(self):
        for obj in self.objects:
            self.app.screen.blit(obj, (obj.x, obj.y))

    def click_update(self, event: pygame.event.Event):
        for obj in self.clickables:
            obj.update(event)