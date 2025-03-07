"""
Every line is connected to the previous line. Line colors cycle through the colors of the rainbow.
"""
import itertools
import pygame
import pg
from reloading import reloading

width = 1000
height = 800
screen = pg.get_screen(width, height)

color_names = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
coords = [(width // 2, height // 2)]

def on_event(event):
    global coords, colors, width

    if event.type == pygame.MOUSEBUTTONDOWN:
        coords.append(pygame.mouse.get_pos())
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        coords = [(width // 2, height // 2)]
        screen.fill('black')

def loop():
    for width, color_name, (point1, point2) in zip(
        itertools.count(3), itertools.cycle(color_names), itertools.pairwise(coords)):
        pygame.draw.line(screen, color_name, point1, point2, width)

    point1 = coords[-1]
    point2 = pygame.mouse.get_pos()
    pygame.draw.line(screen, 'white', point1, point2)

pg.run('Pygame Lines', loop, on_event)
