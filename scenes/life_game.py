from random import random
from typing import Optional, Tuple

import pygame
from pygame.constants import *

from scenes.scene import Scene
import time


def performance(method):
    def decorator(*args, **kwargs):
        start = time.perf_counter()
        result = method(*args, **kwargs)
        print(f'{method.__name__} - {(time.perf_counter() - start)}')
        return result
    return decorator


class LifeGame(Scene):
    def __init__(self, app):
        self.app = app
        self.width = 720
        self.height = 560
        self.cell_size = 10
        self.app.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Life')
        self.app.background = (255, 255, 255)
        self.columns = self.width // self.cell_size
        self.rows = self.height // self.cell_size
        self.matrix = self.create_matrix()
        self.fill_matrix()
        self.draw_matrix()

    def create_matrix(self):
        return [[0] * self.rows for _ in range(self.columns)]

    @performance
    def fill_matrix(self):
        for i, row in enumerate(self.matrix):
            for j, _ in enumerate(row):
                self.matrix[i][j] = random() > 0.5

    def draw_matrix(self):
        for i, row in enumerate(self.matrix):
            for j, _ in enumerate(row):
                if self.matrix[i][j]:
                    cell_center = (i * self.cell_size + self.cell_size // 2, j * self.cell_size + self.cell_size // 2)
                    pygame.draw.circle(self.app.screen, 'Red', cell_center, self.cell_size // 3)

    def update(self, event: Optional[pygame.event.Event] = None):
        self.app.screen.fill(self.app.background)
        self.draw_matrix()
        self.calculate_next_generation()
        if event is None:
            return
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                self.calculate_next_generation()
            elif event.button == 3:
                self.invert_cell(event.pos)

    @performance
    def calculate_next_generation(self):
        next_gen_matrix = self.create_matrix()
        for i, row in enumerate(self.matrix):
            for j, _ in enumerate(row):
                next_gen_matrix[i][j] = self._dead_of_alive(self.matrix[i][j], self.get_neighbours(i, j))
        self.matrix = next_gen_matrix

    @staticmethod
    def _dead_of_alive(cell, neighbours):
        if cell:
            return 1 if neighbours in (2, 3) else 0
        else:
            return 1 if neighbours == 3 else 0

    def get_neighbours(self, cell_i: int, cell_j: int):
        count = 0
        for i in range(cell_i - 1, cell_i + 1 + 1):
            for j in range(cell_j - 1, cell_j + 1 + 1):
                if cell_i == i and cell_j == j:
                    continue
                count += self.matrix[i % self.columns][j % self.rows]
        return count

    def invert_cell(self, pos):
        cursor_x, cursor_y = pos
        i, j = self._find_cell_under_cursor(cursor_x, cursor_y)
        self.matrix[i][j] = not self.matrix[i][j]

    def _find_cell_under_cursor(self, cursor_x: int, cursor_y: int) -> Tuple[int, int]:
        return cursor_x // self.cell_size, cursor_y // self.cell_size
