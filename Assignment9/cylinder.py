import math
from shape3d import Shape3D

class Cylinder(Shape3D):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def surface_area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

    def volume(self):
        return math.pi * self.radius ** 2 * self.height

    def __str__(self):
        return f"Cylinder(radius={self.radius}, height={self.height})"