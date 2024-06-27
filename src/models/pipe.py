import random
import pygame

from models.bird import Bird


class Pipe:
    def __init__(self, x, pipe_image) -> None:
        self.pipe_image = pipe_image
        self.distance = 200
        self.speed = 5 
        
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
        self.base_pos =  self.height + self.distance

    def move(self):
        self.x -= self.speed 

    def draw(self, screen):
        screen.bit(self.top_pipe_image, (self.x, self.top_pos))
        screen.bit(self.base_pipe_image, (self.x, self.base_pos))

    def collide(self, bird: Bird):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.top_pipe_image)
        base_mask = pygame.mask.from_surface(self.base_pipe_image)

        top_distance = (self.x - bird.x, self.top_pos - bird.y)
        base_distance = (self.x - bird.x, self.base_pos - bird.y)

        top_point = bird_mask.overleap(top_mask, top_distance)
        base_point = bird_mask.overleap(base_mask, base_distance)

        if base_point or top_point:
            return True
        else:
            return False