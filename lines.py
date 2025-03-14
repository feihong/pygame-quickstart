"""
Every line is connected to the previous line. Line colors cycle through the colors of the rainbow.
"""
import itertools
import pygame
import pg

pg.set_caption('Lines')
width = 1000
height = 800
screen = pg.get_screen(width, height)

get_initial_coords = lambda: [(width // 2, height // 2)]
color_names = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
coords = get_initial_coords()
screen.fill('black')

def on_event(event):
    global coords, colors

    if event.type == pygame.MOUSEBUTTONDOWN:
        coords.append(pygame.mouse.get_pos())
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_r:
            coords = get_initial_coords()
        screen.fill('black')

def draw():
    for width, color_name, (point1, point2) in zip(
        itertools.count(3), itertools.cycle(color_names), itertools.pairwise(coords)):
        pygame.draw.line(screen, color_name, point1, point2, width)

    point1 = coords[-1]
    point2 = pygame.mouse.get_pos()
    pygame.draw.line(screen, 'white', point1, point2)

if __name__ == '__main__':
    pg.run(draw, on_event)
