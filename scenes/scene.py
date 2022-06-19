from abc import ABC, abstractmethod

import pygame


class Scene(ABC):
    @abstractmethod
    def __init__(self, app):
        self.app = app
        self.width = 0
        self.height = 0

    @abstractmethod
    def update(self, event: pygame.event.Event):
        pass
