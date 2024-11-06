import pygame
import sys

from utils import load_image
from scripts.entities import PhysicsEntity

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Platform Game")
        self.clock = pygame.time.Clock()

        self.movement = [False, False]
        self.assets = {
            "player": load_image("entities/player.png")
        }
        self.player = PhysicsEntity(self, "player", (50, 50), (8, 15))

    def run(self):
        while True:
            self.screen.fill((14, 219, 248))  # Set the background color to "sky" colour

            self.player.update((self.movement[1] - self.movement[0], 0))
            self.player.render(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                    elif event.key == pygame.K_d:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    elif event.key == pygame.K_d:
                        self.movement[1] = False

            pygame.display.update()
            self.clock.tick(60)  # Set the frame rate to 60

Game().run()