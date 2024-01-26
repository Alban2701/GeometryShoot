from background import Background
import boutons


class MenuPrincipal(Background):
    """Pour une fenetre de 720px480p : Chaque secteur de bouton mesure 160p de hauteur.
    Pour aérer un peu, on met une marge de 10p entre le haut de l'écran et le haut du premier bouton.
    On fait pareil avec le bas de l'écran et le bas du dernier bouton.
    Pour ce qui est des côtés, l'espace entre les côtés des boutons et les bordures d'écrans seront de 20p
    Aussi, pour éviter que les boutons soient trop sérrés, il y a une marge de 20p entre chaque bouton.
    Donc : chaque bouton mesure 680p de largeur et 220p de hauteur"""
    def __init__(self):
        super().__init__()
        self.play_button = boutons.PlayBouton(20, 10, 680, 140)
        self.parametres_button = boutons.ParametreBouton(20, 170, 680, 140)
        self.quit_button = boutons.QuitBouton(20, 330, 680, 140)



