import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Platform Game")
        self.clock = pygame.time.Clock()
        self.running = True

        self.img = pygame.image.load("data/images/entities/player.png")
        self.img.set_colorkey((0, 0, 0))  # Set the transparent color to black
        self.img_pos = [160, 260]
        self.movement = [False, False]

        self.collision_area = pygame.Rect(50, 50, 300, 50)

    def run(self):
        while True:
            self.screen.fill((14, 219, 248))  # Set the background color to "sky" colour

            img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())
            if img_r.colliderect(self.collision_area):
                pygame.draw.rect(self.screen, (0, 100, 255), self.collision_area)
            else:
                pygame.draw.rect(self.screen, (0, 50, 255), self.collision_area)

            self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5
            self.screen.blit(self.img, self.img_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.movement[0] = True
                    elif event.key == pygame.K_s:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.movement[0] = False
                    elif event.key == pygame.K_s:
                        self.movement[1] = False

            pygame.display.update()
            self.clock.tick(60)  # Set the frame rate to 60

Game().run()