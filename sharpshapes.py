import math
from functools import reduce

class Shape:

  def __init__(self):
    self.area = 0

class Circular(Shape):

  def __init__(self):
    super().__init__()
    self.radius = 0
    self.diameter = 0
    self.circumference = 0

  def set_radius(self, num):
    self.radius = num

  def set_diameter(self, num):
    self.diameter = num

  def set_circumference(self, num):
    self.circumference = num

  def set_dimensions(self, radius):
    self.set_radius(radius)
    self.set_diameter(radius * 2)
    circ = format((radius * 2) * 3.1415, '.2f')
    self.set_circumference(float(circ))

  def calc_area(self):
    area = format((self.radius * self.radius) * 3.1415, '.2f')
    self.area = float(area)

class Trilateral(Shape):

  def __init__(self):
    super().__init__()
    self.sides = list()

  def set_dimensions(self, s1, s2, s3):
    self.sides.append(s1)
    self.sides.append(s2)
    self.sides.append(s3)
    self.sides.sort()

  def calc_perimeter(self):
    self.perimeter = reduce(lambda x, y: x + y, self.sides)

  def calc_area(self):
    a, b, c = self.sides[0], self.sides[1], self.sides[2]
    peri = reduce(lambda x, y: x + y, self.sides)
    peri /= 2
    area = format(math.sqrt(peri * (peri - a) * (peri - b) * (peri - c)), '.2f')
    self.area = float(area)


class Rectangular(Shape):

  def __init__(self):
    super().__init__()
    self.sides = list()

  def set_dimensions(self, base, height):
    self.sides.append(base)
    self.sides.append(height)

  def calc_perimeter(self):
    self.perimeter = (2 * self.sides[0]) + (2 * self.sides[1])

  def calc_area(self):
    self.area = self.sides[0] * self.sides[1]

class Cylinder():

  def __init__(self):
    self.base = Circular()
    self.height = 0
    self.volume = 0

  def set_dimensions(self, radius, height):
    self.base.set_dimensions(radius)
    self.base.calc_area()
    self.height = height

  def calc_volume(self):
    self.volume = float(format(self.base.area * self.height, '.2f'))

class Pyramid():

  def __init__(self):
    self.base = Rectangular()
    self.height = 0
    self.volume = 0

  def set_dimensions(self, height, base):
    self.height = height
    self.base.sides.extend([base, base])

  def calc_volume(self):
    a, b, c = self.base.sides[0], self.base.sides[1], self.height
    volume = format((a * b * c) / 3, '.2f')
    self.volume = float(volume)

class Cube():

  def __init__(self):
    self.base = Rectangular()
    self.depth = 0
    self.volume = 0

  def set_dimensions(self, val):
    self.base.sides.extend([val, val])
    self.depth = val

  def calc_volume(self):
    a, b, c = self.base.sides[0], self.base.sides[1], self.depth
    self.volume = a * b * c

