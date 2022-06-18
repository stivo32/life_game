import sys

import pygame

from scenes.color_changer import ColorChanger
from scenes.menu import Menu
from state import State


class App:
    def __init__(self):
        pygame.init()
        self.fps = pygame.time.Clock()
        self.fps.tick(60)
        self.background = (0, 0, 0)
        self.screen = pygame.display.set_mode((640, 480))
        self.running = True
        self.state = State.menu
        self.scene = None

    def set_scene(self):
        scene_mapper = {
            State.menu: Menu,
            State.game: ColorChanger
        }
        self.scene = scene_mapper[self.state](self)

    def change_state(self, state: State):
        self.state = state
        self.set_scene()

    def run(self):
        self.set_scene()
        while self.running:
            for event in pygame.event.get():
                self.check_stop(event)
                self.scene.update(event)
            pygame.display.update()
        pygame.quit()
        sys.exit()

    def check_stop(self, event: pygame.event.Event):
        if event.type == pygame.QUIT:
            self.running = False
