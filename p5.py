import pygame

# Global variables
screen = None
stroke_color = (0, 0, 0)
stroke_width = 0
fill_color = (0, 0, 0)
_width, _height = (100, 100)

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

def stroke(*args):
  global stroke_color
  if len(args) == 1:
    args = args * 3
  stroke_color = args

def strokeWidth(value):
  global stroke_width
  stroke_width = value

def fill(*args):
  global fill_color
  if len(args) == 1:
    args = args * 3
  fill_color = args

def point(x, y):
  screen.lock()
  screen.set_at((x, y), stroke_color)
  screen.unlock()

def rect(x, y, w, h):
  pygame.draw.rect(screen, fill_color, (x, y, w, h), stroke_width)

def constrain(v, min, max):
  if v < min:
    return min
  elif v > max:
    return max
  else:
    return v

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
