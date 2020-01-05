
import math
# class Rectangle(object):
#
#     def __init__(self, height, width):
#         self._height = height
#         self._width = width
#
#     @property
#     def height(self):
#         return self._height
#
#     @height.setter
#     def height(self, height):
#         self._height = height
#
#     @property
#     def width(self):
#         return self._width
#
#     @width.setter
#     def width(self, width):
#         self._width = width
#
#     def __str__(self):
#         pass
#
#
# class Circle(object):
#
#     def __init__(self, radius):
#         self._radius = radius
#
#     @property
#     def radius(self):
#         return self._radius
#
#     @radius.setter
#     def radius(self, radius):
#         self._radius = radius

# class AreaCalculator:
#
#     def Area(self, shapes):
#
#         area = 0
#
#         area = shapes.width*shapes.height
#         return area
#
#
# rect = Rectangle(12, 13)
# area = AreaCalculator()
# print(area.Area(rect))

# Let's say if Area is circle then you can do like below

# class AreaCalculator:
#
#     def Area(self, shapes):
#
#         area = 0
#         if isinstance(shapes, Rectangle):
#             area = shapes.width*shapes.height
#         else:
#             area = shapes.radius * shapes.radius * math.pi
#         return area


# rect = Rectangle(12, 13)
# area = AreaCalculator()
# print(area.Area(rect))
#
# cir = Circle(3)
# print(area.Area(cir))


# Now if you have been asked for triangle area then you might have to change AreaCalculator again.
#A solution that abides by the Open/Closed Principle
#One way of solving this puzzle would be to create a base class for both rectangles and
#circles as well as any other shapes that Aldford can think of which defines an abstract method for calculating it’s area.

class Shape:

    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, height, width):
        self._height = height
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    def area(self):
        area = self._width * self._height
        return area


class Circle(Shape):

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        self._radius = radius

    def area(self):
        area = self._radius * self._radius * math.pi
        return area


def Area(shapes):

    area = 0;
    area = shapes.area();

    return area;

rect = Rectangle(2,4)
cir = Circle(3)
print(Area(rect))
print(Area(cir))
