from typing import Optional

import pygame
from pygame.locals import *

from buttons.start_button import StartButton
from .scene import Scene


class Menu(Scene):
    def __init__(self, app):
        super().__init__(app)
        pygame.display.set_caption('Menu')
        self.start_button = StartButton(self)
        self.objects = [self.start_button]

    def update(self, event: Optional[pygame.event.Event] = None):
        self.app.screen.fill(self.app.background)
        self._draw_objects()
        if event is None:
            return
        if event.type == MOUSEBUTTONDOWN:
            self._click_update(event)

    def _draw_objects(self):
        for obj in self.objects:
            self.app.screen.blit(obj, (obj.left, obj.top))

    def _click_update(self, event: pygame.event.Event):
        for obj in self._clickable:
            obj.update(event)

    @property
    def _clickable(self):
        return [obj for obj in self.objects if hasattr(obj, 'clickable')]