import time
from random import random
from typing import Optional, Tuple, List

import pygame
from pygame.constants import *

from scenes.scene import Scene
from settings import START_DENSITY


def performance(method):
    def decorator(*args, **kwargs):
        start = time.perf_counter()
        result = method(*args, **kwargs)
        print(f'{method.__name__} - {(time.perf_counter() - start)}')
        return result

    return decorator


class LifeGame(Scene):
    def __init__(self, app):
        super().__init__(app)
        self.cell_size = 10
        self.cell_color = 'Red'
        pygame.display.set_caption('Life')
        self.app.background = (255, 255, 255)
        self.columns = self.width // self.cell_size
        self.rows = self.height // self.cell_size
        self.matrix = self._create_matrix()
        self._fill_matrix()
        self._draw_matrix()

    def update(self, event: Optional[pygame.event.Event] = None) -> None:
        self.app.screen.fill(self.app.background)
        self._draw_matrix()
        self._calculate_next_generation()
        if event is None:
            return
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 3:
                self._invert_cell(*event.pos)

    def _create_matrix(self) -> List[List[int]]:
        return [[0] * self.rows for _ in range(self.columns)]

    def _fill_matrix(self) -> None:
        for i, row in enumerate(self.matrix):
            for j, _ in enumerate(row):
                self.matrix[i][j] = random() > START_DENSITY

    def _draw_matrix(self):
        for i, row in enumerate(self.matrix):
            for j, _ in enumerate(row):
                if self.matrix[i][j]:
                    cell_center = (i * self.cell_size + self.cell_size // 2, j * self.cell_size + self.cell_size // 2)
                    pygame.draw.circle(self.app.screen, self.cell_color, cell_center, self.cell_size // 3)

    def _calculate_next_generation(self) -> None:
        next_gen_matrix = self._create_matrix()
        for i, row in enumerate(self.matrix):
            for j, _ in enumerate(row):
                next_gen_matrix[i][j] = self._dead_of_alive(self.matrix[i][j], self._get_neighbours_count(i, j))
        self.matrix = next_gen_matrix

    def _get_neighbours_count(self, cell_i: int, cell_j: int) -> int:
        count = 0
        for i in range(cell_i - 1, cell_i + 1 + 1):
            for j in range(cell_j - 1, cell_j + 1 + 1):
                if cell_i == i and cell_j == j:
                    continue
                count += self.matrix[i % self.columns][j % self.rows]
        return count

    def _invert_cell(self, cursor_x: int, cursor_y: int) -> None:
        i, j = self._find_cell_under_cursor(cursor_x, cursor_y)
        self.matrix[i][j] = not self.matrix[i][j]

    def _find_cell_under_cursor(self, cursor_x: int, cursor_y: int) -> Tuple[int, int]:
        return cursor_x // self.cell_size, cursor_y // self.cell_size

    @staticmethod
    def _dead_of_alive(cell_alive: bool, neighbours: int) -> bool:
        return neighbours in (2, 3) if cell_alive else neighbours == 3
