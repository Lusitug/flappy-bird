import random
import pygame
import os

base_path = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(base_path, '../../imgs')

from models.bird import Bird

PIPE_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join(image_path,'pipe.png')))

class Pipe:
    DISTANCE = 200
    SPEED = 5 
    pipe_image = PIPE_IMAGE

    def __init__(self, x) -> None:
        self.x = x
        
        self.height = 0
        self.top_pos = 0
        self.base_pos = 0

        self.top_pipe_image = pygame.transform.flip(self.pipe_image, False, True)
        self.base_pipe_image = self.pipe_image
        self.passed = False

        self.set_height()

    def set_height(self):
        self.height = random.randrange(50, 450)
        self.top_pos  =  self.height - self.top_pipe_image.get_height() 
        self.base_pos =  self.height + self.DISTANCE

    def move(self):
        self.x -= self.SPEED 

    def draw(self, screen_pipe):
        screen_pipe.blit(self.top_pipe_image, (self.x, self.top_pos))
        screen_pipe.blit(self.base_pipe_image, (self.x, self.base_pos))

    def collide(self, bird: Bird):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.top_pipe_image)
        base_mask = pygame.mask.from_surface(self.base_pipe_image)

        top_DISTANCE = (self.x - bird.x, self.top_pos - bird.y)
        base_DISTANCE = (self.x - bird.x, self.base_pos - bird.y)

        top_point = bird_mask.overleap(top_mask, top_DISTANCE)
        base_point = bird_mask.overleap(base_mask, base_DISTANCE)

        if base_point or top_point:
            return True
        else:
            return False