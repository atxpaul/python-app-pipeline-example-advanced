import numpy as np

class GeometryCalculator:
    def area_of_rectangle(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive values.")
        return width * height

    def perimeter_of_rectangle(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive values.")
        return 2 * (width + height)

    def area_of_circle(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive value.")
        return np.pi * (radius ** 2)

    def perimeter_of_circle(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive value.")
        return 2 * np.pi * radius

if __name__ == "__main__":
    calculator = GeometryCalculator()
    print("Area of rectangle (3, 4):", calculator.area_of_rectangle(3, 4))
    print("Perimeter of rectangle (3, 4):", calculator.perimeter_of_rectangle(3, 4))
    print("Area of circle (5):", calculator.area_of_circle(5))
    print("Perimeter of circle (5):", calculator.perimeter_of_circle(5))