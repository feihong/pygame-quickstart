"""
Every line is connected to the previous line. Line colors cycle through the colors of the rainbow.
"""
import random
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
    global coords, colors

    if event.type == pygame.MOUSEBUTTONDOWN:
        coords.append(pygame.mouse.get_pos())
        print(coords)
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        coords = [(width // 2, height // 2)]
        colors = []


def loop():
    screen.fill('black')

    for color_name, (point1, point2) in zip(itertools.cycle(color_names), itertools.pairwise(coords)):
        pygame.draw.line(screen, color_name, point1, point2)

    point1 = coords[-1]
    point2 = pygame.mouse.get_pos()
    pygame.draw.line(screen, 'white', point1, point2)

pg.run('Pygame Lines', loop, on_event)
