from shape3d import Shape3D

class Cube(Shape3D):
    def __init__(self, side):
        self.side = side

    def surface_area(self):
        return 6 * self.side ** 2

    def volume(self):
        return self.side ** 3

    def __str__(self):
        return f"Cube(side={self.side})"