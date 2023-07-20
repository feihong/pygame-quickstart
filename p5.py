import math
import pygame

__all__ = ['background', 'circle', 'constrain', 'createCanvas', 'fill', 'floor', 'height', 'map', 'noFill', 'noStroke',
           'point', 'rect', 'run', 'stroke', 'strokeWeight', 'width']

# Global variables
screen: pygame.Surface = None
stroke_color = None
stroke_width = 0
fill_color = None
_width, _height = (100, 100)
shape = None

def createCanvas(w, h):
  global screen, _width, _height
  _width = w
  _height = h
  screen = pygame.display.set_mode((_width, _height))

def width():
  return _width

def height():
  return _height

def background(*args):
  if len(args) == 1:
    args = args * 3
  screen.fill(args)

def noStroke():
  global stroke_color
  stroke_color = None

def noFill():
  global fill_color
  fill_color = None

def args_to_color(args):
  size = len(args)
  if size == 1:
    v = args[0]
    return pygame.Color(v, v, v)
  elif size == 2:
    v, a = args
    # print(v, a, pygame.Color(v, v, v, a) )
    return pygame.Color(v, v, v, a)
  else:
    return pygame.Color(*args)

def stroke(*args):
  global stroke_color
  stroke_color = args_to_color(args)

def strokeWeight(value):
  global stroke_width
  stroke_width = value

def fill(*args):
  global fill_color
  fill_color = args_to_color(args)

def circle(x, y, r):
  if stroke_color is not None and stroke_width >= 0:
    pygame.draw.circle(screen, stroke_color, (x, y), r, stroke_width)
  if fill_color is not None:
    sw2 = stroke_width + stroke_width

    if fill_color.a >= 255:
      pygame.draw.circle(screen, fill_color, (x, y), r - sw2)
    else:
      r2 = r + r
      target_rect = pygame.Rect(x, y, 0, 0).inflate(r2, r2)
      shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
      pygame.draw.circle(shape_surf, fill_color, (r, r), r)
      screen.blit(shape_surf, target_rect)

def point(x, y):
  if stroke_color is not None:
    if stroke_width > 1:
      circle(x, y, stroke_width)
    else:
      screen.set_at((math.floor(x), math.floor(y)), stroke_color)

def rect(x, y, w, h):
  if stroke_color is not None and stroke_width >= 0:
    pygame.draw.rect(screen, stroke_color, (x, y, w, h), stroke_width)
  if fill_color is not None:
    sw2 = stroke_width + stroke_width
    screen.fill(fill_color, (x+stroke_width, y+stroke_width, w - sw2, h - sw2))

def constrain(v, min, max):
  if v < min:
    return min
  elif v > max:
    return max
  else:
    return v

def map(n, start1, stop1, start2, stop2,):
  newval = (n - start1) / (stop1 - start1) * (stop2 - start2) + start2
  if start2 < stop2:
    return constrain(newval, start2, stop2)
  else:
    return constrain(newval, stop2, start2)

def not_implemented_function(message):
  def result(*args):
    raise NotImplementedError(message)
  return result

floor = not_implemented_function('Use math.floor instead')

def run(title: str, setup, draw) -> None:
  global screen

  pygame.init()
  pygame.display.set_caption(title)
  clock = pygame.time.Clock()

  setup()

  if screen is None:
    screen = pygame.display.set_mode((_width, _height))

  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    draw()

    clock.tick(60)
    pygame.display.flip()

  pygame.quit()
