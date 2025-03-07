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
coords = []
polygons = []


def on_event(event):
    global coords, colors

    if event.type == pygame.MOUSEBUTTONDOWN:
        coords.append(pygame.mouse.get_pos())
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        if len(coords) >= 3:
            polygons.append(coords[:])
            coords = []

def loop():
    for color_name, polygon in zip(itertools.cycle(color_names), polygons):
        pygame.draw.polygon(screen, color_name, polygon)

    if len(coords) > 0:
        point1 = coords[-1]
        point2 = pygame.mouse.get_pos()
        pygame.draw.line(screen, 'white', point1, point2)

pg.run('Polygons', loop, on_event)
