import pygame 
from peach import Peach

screen = pygame.display.set_mode((800, 600))
screen.fill((95, 60, 200))
running = True
clock = pygame.time.Clock()

peach = Peach()
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(peach.image, (peach.rect.x, peach.rect.y))
    pygame.display.update()
    clock.tick(60)




