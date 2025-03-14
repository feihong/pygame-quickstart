"""
- Left line is drawn by naively applying y=mx+b
- Middle line is drawn using Pygame API
- Right line is drawn using Besenham algorithm
"""
import pygame
import pygame.gfxdraw
import pg

pg.set_caption('Bresenham Line')
width = 1000
height = 800
screen = pg.get_screen(width, height)

screen_rect = pygame.Rect(0, 0, width, height)
center = (width // 2, height // 2)
shift_width = 250
use_gfx = False
line_color = (0, 0, 0)

def get_big_line_coords(p1, p2):
    """
    Given two points, return the coordinates of a line that passes through those two points and spans the entire window.
    If the calculation fails, draw a vertical line.
    """
    m = (p1[1] - p2[1]) / (p1[0] - p2[0])
    b = p1[1] - m * p1[0]
    coords = screen_rect.clipline(0, b, width, m * width + b)
    return coords, m, b

def draw_line(p1, p2):
    if use_gfx:
        pygame.gfxdraw.line(screen, p1[0], p1[1], p2[0], p2[1], line_color)
    else:
        pygame.draw.line(screen, line_color, p1, p2)

def draw_vertical_line_if_error(fn):
    def result(p1, p2):
        try:
            fn(p1, p2)
        except ZeroDivisionError:
            draw_line((p1[0], 0), (p1[0], height))

    return result

@draw_vertical_line_if_error
def draw_naive_line(p1, p2):
    coords, m, b = get_big_line_coords(p1, p2)
    for x in range(coords[0][0], coords[1][0]):
        y = m * x + b
        screen.set_at((x, int(y)), line_color)

@draw_vertical_line_if_error
def draw_pygame_line(p1, p2):
    coords, _, _ = get_big_line_coords(p1, p2)
    draw_line(*coords)

@draw_vertical_line_if_error
def draw_bresenham_line(p1, p2):
    coords, _, _ = get_big_line_coords(p1, p2)
    (x0, y0), (x1, y1) = coords

    dx = abs(x1 - x0)
    sx = 1 if x0 < x1 else -1
    dy = -abs(y1 - y0)
    sy = 1 if y0 < y1 else -1
    err = dx + dy

    while True:
        screen.set_at((x0, y0), line_color)
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x0 += sx
        if e2 <= dx:
            err += dx
            y0 += sy

def on_event(event):
    global aliased
    if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
        use_gfx = not use_gfx

def draw():
    screen.fill('white')

    pos = pygame.mouse.get_pos()

    draw_naive_line((center[0] - shift_width, center[1]), (pos[0] - shift_width, pos[1]))

    draw_pygame_line(center, pos)

    draw_bresenham_line((center[0] + shift_width, center[1]), (pos[0] + shift_width, pos[1]))

if __name__ == '__main__':
    pg.run(draw, on_event)
