import pygame

# Global variables
screen = None
stroke_color = None
stroke_width = 0
fill_color = None
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

def noStroke():
  global stroke_color
  stroke_color = None

def noFill():
  global fill_color
  fill_color = None

def stroke(*args):
  global stroke_color
  if len(args) == 1:
    args = args * 3
  stroke_color = args

def strokeWeight(value):
  global stroke_width
  stroke_width = value

def fill(*args):
  global fill_color
  if len(args) == 1:
    args = args * 3
  fill_color = args

def point(x, y):
  if stroke_color is not None:
    screen.lock()
    screen.set_at((x, y), stroke_color)
    screen.unlock()

def rect(x, y, w, h):
  if stroke_color is not None and stroke_width >= 0:
    pygame.draw.rect(screen, stroke_color, (x, y, w, h), stroke_width)
  if fill_color is not None:
    sw2 = stroke_width + stroke_width
    pygame.draw.rect(screen, fill_color, (x+stroke_width, y+stroke_width, w - sw2, h - sw2))

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
