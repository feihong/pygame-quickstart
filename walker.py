import random
import pygame

class Walker:
	def __init__(self):
		width, height = screen.get_size()
		self.x = width // 2
		self.y = height // 2

	def draw(self):
		color = (0, 0, 0)
		screen.lock()
		screen.set_at((self.x, self.y), color)
		screen.unlock()

	def step(self):
		choice = random.randint(0, 3)
		if choice == 0:
			self.x += 1
		elif choice == 1:
			self.x -= 1
		elif choice == 2:
			self.y += 1
		else:
			self.y -= 1

pygame.init()
pygame.display.set_caption('Random walker')
screen = pygame.display.set_mode((640, 480))
screen.fill((255, 255, 255))
walker = Walker()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  walker.step()
  walker.draw()

  pygame.display.flip()

pygame.quit()
