import pygame


class Bouton:
    """Un rect qui, lorsqu'on clique dessus, engage une action"""

    def __init__(self, x, y, width, height, color="orange", font_color="white"):
        self.pos = x, y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.font_color = font_color

    def bouton_clique(self, mouse_pos: tuple):
        """Prend en paramètre un tuple -- à savoir les coordonnées de la souris lors du click --
        et renvoie True si le click a été fait dans le rectangle"""
        is_clicked = self.rect.collidepoint(mouse_pos)
        return self.fonction()

    @staticmethod
    def fonction():  # ne fait rien, car bouton vide, mais les sous-classes ont des fonctions définies
        return


class QuitBouton(Bouton):
    """Bouton dont la fonction est de quitter le jeu
    Se trouve dans le menu principal"""

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.name = "Quitter"

    @staticmethod
    def fonction():  # Quitter le jeu → fermer le programme
        return pygame.QUIT


class PlayBouton(Bouton):
    """Bouton qui permet de commencer une nouvelle partie.
    Se trouve dans le menu principal"""

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.name = "Jouer"

    @staticmethod
    def fonction():  # Commencer une nouvelle partie
        return "play"


class ParametreBouton(Bouton):
    """Ouvre les paramètres.
    Se trouve dans le menu principal et dans le menu pause"""

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.name = "Paramètres"

    @staticmethod
    def fonction():  # Ouvrir les paramètres
        return "parametres"


class MenuPrincipalBouton(Bouton):
    """Ouvre le menu principal.
    Se trouve dans le menu pause"""

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.name = "Menu Principal"

    @staticmethod
    def fonction():
        return "menu principal"


class ReprendreBouton(Bouton):
    """Reprend le jeu.
    Se trouve dans le menu pause."""

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.name = "Reprendre"

    @staticmethod
    def fonction():
        return "reprendre le jeu"
