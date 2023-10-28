# Implementor interface for colors
class ColorImplementation:
    def apply_color(self):
        pass

# Concrete implementations for colors
class RedColor(ColorImplementation):
    def apply_color(self):
        return "Red"

class GreenColor(ColorImplementation):
    def apply_color(self):
        return "Green"

# Abstraction for shapes
class Shape:
    def __init__(self, color_implementation):
        self.color_implementation = color_implementation

    def apply_color(self):
        return f"Shape filled with {self.color_implementation.apply_color()}"

# Concrete shapes
class Circle(Shape):
    def draw(self):
        return f"Circle: {self.apply_color()}"

class Square(Shape):
    def draw(self):
        return f"Square: {self.apply_color()}"

# Client code
red_color = RedColor()
green_color = GreenColor()

circle = Circle(red_color)
square = Square(green_color)

print(circle.draw())
print(square.draw())
