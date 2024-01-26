import pygame

from square import Square
from random import randint
import math


class Enemy(Square):
    """Un ennemi classique apparait sur les bordures de l'écran vers l'extérieur comme s'ils envahissaient la zone
    du joueur. Son comportement est équivalent à celui d'un zombie. Il est un peu plus lent et se dirige toujours vers
    le joueur. Il possède peu de point de vie et ne tire aucun projectile, infligeant donc des dégâts au contact du
    joueur"""

    def __init__(self, surface, target):
        super().__init__()
        self.width = 20
        self.height = 20
        self.generate_coord(surface)
        self.color = "red"
        self.max_health = 10
        self.health = self.max_health
        self.damage = 10
        self.velocity = 2.5
        self.target = target.rect.center
        self.moving_to = [0, 0]

    def generate_coord(self, surface):
        """Attribue des coordonnées aléatoires au niveau des bordures de l'écran"""

        # On détermine si l'ennemi apparait au niveau des largeurs ou des longueurs
        chosen_side = randint(1, 4)
        if chosen_side == 1:  # L'ennemi apparait sur la longueur en haut
            coord = randint(0, surface.width)
            self.rect = pygame.Rect(coord, self.height * -1, self.width, self.height)
        elif chosen_side == 2:  # l'ennemi apparait sur la largeur à droite
            coord = randint(0, surface.height)
            self.rect = pygame.Rect(surface.width, coord, self.width, self.height)
        elif chosen_side == 3:  # l'ennemi apparait sur la longueur en bas
            coord = randint(0, surface.width)
            self.rect = pygame.Rect(coord, surface.height, self.width, self.height)
        elif chosen_side == 4:  # l'ennemi apparait sur la largeur à gauche
            coord = randint(0, surface.height)
            self.rect = pygame.Rect(self.width * -1, coord, self.width, self.height)

    def is_dead(self):
        return self.health <= 0

    def get_direction(self):
        """Permet de calculer des coordonnées d'arrivée en fonction d'un coéfficient directeur et des coordonnées
            de départ. Utile pour calculer le point d'arrivée du projectile lorsqu'on le dessine, ou alors pour calculer
            sa position après un déplacement"""
        # calcul de l'angle radian
        c_dir = self.get_c_dir()
        if c_dir == "up":  # Si l'entité doit monter parallèlement à l'axe des ordonnées
            x2 = 0
            y2 = self.velocity
            return x2, y2
        elif c_dir == "down":  # Si l'entité doit descendre parallèlement à l'axe des ordonnées
            x2 = 0
            y2 = self.velocity * -1
            return x2, y2
        angle_radians = math.atan(c_dir)
        # calcul des variations horizontales et verticales
        delta_x = self.velocity * math.cos(angle_radians)
        delta_y = self.velocity * math.sin(angle_radians)
        if self.opposite_direction():  # Si la cible est à gauche, l'entité va à gauche
            delta_x *= -1
            delta_y *= -1
        # Calcul des coordonnées d'arrivée (x2, y2)
        x2 = self.moving_to[0] + delta_x
        y2 = self.moving_to[1] + delta_y
        return x2, y2

    def get_c_dir(self):
        """Prend 2 couples de coordonnées en paramètre et calcule le coefficient directeur de la droite passant par
        ces deux points"""
        if self.target[0] - self.rect.center[0] != 0:
            return (self.target[1] - self.rect.center[1]) / (self.target[0] - self.rect.center[0])
        else:
            if self.target[1] - self.rect.center[1] <= 0:  # Si l'entité doit descendre
                return "down"
            else:
                return "up"


    def opposite_direction(self):
        return self.target[0] < self.rect.center[0]

    def move(self):
        """Rect.move(x, y) renvoie un nouveau rectangle tandis que rect.move_ip(x, y) modifie le rectangle appelant la
        fonction. Ici, il est plus utile d'utiliser la fonction Rect.move_ip(x, y)"""
        direction = self.get_direction()
        self.rect.move_ip(direction)

    def get_target(self, target: tuple):
        self.target = target






