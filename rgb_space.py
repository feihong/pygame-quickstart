import random
import pygame
import pg
from reloading import reloading

width = 1000
height = 800
screen = pg.get_screen(width, height)

color_indexes = [0, 1, 2]

def get_color(x, y):
    res = (int(x / width * 225), int(y / height * 255), 255)
    return tuple(res[i] for i in color_indexes)

def on_event(event):
    global color_indexes
    if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
        new_indexes = random.sample(color_indexes, k=3)
        while new_indexes == color_indexes:
            new_indexes = random.sample(color_indexes, k=3)
        color_indexes = new_indexes
        print(color_indexes)

@reloading
def loop():
    for y in range(height):
        for x in range(width):
            screen.set_at((x, y), get_color(x, y))

pg.run('RGB Space', loop, on_event=on_event)
