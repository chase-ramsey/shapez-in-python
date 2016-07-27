class Shape:

  def __init__(self):
    self.area = 0

class Circular(Shape):

  def __init__(self):
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
    self.set_circumference((radius * 2) * 3.1415)

  def calc_area(self):
    self.area = float((format((self.radius * self.radius) * 3.1415), '.2f'))

class Trilateral(Shape):

  def __init__(self):
    pass

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
