import math

import pygame


class Projectile:
    def __init__(self, direction, entity):
        """Construction d'une instance de projectile qui dépend de la direction (pour le joueur là où il clique,
        pour un ennemi, le joueur), et l'entité génératrice du projectile (le joueur ou l'ennemi)"""
        self.entity_center = entity.rect.center
        self.start_pos = self.entity_center
        self.width = 3  # pixels de largeur
        self.length = 10  # pixel de longueur
        self.velocity = 10  # Vitesse du projectile
        self.direction = direction
        self.opposite_direction = self.set_opposite_direction()
        self.end_pos = self.get_coord_arrivee(self.start_pos, self.length)
        self.color = entity.color
        self.damage = 5
        self.rect = None

    def __str__(self):
        return "color = {}, start_pos = {}, end_pos = {}".format(self.color, self.start_pos, self.end_pos)

    def get_c_dir(self):
        """Prend 2 couples de coordonnées en paramètre et calcule le coefficient directeur de la droite passant par
        ces deux points"""
        if self.direction[0] - self.start_pos[0] == 0:
            if self.direction[1] - self.start_pos[1] <= 0:
                return "up"
            else:
                return "down"
        return (self.direction[1] - self.start_pos[1]) / (self.direction[0] - self.start_pos[0])

    def get_coord_arrivee(self, start_pos, distance):
        """Permet de calculer des coordonnées d'arrivée en fonction d'un coéfficient directeur et des coordonnées
        de départ. Utile pour calculer le point d'arrivée du projectile lorsqu'on le dessine, ou alors pour calculer
        sa position après un déplacement"""
        # calcul de l'angle radian
        c_dir = self.get_c_dir()
        # print(c_dir)
        if c_dir == "down":  # Si l'entité doit monter parallèlement à l'axe des ordonnées
            x2 = start_pos[0]
            y2 = start_pos[1] + self.velocity
            return x2, y2
        elif c_dir == "up":  # Si l'entité doit descendre parallèlement à l'axe des ordonnées
            x2 = start_pos[0]
            y2 = start_pos[1] - self.velocity
            return x2, y2
        angle_radians = math.atan(c_dir)
        # calcul des variations horizontales et verticales
        delta_x = distance * math.cos(angle_radians)
        delta_y = distance * math.sin(angle_radians)
        if self.opposite_direction:  # Si on tire à gauche, le projectile va à gauche
            delta_x *= -1
            delta_y *= -1
        # Calcul des coordonnées d'arrivée (x2, y2)
        x2 = start_pos[0] + delta_x
        y2 = start_pos[1] + delta_y

        return x2, y2

    def move(self):
        """Calcule des coordonnées après un déplacement. ((x1, y1), (x2, y2)) forme le segment de départ et
        ((x3, y3), (x4, y4)) forme le segment après déplacement"""
        x3, y3 = self.get_coord_arrivee(self.start_pos, self.velocity)
        x4, y4 = self.get_coord_arrivee(self.end_pos, self.velocity)
        self.start_pos = x3, y3
        self.end_pos = x4, y4

    def update_line(self, surface):
        return pygame.draw.line(surface, self.color, self.start_pos, self.end_pos, width=self.width)

    def set_opposite_direction(self):
        """Cherche à savoir si l'entité tire à gauche d'elle-même ou à droite afin de déterminer correctement
        la variable "end_pos" qui, sans cette fonction, sera toujours à droite de l'entité tireuse"""
        return self.direction[0] < self.start_pos[0]
