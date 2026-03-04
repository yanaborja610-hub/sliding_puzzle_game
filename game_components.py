import pygame
from game_settings import *

pygame.font.init()


class Tile(pygame.sprite.Sprite):
    def __init__(self, game, x, y, text):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((tile_size, tile_size))
        self.x = x
        self.y = y
        self.text = text
        self.rect = self.image.get_rect()
        if self.text != "empty":
            self.font = pygame.font.Sysfont("Consolas", 50)
            font_surface = self.font.render(self.text, True, black)
            self.image.fill(white)
            self.font_size = self.font.size(self.text)
            self.image.blit(font_surface, (self.x, self.y))

    def update(self):
        self.rect.x = self.x * tile_size
        self.rect.y = self.y * tile_size

    def click(self,mouse_x, mouse_y):
        return self.rect.left <= mouse_x <= self.rect.right and self.rect.top <= mouse_y <= self.rect.bottom
