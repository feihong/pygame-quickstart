"""
Pressing a key randomizes where the x, y, and free values go in the RGB color
"""
import random
import pygame
import pg
from reloading import reloading

width = 1000
height = 800
screen = pg.get_screen(width, height)

color_indexes = [0, 1, 2]
intensities = [0, 50, 100, 150, 200, 255]
intensity = 255

def get_color(x, y):
    res = (int(x / width * 225), int(y / height * 255), intensity)
    return tuple(res[i] for i in color_indexes)

# @reloading
def on_event(event):
    global color_indexes, intensity

    if event.type == pygame.KEYDOWN:
        color_indexes = random.sample(color_indexes, k=3)
        intensity = random.choice(intensities)
        print(color_indexes, intensity)

def loop():
    for y in range(height):
        for x in range(width):
            screen.set_at((x, y), get_color(x, y))

pg.run('RGB Space', loop, on_event)
