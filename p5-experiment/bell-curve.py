import math
from p5 import *

title = 'Bell Curve'

heights = None
sd = 0.5
sd_dir = 0.01
e = 2.71828183 # "e", see http://mathforum.org/dr.math

def setup():
  global heights
  createCanvas(640, 240)
  heights = [0] * width()

def draw():
  global sd, sd_dir

  background(255)
  m = 0
  for i in range(width()):
    xcoord = map(i, 0, width(), -3, 3)
    sq2pi = math.sqrt(2 * math.pi)
    xmsq = -1 * (xcoord - m) * (xcoord - m)
    sdsq = sd * sd
    heights[i] = (1 / (sd * sq2pi)) * math.pow(e, xmsq / sdsq)

  sd += sd_dir
  if sd > 2 or sd < 0.3:
    sd_dir *= -1

  stroke(0)
  strokeWeight(2)
  noFill()
  for i, h in enumerate(heights):
    x = i
    y = map(h, 0, 1, height() - 2, 2)
    point(x, y)

run(title, setup, draw)
