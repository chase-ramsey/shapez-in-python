from sharpshapes import *

class ShapesMenu:

  def __init__(self):
    pass

  def show_menu(self):
    print('What kind of shape would you like to make?')
    print('1. Circle')
    print('2. Triangle')
    print('3. Rectangle')
    print('4. Cylinder')
    print('5. Pyramid')
    print('6. Cube')
    print('7. Quit')
    choice = input('> ')

    if choice != '7':

      if choice == '1':
        circle = Circular()
        print('What is the circle\'s radius?')
        radius = int(input('> '))
        circle.set_dimensions(radius)
        print("The circle's diameter is {0}".format(circle.diameter))
        print("The circle's circumference is {0}".format(circle.circumference))
        circle.calc_area()
        print("The circle's area is {0}".format(circle.area))

      elif choice == '2':
        tri = Trilateral()
        print('What is the length of the first side?')
        s1 = int(input('> '))
        print('What is the length of the second side?')
        s2 = int(input('> '))
        print('What is the length of the third side?')
        s3 = int(input('> '))
        tri.set_dimensions(s1, s2, s3)
        tri.calc_perimeter()
        print("The triangle's perimeter is {0}".format(tri.perimeter))
        tri.calc_area()
        print("The triangle's area is {0}".format(tri.area))

      elif choice == '3':
        quad = Rectangular()
        print('What is rectangle\'s height?')
        s1 = int(input('> '))
        print('What is rectangle\'s length?')
        s2 = int(input('> '))
        quad.set_dimensions(s1, s2)
        quad.calc_perimeter()
        print("The rectangle's perimeter is {0}".format(quad.perimeter))
        quad.calc_area()
        print("The triangle's area is {0}".format(quad.area))

      elif choice == '4':
        cyl = Cylinder()
        print('What is the radius of the cylinder\'s base?')
        radius = int(input('> '))
        print('What is the height of the cylinder?')
        height = int(input('> '))
        cyl.set_dimensions(radius, height)
        print("The diameter of the cylinder's base is {0}".format(cyl.base.diameter))
        print("The circumference of the cylinder's base is {0}".format(cyl.base.circumference))
        cyl.base.calc_area()
        print("The circle's area is {0}".format(cyl.base.area))
        cyl.calc_volume()
        print("The cylinder's volume is {0}".format(cyl.volume))

      elif choice == '5':
        pyr = Pyramid()
        print('What is the length of the pyramid\'s base?')
        length = int(input('> '))
        print('What is the pyramid\'s height?')
        height = int(input('> '))
        pyr.set_dimensions(length, height)
        pyr.base.calc_perimeter()
        print('The perimeter of the pyramid\'s base is {0}'.format(pyr.base.perimeter))
        pyr.base.calc_area()
        print('The area of the pyramid\'s base is {0}'.format(pyr.base.area))
        pyr.calc_volume()
        print('The volume of the pyramid\'s base is {0}'.format(pyr.volume))

      elif choice == '6':
        cube = Cube()
        print('What is the length of the sides of the cube?')
        length = int(input('> '))
        cube.set_dimensions(length)
        cube.base.calc_perimeter()
        print('The perimeter of the cube\'s base is {0}'.format(cube.base.perimeter))
        cube.base.calc_area()
        print('The area of the cube\'s base is {0}'.format(cube.base.area))
        cube.calc_volume()
        print('The volume of the cube\'s base is {0}'.format(cube.volume))

      self.show_menu()

    elif choice == '7':
      quit()

    else:
      print('Sorry, I didn\'t understand your choice. Try again?')
      self.show_menu()
