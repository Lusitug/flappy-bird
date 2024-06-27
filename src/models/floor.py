class Floor:
    def __init__(self, floor_image, y) -> None:
        self.floor_image = floor_image        
        self.speed = 0
        self.width = floor_image.get_width()

        self.y = y
        self.x_1 = 0
        self.x_2 = self.width

    def move(self):
        self.x_1 -= self.speed
        self.x_2 -= self.speed

        if self.x_1 + self.width < 0:
            self.x_1 = self.x_1+self.width

        if self.x_2 + self.width < 0:
            self.x_2 = self.x_2+self.width
        
    def draw(self, screen):
        screen.blit(self.floor_image, (self.x_1, self.y))
        screen.blit(self.floor_image, (self.x_2, self.y))