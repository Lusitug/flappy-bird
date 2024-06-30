from typing import List
import pygame
import random
import os
from models.bird import Bird
from models.pipe import Pipe
from models.floor import Floor

pygame.init()
pygame.font.init()

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, '..', 'imgs')

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 800

BG_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join(image_path,'bg.png')))

POINTS_FONT = pygame.font.SysFont('arial', 50)

def draw_screen(screen, birds: List[Bird], pipes: List[Pipe], floor: Floor, points):
    screen.blit(BG_IMAGE, (0, 0))
    for bird in birds:
        bird.draw(screen_bird=screen)

    for pipe in pipes:
        pipe.draw(screen_pipe=screen)
    
    text = POINTS_FONT.render(f"[Score: {points}]",
                               1, (255,255,255))
                              
    screen.blit(text, (WINDOW_WIDTH - 10 - text.get_width(), 10 ))

    floor.draw(screen_floor=screen)
    
    pygame.display.update()


