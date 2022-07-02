from abc import ABC, abstractmethod

import pygame

from settings import WINDOW_SIZE


class Scene(ABC):
    @abstractmethod
    def __init__(self, app):
        self.app = app
        self.width, self.height = WINDOW_SIZE

    @abstractmethod
    def update(self, event: pygame.event.Event):
        pass
