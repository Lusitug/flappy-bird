import pygame
import random
import os
from models import bird, floor, pipe

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 800

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, '..', 'imgs')

FLOOR_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join(image_path,'base.png')))
PIPE_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join(image_path,'pipe.png')))
BG_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join(image_path,'bg.png')))
BIRD_IMAGES = [
    pygame.transform.scale2x(pygame.image.load(os.path.join(image_path,'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join(image_path,'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join(image_path,'bird3.png')))
]

pygame.font.init()
POINTS_FONT = pygame.font.SysFont('arial', 50)

bird = bird.Bird(bird_imgs=BIRD_IMAGES, x=1, y= 2)

print(bird.time)
