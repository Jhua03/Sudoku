import pygame
from Sudoku import solve, isValid
from sys import exit

import time

pygame.font.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Sudoku")
clock =pygame.time.Clock()
text_font = pygame.font.Font('Images/Font.otf', 50)

sky_surface = pygame.image.load('Images/background.jpg')
sky_surface = pygame.transform.scale(sky_surface,(800,400))
text_surface = text_font.render('My game',False,'Red')
hero_surface = pygame.image.load('Images/hero.png')
hero_surface = pygame.transform.scale(hero_surface,(100,100))
hero_x_pos = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    

    screen.blit(sky_surface,(0,0))
    screen.blit(text_surface,(300,100))
    screen.blit(hero_surface,(hero_x_pos,300))
    hero_x_pos += 1
    pygame.display.update()
    clock.tick(60)

    

