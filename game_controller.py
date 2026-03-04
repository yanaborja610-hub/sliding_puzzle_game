import pygame
import random
import time
from game_components import*
from game_settings import*

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()

    def new(self):
        pass

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(fps)
            self.events()
            self.update()
            self.draw()

    def update(self):
        pass

    def draw_grid(self):
        for row in range(-1, game_size * tile_size, tile_size):
            pygame.draw.line(self.screen, light_grey, (row, 0), (row, game_size * tile_size))
        for col in range(-1, game_size * tile_size, tile_size):
            pygame.draw.line(self.screen, light_grey, (0, col), (game_size * tile_size, col))

    def draw(self):
        self.screen.fill(background_color)
        self.draw_grid()
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)



game = Game()
while True:
    game.new()
    game.run()
