import pygame
import random
import os

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 800

FLOOR_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','base.png')))
PIPE_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','pipe.png')))
BG_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bg.png')))
BIRD_IMAGES = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bird3.png')))
]

