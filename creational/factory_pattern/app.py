from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self) -> None:
        pass


class Rectangle(Shape):
    def draw(self) -> None:
        print("Inside Rectangle::draw() method.")


class Square(Shape):
    def draw(self) -> None:
        print("Inside Square::draw() method.")


class Circle(Shape):
    def draw(self) -> None:
        print("Inside Circle::draw() method.")


class ShapeFactory:
    def getShape(self, shape_type: str) -> Shape:
        if shape_type is None:
            return None
        elif shape_type == "CIRCLE":
            return Circle()
        elif shape_type == "RECTANGLE":
            return Rectangle()
        elif shape_type == "SQUARE":
            return Square()
        else:
            return None


if __name__ == "__main__":
    shape_factory = ShapeFactory()

    shape1 = shape_factory.getShape("CIRCLE")
    shape1.draw()

    shape2 = shape_factory.getShape("RECTANGLE")
    shape2.draw()

    shape3 = shape_factory.getShape("SQUARE")
    shape3.draw()
