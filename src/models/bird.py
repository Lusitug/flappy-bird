import pygame
import os

base_path = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(base_path, '../../imgs')

BIRD_IMAGES = [
    pygame.transform.scale2x(pygame.image.load(os.path.join(image_path,'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join(image_path,'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join(image_path,'bird3.png')))
]


class Bird:
    RATATION_MAX = 25
    RATATION_SPEED = 20
    ANIMATION_TIME = 5
    bird_imgs = BIRD_IMAGES
    
    def __init__(self, x, y) -> None:
        self.x = x #left=negativo right=positivo
        self.y = y #down=positivo up=negativo


        self.height = self.y
        self.angle = 0
        self.speed = 0
        self.time = 0

        self.image_count = 0
        self.image = self.bird_imgs[0]


    def jump(self):
        self.speed = -10.50
        self.time = 0
        self.height = self.y

    def move(self):
    #calcular deslocamento
        self.time += 1
        # S = so + vo.t + a.t²/2
        movement = (1.5 * (self.time**2)) + (self.speed*self.time) 
    
    #restringir deslocamento
        if movement > 16:
            movement = 16
        elif movement < 0:
            movement -= 2

        self.y += movement
        
    #amgulo
        if movement < 0 or self.y < (self.height + 50):
            if self.angle < self.RATATION_MAX:
                self.angle = self.RATATION_MAX
        else:
            if self.angle > -90:
                self.angle -= self.RATATION_SPEED

    def draw(self, screen_bird):
    #definir imagem atual do passaro
        self.image_count += 1

        if self.image_count < self.ANIMATION_TIME:
            self.image = self.bird_imgs[0]

        elif self.image_count < self.ANIMATION_TIME*2:
            self.image = self.bird_imgs[1]
            
        elif self.image_count < self.ANIMATION_TIME*3:
            self.image = self.bird_imgs[2]

        elif self.image_count < self.ANIMATION_TIME*4:
            self.image = self.bird_imgs[1]

        elif self.image_count >= self.ANIMATION_TIME*4+1:
            self.image = self.bird_imgs[0]
            self.image_count = 0
        
    #durante a queda não bate asas
        if self.angle <= -80:
            self.image = self.bird_imgs[1]
            self.image_count = self.ANIMATION_TIME*2
            
    #desenhar imagem
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        image_center_pos = self.image.get_rect(topleft=(self.x, self.y)).center
        rectangle = rotated_image.get_rect(cemter=image_center_pos) # desenha retangulo, joga na tela e dentro dele contem a imagem
        screen_bird.blit(rotated_image, rectangle.topleft)

    def get_mask(self):
        pygame.mask.from_surface(self.image)