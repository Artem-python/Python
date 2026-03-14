from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Базовый класс для геометрических фигур."""

    def __init__(self, color: str = "black", name: str = "Shape"):
        self._color = color
        self.name = name

    @abstractmethod
    def area(self) -> float: pass

    @abstractmethod
    def perimeter(self) -> float: pass

    def get_color(self) -> str: return self._color

    def set_color(self, color: str) -> None:
        if not isinstance(color, str):
            raise ValueError("Color must be a string")
        self._color = color

    def __str__(self) -> str:
        return f"{self.name} (color: {self._color})"

    def __repr__(self) -> str:
        return f"Shape(color='{self._color}', name='{self.name}')"


class Circle(Shape):
    """Класс круга."""

    def __init__(self, radius: float, color: str = "black", name: str = "Circle"):
        super().__init__(color, name)
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

    def diameter(self) -> float:
        return 2 * self.radius

    def __str__(self) -> str:
        return f"{self.name} (color: {self._color}, radius: {self.radius})"

    def __repr__(self) -> str:
        return f"Circle(radius={self.radius}, color='{self._color}', name='{self.name}')"


class Rectangle(Shape):
    """Класс прямоугольника."""

    def __init__(self, width: float, height: float, color: str = "black", name: str = "Rectangle"):
        super().__init__(color, name)
        if width <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive")
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def is_square(self) -> bool:
        return self.width == self.height

    def __str__(self) -> str:
        return f"{self.name} (color: {self._color}, {self.width}x{self.height})"

    def __repr__(self) -> str:
        return f"Rectangle({self.width}, {self.height}, color='{self._color}', name='{self.name}')"


class Square(Rectangle):
    """Класс квадрата (наследуется от Rectangle)."""

    def __init__(self, side: float, color: str = "black", name: str = "Square"):
        super().__init__(side, side, color, name)
        self.side = side

    def set_side(self, side: float) -> None:
        self.side = self.width = self.height = side

    def __str__(self) -> str:
        return f"{self.name} (color: {self._color}, side: {self.side})"

    def __repr__(self) -> str:
        return f"Square({self.side}, color='{self._color}', name='{self.name}')"


if __name__ == "__main__":
    # Примеры использования
    circle = Circle(5, "red", "My Circle")
    print(circle)
    print(f"Area: {circle.area():.2f}")

    rect = Rectangle(4, 6, "blue")
    print(rect)
    print(f"Is square? {rect.is_square()}")

    square = Square(4, "green")
    print(square)
