import pygame

BASE_IMAGE_PATH = "data/images/"

def load_image(path):
    img = pygame.image.load(f"{BASE_IMAGE_PATH}/{path}").convert()
    img.set_colorkey((0, 0, 0))  # Set the transparent color to black
    return img