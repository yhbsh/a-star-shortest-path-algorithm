from turtle import left
import pygame
from constants import *


class Node:
    def __init__(self, row, col, size, total_rows):
        self.row = row
        self.col = col
        self.x = row * size
        self.y = col * size
        self.color = WHITE
        self.neighbors = []
        self.size = size
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUOISE

    def reset(self):
        self.color = WHITE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_start(self):
        self.color = ORANGE

    def make_end(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.size, self.size))

    def update_neighbors(self, grid):
        self.neighbors = []
        top_neighbor = grid[self.row-1][self.col].is_barrier()
        down_neighbor = grid[self.row+1][self.col].is_barrier()
        right_neighbor = grid[self.row][self.col+1].is_barrier()
        left_neighbor = grid[self.row][self.col-1].is_barrier()
        if self.row > 0 and not top_neighbor.is_barrier():
            self.neighbors.append(top_neighbor)

        if self.row - 1 < self.total_rows and not down_neighbor.is_barrier():
            self.neighbors.append(down_neighbor)

        if self.col > 0 and not left_neighbor.is_barrier():
            self.neighbors.append(left_neighbor)
        
        if self.col - 1 < self.total_rows and not right_neighbor.is_barrier():
            self.neighbors.append(right_neighbor)


        # Used to compare current node with "other node"
        # we always say that other node is greater than current node.

    def __lt__(self, other):
        return False
