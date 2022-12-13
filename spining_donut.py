import pygame
import os

WHITE = (255,255,255)
BLACK = (0,0,0)

RESOLUTION = W_HEIGHT,W_WIDTH = 300,300
FPS = 60

pygame.init()

window = pygame.display.set_mode(RESOLUTION)
clock = pygame.time.Clock()
pygame.display.set_caption("Spinning donut by ZiM0u")

screen_size = W_HEIGHT*W_WIDTH

continuer= 1
while continuer:
    clock.tick(FPS)
    window.fill(BLACK)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                continuer = 0
            
            
    
pygame.quit()
