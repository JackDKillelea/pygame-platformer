import pygame

class PhysicsEntity:
    def __init__(self, game, entity_type, position, size):
        self.game = game
        self.type = entity_type
        self.position = list(position)
        self.size = size
        self.velocity = [0,0]

    def update(self, movement=(0,0)):
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])

        self.position[0] += frame_movement[0] # Updating x position
        self.position[1] += frame_movement[1] # Updating y position

    def render(self, surf):
        surf.blit(self.game.assets["player"], self.position)
