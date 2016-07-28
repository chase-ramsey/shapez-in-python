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
    self.perimeter = 0

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
    area = math.sqrt(peri * (peri - a) * (peri - b) * (peri - c))
    self.area = area


class Rectangular(Shape):

  def __init__(self):
    pass

class Cylinder(Circular):

  def __init__(self):
    pass

class Pyramid(Trilateral):

  def __init__(self):
    pass

class Cube(Rectangular):

  def __init__(self):
    pass
