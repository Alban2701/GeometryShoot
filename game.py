import pygame

import enemy
import projectile
from arena import Arena
from projectile import Projectile
from square import Square
from enemy import Enemy
from screen import Screen
from player import Player


# Créer une classe qui représente le jeu
class Game:
    def __init__(self):
        self.arena = Arena()  # mise en place de l'arrière-plan qui sera blanc avec des bordures noires
        self.player = Player(self.arena)  # générer le joueur
        self.enemies = []  # contient tous les ennemis qui seront créer
        self.pressed = {}  # Dictionnaire des touches sur lesquelles on appuie
        self.anti_rafale_pressed = {}  # gère les touches qui ne doivent pas être activées en rafale
        self.wall_collide_dic = {"LEFT": False, "UP": False, "RIGHT": False, "DOWN": False}
        # Ce dictionnaire varie ses valeurs en fonction des collisions de murs avec le joueur
        self.projectiles = []  # Liste qui va contenir tous les projectiles que le joueur va tirer
        self.player_is_shooting = False
        self.wave = 0  # le nombre de vague d'ennemis
        self.running = True  # Est-ce que le jeu est en cours d'execution
        self.in_pause = False  # Est-ce que le jeu est en pause

    #DEMARRAGE GRAPHIQUE DU JEU#
    def graph_init(self, surface: Screen):
        self.init_item(self.arena, surface)
        self.init_item(self.player, surface)
    def init_item(self, objet, surface):
        if isinstance(objet, Square):
            # print("here")
            objet.square_init(surface)

    #GESTION DES ACTIONS DU JOUEUR#
    def entity_move(self, entity):
        self.player.reset_moving()
        # Vérifier si le joueur souhaite se déplacer en diagonale
        if self.pressed.get(pygame.K_d) and self.pressed.get(pygame.K_z) and not (
                self.wall_collide_dic["RIGHT"] or self.wall_collide_dic["UP"]):
            entity.move_right(diagonale=True)
            entity.move_up(diagonale=True)
        elif self.pressed.get(pygame.K_q) and self.pressed.get(pygame.K_z) and not (
                self.wall_collide_dic["LEFT"] or self.wall_collide_dic["UP"]):
            entity.move_left(diagonale=True)
            entity.move_up(diagonale=True)
        elif self.pressed.get(pygame.K_d) and self.pressed.get(pygame.K_s) and not (
                self.wall_collide_dic["RIGHT"] or self.wall_collide_dic["DOWN"]):
            entity.move_right(diagonale=True)
            entity.move_down(diagonale=True)
        elif self.pressed.get(pygame.K_q) and self.pressed.get(pygame.K_s) and not (
                self.wall_collide_dic["LEFT"] or self.wall_collide_dic["DOWN"]):
            entity.move_left(diagonale=True)
            entity.move_down(diagonale=True)

        # Vérifier si le joueur souhaite se déplacer horizontalement ou verticalement

        elif self.pressed.get(pygame.K_d) and not self.wall_collide_dic["RIGHT"]:
            self.player.move_right()
        elif self.pressed.get(pygame.K_q) and not self.wall_collide_dic["LEFT"]:
            self.player.move_left()
        elif self.pressed.get(pygame.K_z) and not self.wall_collide_dic["UP"]:
            self.player.move_up()
        elif self.pressed.get(pygame.K_s) and not self.wall_collide_dic["DOWN"]:
            self.player.move_down()

    def check_player_wall_collide(self):
        """Vérifie si le joueur touche un mur et transforme le dictionnaire lié aux booléens en fonction des résultats """
        self.wall_collide_dic["LEFT"] = self.player.rect[0] <= self.arena.x_pos + self.arena.borders_thickness
        self.wall_collide_dic["RIGHT"] = self.player.rect[0] + self.player.rect[
            2] >= self.arena.width - self.arena.borders_thickness
        self.wall_collide_dic["UP"] = self.player.rect[1] <= self.arena.y_pos + self.arena.borders_thickness
        self.wall_collide_dic["DOWN"] = self.player.rect[1] + self.player.rect[
            3] >= self.arena.height - self.arena.borders_thickness

    def player_shooting(self, rafale=False, direction=None):
        if direction == "up":
            if self.anti_rafale(pygame.MOUSEBUTTONDOWN):
                projectile = (Projectile((self.player.rect.center[0], self.player.rect.center[1] - 1), self.player))
                self.projectiles.append(projectile)
                # print(projectile)

        elif direction == "down":
            if self.anti_rafale(pygame.MOUSEBUTTONDOWN):
                projectile = (Projectile((self.player.rect.center[0], self.player.rect.center[1] + 1), self.player))
                self.projectiles.append(projectile)


        if rafale:
            if self.pressed.get(pygame.MOUSEBUTTONDOWN):
                x, y = pygame.mouse.get_pos()
                self.projectiles.append(Projectile((x, y), self.player))

        else :
            if self.anti_rafale(pygame.MOUSEBUTTONDOWN):
                x, y = pygame.mouse.get_pos()
                projectile = (Projectile((x, y), self.player))
                self.projectiles.append(projectile)
                # print(projectile)

    def anti_rafale(self, key):
        """La boucle du jeu est tellement rapide que cette fonction permet de faire en sorte qu'un évènement n'arrive
        qu'une fois par pression de bouton"""
        if self.pressed.get(key):
            self.anti_rafale_pressed[key] = True
        elif self.anti_rafale_pressed.get(key):
            x, y = pygame.mouse.get_pos()
            self.anti_rafale_pressed[key] = False
            return True

    #GESTIONS DES ACTIONS NON JOUEURS
    def remove_proj_out_of_arena(self, projectile, arena):
        """teste si le projectile se trouve encore dans l'arène.
        Si le projectile n'est plus partiellement, alors la ligne qui le dessine est raccouris
        Si il n'y est plus, il est détruit"""
        collide = arena.rect.contains(projectile.rect)
        if not collide:
            self.projectiles.remove(projectile)

    def create_ennemie(self, surface: Screen, manual_mode=False):
        if manual_mode:
            if self.anti_rafale(pygame.K_e) and manual_mode:
                ennemi = Enemy(surface, self.player)
                self.enemies.append(ennemi)
        else:
            for n in range(self.wave):
                ennemi = Enemy(surface, self.player)
                self.enemies.append((ennemi))


    def display_some_things(self):
        print("player's health", self.player.health)

    def check_proj_hit_enemy(self):
        for projectile in self.projectiles:
            for enemy in self.enemies:
                clipped_line = enemy.rect.clipline(projectile.start_pos, projectile.end_pos)
                if clipped_line:
                    enemy.health -= projectile.damage
                    projectile.damage = 0
                    if projectile in self.projectiles:
                        self.projectiles.remove((projectile))
                    # projectile.start_pos, projectile.end_pos = clipped_line
                if enemy.health == 0:
                    self.enemies.remove(enemy)
                    # self.projectiles.remove(projectile)

    def wave_managing(self):
        if len(self.enemies) == 0:
            self.wave += 1
            return True

    def check_enemy_hurt_player(self):
        for enemy in self.enemies:
            if self.player.rect.colliderect(enemy.rect):
                self.player.health -= enemy.damage
                self.enemies.remove(enemy)

    def pausing_the_game(self):
        touche_echap = self.anti_rafale((pygame.K_ESCAPE))
        if touche_echap and self.in_pause:
            self.in_pause = False
            print(self.in_pause)
        elif touche_echap and not self.in_pause:
            self.in_pause = True
            print(self.in_pause)

        return self.in_pause


    def check_event(self):
        for event in pygame.event.get():
            # Si le joueur ferme la fenêtre
            if event.type == pygame.QUIT:
                self.in_pause = False
                self.running = False


            # détecter si le joueur appuie sur une touche du clavier
            if event.type == pygame.KEYDOWN:
                self.pressed[event.key] = True
            elif event.type == pygame.KEYUP:
                self.pressed[event.key] = False

            # détecter si le joueur tire
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.pressed[pygame.MOUSEBUTTONDOWN] = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.pressed[pygame.MOUSEBUTTONDOWN] = False



