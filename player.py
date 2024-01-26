import arena
from square import Square


class Player(Square):
    def __init__(self, arene: arena.Arena):
        super().__init__()
        self.rect = (arene.rect.center[0], arene.rect.center[1], 20, 20)
        self.max_health = 100
        self.health = self.max_health

    def is_dead(self):
        return self.health <= 0


