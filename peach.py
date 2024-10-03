import pygame 

class Peach(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pictures/peach.png").convert_alpha()
        self.rect = self.image.get_rect() 




        
