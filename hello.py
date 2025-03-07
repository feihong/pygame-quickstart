"""
Show Hello World in all the fonts accessible to pygame
"""
import pygame

pygame.init()
pygame.display.set_caption('Hello World')

screen = pygame.display.set_mode((640, 240))
clock = pygame.time.Clock()

# fonts = ['arialunicode', 'pingfang', 'songti', 'stheitilight', 'stheitimedium']
fonts = pygame.font.get_fonts()
fonts.sort()
current_font = 0

def get_font(size):
  return pygame.font.Font(pygame.font.match_font(fonts[current_font]), size)

font = get_font(48)
small_font = pygame.font.Font(pygame.font.match_font('arialunicode'), 24)
black = (0,0,0)

def draw_text(font, text, dest):
  try:
    screen.blit(pygame.font.Font.render(font, text, True, 'black'), dest)
  except pygame.error as e:
    print(e)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      raise SystemExit
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        current_font += 1
      elif event.key == pygame.K_LEFT:
        current_font -= 1
      elif event.key == pygame.K_UP:
        current_font -= 25
      elif event.key == pygame.K_DOWN:
        current_font += 25

      current_font = current_font % len(fonts)
      font = get_font(48)
      print(current_font)

  screen.fill('white')

  draw_text(small_font, f'Font: {fonts[current_font]} ({current_font + 1} of {len(fonts)})', (20, 10))

  draw_text(font, 'Hello World!', (20, 60))

  draw_text(font, '你好世界！', (20, 120))

  pygame.display.flip()
  clock.tick(30)
