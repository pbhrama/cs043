import math


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<" + self.__class__.__name__ + " x=" + str(self.x) + " y=" + str(self.y) + ">"

    def area(self):
        return self.x * self.y

    def circumference(self):
        return round(2 * math.pi * self.radius, 3)


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def __repr__(self):
        return "<" + self.__class__.__name__ + " x=" + str(self.x) + " y=" + str(self.y) + " radius=" + str(
            self.radius) + ">"

    def area(self):
        return round(math.pi * (self.radius ** 2), 3)


class Rectangle(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __repr__(self):
        return "<" + self.__class__.__name__ + " x=" + str(self.x) + " y=" + str(self.y) + ">"


class RightTriangle(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __repr__(self):
        return "<" + self.__class__.__name__ + " x=" + str(self.x) + " y=" + str(self.y) + ">"

    def area(self):
        triangleArea = super().area()
        return triangleArea / 2


class Square(Rectangle):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __repr__(self):
        return "<" + self.__class__.__name__ + " x=" + str(self.x) + " y=" + str(self.y) + ">"


circle_ex = Circle(10, 20, 30)
square_ex = Square(10, 10)
rectangle_ex = Rectangle(20, 30)
rightTriangle_ex = RightTriangle(2, 3)
shape_ex = Shape(35, 40)

print("Inheritance and Polymorphism examples:")
print("Circle circumference: " + str(circle_ex.circumference()))
print("Circle area: " + str(circle_ex.area()))
print("Square area: " + str(square_ex.area()))
print("Rectangle area: " + str(rectangle_ex.area()))
print("Triangle area: " + str(rightTriangle_ex.area()))
print("------------------------------------------------")
print("Representation function examples:")
print(circle_ex)
print(square_ex)
print(rightTriangle_ex)
print(shape_ex)
