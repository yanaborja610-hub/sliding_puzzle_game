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
            self.font = pygame.font.SysFont("Consolas", 50)
            font_surface = self.font.render(self.text, True, black)
            self.image.fill(white)
            self.font_size = self.font.size(self.text)
            draw_x = (tile_size / 2) - self.font_size[0] / 2
            draw_y = (tile_size / 2) - self.font_size[1] / 2
            self.image.blit(font_surface, (draw_x, draw_y))
        else:
            self.image.fill(background_color)

    def update(self):
        self.rect.x = self.x * tile_size
        self.rect.y = self.y * tile_size

    def click(self,mouse_x, mouse_y):
        return self.rect.left <= mouse_x <= self.rect.right and self.rect.top <= mouse_y <= self.rect.bottom

    def right(self):
        return self.rect.x + tile_size < game_size * tile_size

    def left(self):
        return self.rect.x - tile_size >= 0

    def up(self):
        return self.rect.y - tile_size >= 0

    def down(self):
        return self.rect.y + tile_size < game_size * tile_size

class ui_element:
    def __init__(self, x, y, text):
        self.x, self.y = x, y
        self.text = text

    def draw(self, screen):
        font = pygame.font.SysFont("Consolas", 50)
        text = font.render(self.text, True, white)
        screen.blit(text, (self.x, self.y))

class button:
    def __init__(self, x, y, button_width, button_height, text, button_colour, text_colour):
        self.x, self.y = x, y
        self.button_width = button_width
        self.button_height = button_height
        self.text = text
        self.colour, self.text_colour = button_colour, text_colour

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour,
                         (self.x, self.y, self.button_width, self.button_height))
        font = pygame.font.SysFont("Consolas", 30)
        text = font.render(self.text, True, self.text_colour)
        self.font_size = font.size(self.text)
        draw_x = self.x + (self.button_width / 2) - self.font_size[0] / 2
        draw_y = self.y + (self.button_height / 2) - self.font_size[1] / 2
        screen.blit(text, (draw_x, draw_y))

    def click(self, mouse_x, mouse_y):
        return self.x <= mouse_x <= self.x + self.button_width and self.y <= mouse_y <= self.y + self.button_height