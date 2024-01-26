import pygame
from game import Game
from screen import Screen

# pygame setup
pygame.init()  # on initialise le module
# générer une fenêtre de jeu
main_screen = Screen()
fenetre = main_screen.set_display()  # on allume la fenêtre
main_screen.set_caption()  # on met le titre de la fenêtre
# Définir une clock
clock = pygame.time.Clock()
FPS = 60

# Charger notre jeu
game = Game()
game.graph_init(fenetre)
# Création d'une variable "running" qui dit si le jeu tourne ou pas

# Création de la boucle de jeu

while game.running:  # Boucle dans laquelle le jeu tourne
    while game.in_pause:  # Boucle dans laquelle le jeu tourne encore, mais est en pause
        game.check_event()  # Vérifier les évènements des périphériques d'entrée
        game.pausing_the_game()  # vérifier si on doit sortir du mode pause

    game.pausing_the_game()  # vérifier si on doit mettre en pause le jeu

    # appliquer l'arrière-plan de notre jeu
    game.arena.update_square(fenetre)

    # On affiche le joueur
    game.player.update_square(fenetre)

    #  Boucle de gestion des projectiles
    for projectile in game.projectiles:  # Pour chaque projectile du jeu
        projectile.move()  # On le fait se déplacer
        projectile.rect = projectile.update_line(fenetre)  # On trace le nouveau tracé avec les nouvelles coordonnées
        game.remove_proj_out_of_arena(projectile, game.arena)  # So le projectile sort de l'arène, on le supprime

    # Boucle de gestions des ennemis
    for ennemi in game.enemies:  # Pour chaque ennemi en jeu
        ennemi.get_target(game.player.rect.center)  # On actualise la cible qui est le centre du joueur
        ennemi.move()  # On fait bouger l'ennemi vers le centre du joueur
        ennemi.update_square(fenetre)  # On affiche l'ennemi après son déplacement
        if ennemi.is_dead():  # Si l'ennemi n'a plus de santé
            game.enemies.remove()  # On retire l'ennemi du jeu

    # On affiche les bordures après le joueur, ainsi, le joueur n'aura pas l'air d'être 'au-dessus' des bordures
    game.arena.rect = game.arena.draw_borders(fenetre)

    # Déplacement joueur
    game.check_player_wall_collide()  # Vérifier si le joueur touche les bords de l'arène
    game.entity_move(game.player)  # Faire bouger le joueur
    game.player_shooting()  # Gestion du tir du joueur

    # Gestion de vague d'ennemi : s'il n'y a plus d'ennemis, on lance la manche suivante
    if game.wave_managing():
        # Création d'ennemi
        game.create_ennemie(game.arena)

    game.check_proj_hit_enemy()  # Vérifier si les projectiles ont atteint une cible
    game.check_enemy_hurt_player()  # Vérifier si un ennemi touche le joueur
    if game.player.is_dead():  # Si le joueur n'a plus de santé
        game.running = False  # Le jeu se termine

    pygame.display.flip()  # Mise à jour de l'écran
    game.check_event()  # On vérifie les évènements de périphérique d'entrée
    # game.display_some_things()  # Afficher quelques informations utiles au débogage

    clock.tick(FPS)  # Fixer le nombre de FPS sur ma clock


pygame.quit()  # Une fois sorti de la boucle du jeu, on quitte la fenetre
print("le jeu est terminé")  # Todo faire un écran de fin de jeu, plus sympa qu'un simple print
print("Vous avez perdu à la manche {}".format(game.wave))  # Todo faire apparaitre le nombre de manches sur la fenetre du jeu en temps réel

# Todo animation de mort pour moi et les ennemis (explosion de pixels)
# Todo inventer plusieurs types d'ennemis
# Todo faire un tir secondaire
# Todo faire un écran d'accueil pour lancer le jeu
