import math
from shape3d import Shape3D

class Sphere(Shape3D):
    def __init__(self, radius):
        self.radius = radius

    def surface_area(self):
        return 4 * math.pi * self.radius ** 2

    def volume(self):
        return (4/3) * math.pi * self.radius ** 3

    def __str__(self):
        return f"Sphere(radius={self.radius})"