import sys

import pygame
import pygame.color

from scenes.life_game import LifeGame
from scenes.menu import Menu
from state import State
from settings import WINDOW_SIZE, FPS


class App:
    def __init__(self):
        pygame.init()
        self.fps = FPS
        self.frames = pygame.time.Clock()
        self.background = pygame.Color('white')
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.running = True
        self.state = State.menu
        self.scene = None

    def set_scene(self):
        scene_mapper = {
            State.menu: Menu,
            State.game: LifeGame
        }
        self.scene = scene_mapper[self.state](self)

    def change_state(self, state: State):
        self.state = state
        self.set_scene()

    def run(self):
        self.set_scene()
        pygame.display.update()
        while self.running:
            self.frames.tick(self.fps)
            for event in pygame.event.get():
                self.check_stop(event)
                self.scene.update(event)
            else:
                self.scene.update()
            pygame.display.flip()

        pygame.quit()
        sys.exit()

    def check_stop(self, event: pygame.event.Event):
        if event.type == pygame.QUIT:
            self.running = False
