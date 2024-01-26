# Création de la classe d'un carré
from math import sqrt

import pygame


class Square:

    def __init__(self):
        self.rect = pygame.Rect(0, 0, 20, 20)
        self.moving_to = [0.0, 0.0]
        self.color = (0, 81, 255)
        self.velocity = 4

    def update_square(self, surface):
        self.rect.move_ip(self.moving_to)
        pygame.draw.rect(surface, self.color, self.rect)

    def move_left(self, diagonale=False):
        if diagonale:
            self.moving_to[0] = self.velocity / sqrt(2) * -1
        else:
            self.moving_to[0] = self.velocity * -1
        # print("gauche")
        # self.print_position()

    def move_right(self, diagonale=False):
        if diagonale:
            self.moving_to[0] = self.velocity / sqrt(2)
        else:
            self.moving_to[0] = self.velocity
        # print("droite")
        # self.print_position()

    def move_up(self, diagonale=False):
        if diagonale:
            self.moving_to[1] = self.velocity / sqrt(2) * -1
        else:
            self.moving_to[1] = self.velocity * -1
        # print("haut")
        # self.print_position()

    def move_down(self, diagonale=False):
        if diagonale:
            self.moving_to[1] = self.velocity / sqrt(2)

        else:
            self.moving_to[1] = self.velocity
        # print("bas")
        # self.print_position()

    def get_position(self):
        print(self.rect)

    def square_init(self, surface):
        self.rect = pygame.draw.rect(surface, self.color, self.rect)

    def reset_moving(self):
        self.moving_to = [0.0, 0.0]
