"""
- Left line is drawn by naively applying y=mx+b
- Middle line is drawn using Pygame API
- Right line is drawn using Besenham algorithm
"""
import pygame
import pg

width = 1000
height = 800
screen = pg.get_screen(width, height)

screen_rect = pygame.Rect(0, 0, width, height)
center = (width // 2, height // 2)
shift_width = 250

def draw_vertical_line(p):
    pygame.draw.line(screen, 'white', (p[0], 0), (p[0], height))

def draw_naive_line(p1, p2):
    if p1[0] == p2[0]:
        draw_vertical_line(p1)
    else:
        m = (p1[1] - p2[1]) / (p1[0] - p2[0])
        b = p1[1] - m * p1[0]
        coords = screen_rect.clipline(0, b, width, m * width + b)
        for x in range(coords[0][0], coords[1][0]):
            y = m * x + b
            screen.set_at((x, int(y)), 'white')

def draw_pygame_line(p1, p2):
    if p1[0] == p2[0]:
        draw_vertical_line(p1)
    else:
        m = (p1[1] - p2[1]) / (p1[0] - p2[0])
        b = p1[1] - m * p1[0]
        coords = screen_rect.clipline(0, b, width, m * width + b)
        pygame.draw.line(screen, 'white', *coords)

def draw_besenham_line(p1, p2):
    if p1[0] == p2[0]:
        draw_vertical_line(p1)
        return

    m = (p1[1] - p2[1]) / (p1[0] - p2[0])
    b = p1[1] - m * p1[0]
    (x0, y0), (x1, y1) = screen_rect.clipline(0, b, width, m * width + b)

    dx = abs(x1 - x0)
    sx = 1 if x0 < x1 else -1
    dy = -abs(y1 - y0)
    sy = 1 if y0 < y1 else -1
    err = dx + dy

    while True:
        screen.set_at((x0, y0), 'white')
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x0 += sx
        if e2 <= dx:
            err += dx
            y0 += sy

def loop():
    screen.fill('black')

    pos = pygame.mouse.get_pos()

    draw_pygame_line(center, pos)

    draw_naive_line((center[0] - shift_width, center[1]), (pos[0] - shift_width, pos[1]))

    draw_besenham_line((center[0] + shift_width, center[1]), (pos[0] + shift_width, pos[1]))

pg.run('Bresenham Line', loop)
