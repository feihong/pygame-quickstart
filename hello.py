import pygame
import pygame.freetype

pygame.init()
pygame.display.set_caption('Hello World')

pygame.freetype.init()
print(pygame.freetype.get_default_font())
my_font = pygame.freetype.SysFont('Arial', 48)

screen = pygame.display.set_mode((480, 240))

running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill((255,255,255))

  # text_surface, rect = my_font.render('Hello World!', (0, 0, 0))
  # screen.blit(text_surface, (20, 50))

  my_font.render_to(screen, (20, 50), 'Hello World!', (0, 0, 0))
  # Doesn't work for some reason
  my_font.render_to(screen, (50, 100), '你好世界！', (0, 0, 0))

  pygame.display.flip()

pygame.quit()
