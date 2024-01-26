import pygame

from background import Background


class Arena(Background):
    def __init__(self):
        super().__init__()
        self.borders_coord = [(0, 0), (0, self.height - 1), (self.width - 1, self.height - 1), (self.width - 1, 0)]
        # self.borders est une liste de tuple correspondant chacun à deux sommets d'un segment formant
        # une bordure de l'arène
        self.borders_color = "black"  # Les couleurs de bordures en noir
        self.closed = True  # Est-ce que l'arène est fermée
        self.borders_thickness = 1

    def draw_borders(self, surface):
        return pygame.draw.lines(surface, self.borders_color, self.closed, self.borders_coord,
                                 self.borders_thickness)


if __name__ == "__main__":
    from screen import Screen

    # générer une fenêtre de jeu
    main_screen = Screen()
    background = main_screen.set_display()  # on allume la fenêtre
    main_screen.set_caption()  # on met le titre de la fenêtre

    # mise en place de l'arrière-plan qui sera blanc avec des bordures noires
    arena = Arena()
    # Création d'une variable "running" qui dit si le jeu tourne ou pas

    running = True

    # Création de la boucle de jeu

    # print(main_screen.size)
    while running:
        # appliquer l'arrière-plan de notre jeu
        arena.update_square(background)
        # On affiche les bordures après le joueur, ainsi, le joueur n'aura pas l'air d'être 'au-dessus' des bordures
        rect_arena = arena.draw_borders(background)
        for event in pygame.event.get():
            # Si le joueur ferme la fenêtre
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                print("le jeu est terminé")
                # print(rect_arena)
