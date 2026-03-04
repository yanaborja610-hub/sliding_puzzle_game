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
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def events(self):
        pass


game = Game()
while True:
    game.new()
    game.run()
