# la classe qui gère l'arrière-plan
import pygame

from square import Square


class Background(Square):

    def __init__(self):
        super().__init__()
        self.x_pos = 0
        self.y_pos = 0
        self.width, self.height = pygame.display.get_window_size()
        self.color = (255, 255, 255)  # blanc en RGB
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
