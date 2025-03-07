"""
Utility module for pygame
"""
import pygame

def run(caption, loop, on_event=None):
    pygame.init()
    pygame.display.set_caption(caption)

    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            raise SystemExit
        else:
            if on_event is not None:
                on_event(event)

      loop()
      pygame.display.flip()

def get_screen(w, h):
   return pygame.display.set_mode((w, h))
