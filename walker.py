import random
from p5 import *

class Walker:
  def __init__(self):
    self.x = width() // 2
    self.y = height() // 2
    print(width, height)

  def show(self):
    stroke(0)
    point(self.x, self.y)

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

    self.x = constrain(self.x, 0, width())
    self.y = constrain(self.y, 0, height())

walker = None

def setup():
	global walker
	createCanvas(640, 240)
	walker = Walker()
	background(255)

def draw():
  walker.step()
  walker.show()

run('Random walk traditional', setup, draw)
