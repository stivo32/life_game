from abc import ABC, abstractmethod

import pygame


class Scene(ABC):
    @abstractmethod
    def __init__(self, app):
        pass

    @abstractmethod
    def update(self, event: pygame.event.Event):
        pass
