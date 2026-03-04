import pygame
import random
import time

from pygame.examples import grid

from game_components import*
from game_settings import*

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()

    def create_game(self):
        grid = [[x + y * game_size for x in range(1, game_size + 1)] for y in range(game_size)]
        grid[-1][-1] = 0
        print(grid)

    def new(self):
        self.create_game()

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
