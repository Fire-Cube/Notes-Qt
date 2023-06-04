from test import poi
import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as spi

def reduce_points(points, factor):
    reduced_points = (points[0],)
    i = iter(points)
    next(i)
    step = factor
    for point in i:
        if step == factor:
            reduced_points += (point,)
            step = 1
        else:
            step += 1
    reduced_points += (points[-1],)
    return reduced_points

import math

def fill_missing_points(coordinates):
  x = [coord[0] for coord in coordinates]
  y = [coord[1] for coord in coordinates]
  
  t = range(len(coordinates))
  ipl_t = np.linspace(0.0, len(coordinates) - 1, num=100*(len(coordinates)-1))
  
  x_tup = spi.splrep(t, x, k=3)
  y_tup = spi.splrep(t, y, k=3)
  
  x_list = list(spi.splev(ipl_t, x_tup))
  y_list = list(spi.splev(ipl_t, y_tup))
  
  filled_coordinates = [(x_list[i], y_list[i]) for i in range(len(x_list))]
  return filled_coordinates

reduced = reduce_points(poi, 2)
plt.scatter(*zip(*poi), s=[10] * len(poi), c="red")
plt.scatter(*zip(*reduced), s=[5] * len(reduced), c="blue")
plt.scatter(*zip(*fill_missing_points(reduced)), s=[2] * len(fill_missing_points(reduced)), c="green")
plt.show()

print(len(poi))
print(len(reduced))
print(len(fill_missing_points(reduced)))

from math import sqrt
cx = 100
cy = 100
r = 20
px = 135.6
py = 134.7

def point():
    d = sqrt((px - cx)**2 + (py - cy)**2)
    x = cx + r * (px - cx) / d
    y = cy + r * (py - cy) / d

    return x, y

x, y = point()

circle = plt.Circle((cx, cy), r)
plt.gca().add_patch(circle)
plt.scatter([x], [y])
plt.show()