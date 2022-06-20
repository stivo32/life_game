import pygame
from pygame import Surface

from scenes.scene import Scene
from state import State


class StartButton(Surface):
    def __init__(self, scene: Scene):
        self.scene = scene
        self.width = 100
        self.height = 50
        self.clickable = True
        super().__init__((self.width, self.height))
        self.fill('Black')
        self.font = pygame.font.SysFont('Arial', 14)
        self.text = self.font.render('start', True, 'Black')
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.width // 2, self.height // 2)
        self.border = pygame.Rect((5, 5), (self.width - 10, self.height - 10))
        pygame.draw.rect(self, 'White', self.border)
        self.blit(self.text, self.textRect)
        self.left = 0
        self.top = 0
        self.calculate_coordinates()

    def calculate_coordinates(self):
        self.left = (self.scene.width - self.width) // 2
        self.top = self.scene.height - self.height - 40

    def update(self, event: pygame.event.Event):
        if event.button == 1:
            if self.click_inside(*event.pos):
                self.scene.app.change_state(State.game)

    def click_inside(self, cursor_x: int, cursor_y: int) -> bool:
        return self.left < cursor_x < self.left + self.width and self.top < cursor_y < self.top + self.height
