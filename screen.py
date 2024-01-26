import pygame


class Screen(pygame.surface.Surface):
    def __init__(self):
        self.size = (720, 480)  # Taille de la fenêtre
        super().__init__(self.size)
        self.title = "Geometry Shoot"  # Tite de la fenêtre
        self.display = None  # Variable qui va accueillir l'instance de la fenêtre afin de la manipuler
        self.caption = None  # Variable qui contient le titre de la fenêtre

    def set_caption(self):  # Définir le titre de la fenêtre
        pygame.display.set_caption(self.title)

    def set_display(self):  # Afficher la fenêtre avec les dimensions souhaitées
        self.display = pygame.display.set_mode(self.size)
        return self.display
