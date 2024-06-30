import os

import pygame

base_path = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(base_path, '../../imgs')

FLOOR_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join(image_path,'base.png')))

class Floor:
    SPEED = 0
    floor_image = FLOOR_IMAGE        
    
    def __init__(self, y) -> None:
        self.WIDTH = self.floor_image.get_width()

        self.y = y
        self.x_1 = 0
        self.x_2 = self.WIDTH

    def move(self):
        self.x_1 -= self.SPEED
        self.x_2 -= self.SPEED

        if self.x_1 + self.WIDTH < 0:
            self.x_1 = self.x_1+self.WIDTH

        if self.x_2 + self.WIDTH < 0:
            self.x_2 = self.x_2+self.WIDTH
        
    def draw(self, screen_floor):
        screen_floor.blit(self.floor_image, (self.x_1, self.y))
        screen_floor.blit(self.floor_image, (self.x_2, self.y))