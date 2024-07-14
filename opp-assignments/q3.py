import math

class Circle:
    def _init_(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    
    def get_area(self):
        area = math.pi * self.radius ** 2
        return area
    
    def get_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter
    
    def get_circumference(self):
        circumference = self.get_perimeter()
        return circumference


circle1 = Circle(0, 0, 5)
print(f"Area of circle: {circle1.get_area():.2f}")
print(f"Perimeter of circle: {circle1.get_perimeter():.2f}")
print(f"Circumference of circle: {circle1.get_circumference():.2f}")