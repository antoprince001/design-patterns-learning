**Bridge** is a structural design pattern that lets you split a large class or a set of closely related classes into two separate hierarchies—abstraction and implementation—which can be developed independently of each other.

ColorImplementation is the Implementor interface for colors with the apply_color method.

RedColor and GreenColor are concrete implementations of colors.

Shape is the Abstraction class that takes a color implementation in its constructor.

Circle and Square are concrete shapes that inherit from Shape. They use the color implementation to apply the color to the shape.

The client code demonstrates creating different shapes with various color implementations, showing how you can change both the shape and color independently.

When you run this code, you'll see that you can create different shapes with different colors, all thanks to the Bridge Pattern, which decouples the shape abstraction from the color implementation.