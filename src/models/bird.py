class Bird:
    def __init__(self, bird_imgs, x, y) -> None:
        self.bird_imgs = bird_imgs
        self.x = x #left=negativo right=positivo
        self.y = y #down=positivo up=negativo

        self.rotation_max =25
        self.rotation_speed = 20
        self.animation_time = 5
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
            if self.angle < self.rotation_max:
                self.angle = self.rotation_max
        else:
            if self.angle > -90:
                self.angle -= self.rotation_speed