import unittest
from sharpshapes import *

class TestShape(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.shape = Shape()

  def test_shape_area_zero_default:
    self.assertEqual(self.shape.area, 0)

class TestCircular(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.circular = Circular(Shape)

  def test_circular_is_instance_shape(self):
    self.assertIsInstance(self.circular, Shape)

  def test_circular_has_area_default_zero(self):
    self.assertEqual(self.circular.area, 0)

  def test_radius_zero_default(self):
    self.circular.radius = 0

  def test_diameter_zero_default(self):
    self.circular.diameter = 0

  def test_circumference_zero_default(self):
    self.circular.circumference = 0

  def test_set_dimensions(self):
    circle_shape = Circular(Shape)
    circle_shape.set_dimensions(5)
    self.assertEqual(circle_shape.radius, 5)
    self.assertEqual(circle_shape.diameter, 10)
    self.assertEqual(circle_shape.circumference, 31.41)

  def test_calculate_area_circle(self):
    circle_shape = Circular(Shape)
    circle_shape.set_dimensions(5)
    circle_shape.calc_area()
    self.assertEqual(circle_shape.area, 78.54)


class TestTrilateral(unittest.TestCase):
  pass

class TestQuadrilateral(unittest.TestCase):
  pass


if __name__ == '__main__':
  unittest.main()
