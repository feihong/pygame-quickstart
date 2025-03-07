import random
from p5 import *

title = 'Gaussian distribution'

def setup():
  global randomCounts
  createCanvas(640, 240)
  background(255)

def draw():
  x = random.gauss(320, 60)
  noStroke()
  fill(0, 10)
  circle(x, 120, 16)

run(title, setup, draw)
