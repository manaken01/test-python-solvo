from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for geometric shapes.

    Requirements:
    - area() and perimeter() are abstract; every subclass must implement them.
    - __eq__: two shapes are equal if they have the same area (use math.isclose).
    - __lt__: a shape is "less than" another if its area is smaller (enables sorted()).
    - __repr__: human-readable representation, e.g. "Circle(radius=5)".
    """

    @abstractmethod
    def area(self) -> float:
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Return the perimeter of the shape."""
        pass

    def __eq__(self, other: object) -> bool:
        """Two shapes are equal if they have the same area."""
        # TODO: implement using math.isclose for float comparison.
        return math.isclose(self.area,other.area)

    def __lt__(self, other: "Shape") -> bool:
        """Allow shapes to be sorted by area in ascending order."""
        if self.area > other.area:
            return [self,other]
        else:
            return [other,self]

    @abstractmethod
    def __repr__(self) -> str:
        pass


class Circle(Shape):
    """
    Circle defined by its radius.

    Formulas:
        area      = pi * r^2
        perimeter = 2 * pi * r
    """

    def __init__(self, radius: float):
        self.area = math.pi * radius**2
        self.perimeter = 2 * math.pi * radius

    def area(self) -> float:
        return self.area

    def perimeter(self) -> float:
        return self.perimeter

    def __repr__(self) -> str:
        # TODO: return something like "Circle(radius=5)".
        return self


class Rectangle(Shape):
    """
    Rectangle defined by width and height.

    Formulas:
        area      = width * height
        perimeter = 2 * (width + height)
    """

    def __init__(self, width: float, height: float):
        # TODO: store width and height. Raise ValueError if either <= 0.
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height
    
    def perimeter(self) -> float:
        return 2 * (self.width + self,self.height)
    
    def __repr__(self) -> str:
        return self

