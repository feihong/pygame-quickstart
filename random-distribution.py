import random
from p5 import *

title = 'Random distribution'

randomCounts = None
total = 20

def setup():
  global randomCounts
  createCanvas(640, 240)
  randomCounts = [0] * total

def draw():
  background(255)
  index = random.randint(0, total - 1)
  randomCounts[index] += 1

  stroke(0)
  strokeWeight(2)
  fill(127)
  w = width() // total

  for x in range(total):
    rect(x * w, height() - randomCounts[x], w, randomCounts[x])

run(title, setup, draw)
