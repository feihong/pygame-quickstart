"""
Click to add more vertices. Press SPACE to draw the polygon using the latest points.
"""
import itertools
import pygame
import pg

pg.set_caption('Polygons')
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

def draw():
    for color_name, polygon in zip(itertools.cycle(color_names), polygons):
        pygame.draw.polygon(screen, color_name, polygon)

    if len(coords) > 0:
        point1 = coords[-1]
        point2 = pygame.mouse.get_pos()
        pygame.draw.line(screen, 'white', point1, point2)

if __name__ == '__main__':
    pg.run(draw, on_event)
