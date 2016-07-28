import unittest
from sharpshapes import *

class TestShape(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.shape = Shape()

  def test_shape_area_zero_default(self):
    self.assertEqual(self.shape.area, 0)

class TestCircular(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.circular = Circular()

  def test_circular_is_instance_shape(self):
    self.assertIsInstance(self.circular, Shape)

  def test_circular_has_area_default_zero(self):
    self.assertEqual(self.circular.area, 0)

  def test_radius_zero_default(self):
    self.assertEqual(self.circular.radius, 0)

  def test_diameter_zero_default(self):
    self.assertEqual(self.circular.diameter, 0)

  def test_circumference_zero_default(self):
    self.assertEqual(self.circular.circumference, 0)

  def test_set_radius(self):
    circle_shape = Circular()
    circle_shape.set_radius(5)
    self.assertEqual(circle_shape.radius, 5)

  def test_set_diameter(self):
    circle_shape = Circular()
    circle_shape.set_diameter(5)
    self.assertEqual(circle_shape.diameter, 5)

  def test_set_circumference(self):
    circle_shape = Circular()
    circle_shape.set_circumference(5)
    self.assertEqual(circle_shape.circumference, 5)

  def test_circular_set_dimensions(self):
    circle_shape = Circular()
    circle_shape.set_dimensions(5)
    self.assertEqual(circle_shape.radius, 5)
    self.assertEqual(circle_shape.diameter, 10)
    self.assertEqual(circle_shape.circumference, 31.42)

  def test_calculate_area_circle(self):
    circle_shape = Circular()
    circle_shape.set_dimensions(5)
    circle_shape.calc_area()
    self.assertEqual(circle_shape.area, 78.54)


class TestTrilateral(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.trilateral = Trilateral()

  def test_trilateral_is_instance_shape(self):
    self.assertIsInstance(self.trilateral, Shape)

  def test_trilateral_has_area_default_zero(self):
    self.assertEqual(self.trilateral.area, 0)

  def test_trilateral_sides_empty_list_default(self):
    self.assertIsInstance(self.trilateral.sides, list)
    self.assertEqual(self.trilateral.sides, [])

  def test_trilateral_set_dimensions(self):
    tri = Trilateral()
    tri.set_dimensions(3, 4, 5)
    tri.sides = [3, 4, 5]

  def test_calculate_perimeter_triangle(self):
    tri = Trilateral()
    tri.set_dimensions(3, 4, 5)
    tri.calc_perimeter()
    self.assertEqual(tri.perimeter, 12)

  def test_calculate_area_triangle(self):
    tri = Trilateral()
    tri.set_dimensions(3, 4, 5)
    tri.calc_area()
    self.assertEqual(tri.area, 6)

class TestRectangular(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.rectangular = Rectangular()

  def test_rectangular_is_instance_shape(self):
    self.assertIsInstance(self.rectangular, Shape)

  def test_rectangular_has_area_default_zero(self):
    self.assertEqual(self.rectangular.area, 0)

  def test_rectangular_sides_empty_list_default(self):
    self.assertIsInstance(self.rectangular.sides, list)
    self.assertEqual(self.rectangular.sides, [])

  def test_rectangular_set_dimensions(self):
    rect = Rectangular()
    rect.set_dimensions(4, 4)
    self.assertEqual(rect.sides, [4, 4])

  def test_calculate_perimeter_rectangle(self):
    rect = Rectangular()
    rect.set_dimensions(4, 4)
    rect.calc_perimeter()
    self.assertEqual(rect.perimeter, 16)

  def test_calculate_area_rectangle(self):
    rect = Rectangular()
    rect.set_dimensions(4, 4)
    rect.calc_area()
    self.assertEqual(rect.area, 16)

class TestCylinder(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.cylinder = Cylinder()

  def test_cylinder_base_is_circular(self):
    self.assertIsInstance(self.cylinder.base, Circular)

  def test_cylinder_base_inherits_circular_properties(self):
    self.assertEqual(self.cylinder.base.area, 0)
    self.assertEqual(self.cylinder.base.radius, 0)
    self.assertEqual(self.cylinder.base.diameter, 0)
    self.assertEqual(self.cylinder.base.circumference, 0)

  def test_cylinder_height_default_zero(self):
    self.assertEqual(self.cylinder.height, 0)

  def test_cylinder_volume_default_zero(self):
    self.assertEqual(self.cylinder.volume, 0)

  def test_set_cylinder_dimensions(self):
    cylinder = Cylinder()
    cylinder.set_dimensions(5, 10)
    self.assertEqual(cylinder.base.radius, 5)
    self.assertEqual(cylinder.base.diameter, 10)
    self.assertEqual(cylinder.base.circumference, 31.42)
    self.assertEqual(cylinder.height, 10)

  def test_calculate_cylinder_volume(self):
    cylinder = Cylinder()
    cylinder.set_dimensions(5, 10)
    cylinder.calc_volume()
    self.assertEqual(int(cylinder.volume), 785)


class TestPyramid(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.pyramid = Pyramid()

  def test_pyramid_base_has_rectangular(self):
    self.assertIsInstance(self.pyramid.base, Rectangular)

  def test_pyramid_height_default_zero(self):
    self.assertEqual(self.pyramid.height, 0)

  def test_pyramid_volume_default_zero(self):
    self.assertEqual(self.pyramid.volume, 0)

  def test_pyramid_base_inherits_rectangular_properties(self):
    self.assertIsInstance(self.pyramid.base.sides, list)
    self.assertEqual(self.pyramid.base.sides, [])

  def test_set_pyramid_dimensions(self):
    pyramid = Pyramid()
    pyramid.set_dimensions(5, 4)
    self.assertEqual(pyramid.base.sides, [4, 4])
    self.assertEqual(pyramid.height, 5)

  def test_calculate_pyramid_volume(self):
    pyramid = Pyramid()
    pyramid.set_dimensions(5, 4)
    pyramid.calc_volume()
    self.assertEqual(pyramid.volume, 26.67)

class TestCube(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.cube = Cube()

  def test_cube_base_is_rectangular(self):
    self.assertIsInstance(self.cube.base, Rectangular)

  def test_cube_depth_default_zero(self):
    self.assertEqual(self.cube.depth, 0)

  def test_cube_volume_default_zero(self):
    self.assertEqual(self.cube.volume, 0)

  def test_cube_base_inherits_rectangular_properties(self):
    self.assertIsInstance(self.cube.base.sides, list)
    self.assertEqual(self.cube.base.sides, [])

  def test_set_cube_dimensions(self):
    cube = Cube()
    cube.set_dimensions(4)
    self.assertEqual(cube.depth, 4)
    self.assertEqual(cube.base.sides, [4, 4])

  def test_calculate_cube_volume(self):
    cube = Cube()
    cube.set_dimensions(4)
    cube.calc_volume()
    self.assertEqual(cube.volume, 64)


if __name__ == '__main__':
  unittest.main()
