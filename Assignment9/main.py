import random
from sphere import Sphere
from cylinder import Cylinder
from cube import Cube

def generate_random_shape():
    shape_type = random.choice(["sphere", "cylinder", "cube"])

    if shape_type == "sphere":
        radius = random.randint(1, 10)
        return Sphere(radius)

    elif shape_type == "cylinder":
        radius = random.randint(1, 10)
        height = random.randint(5, 20)
        return Cylinder(radius, height)

    else:
        side = random.randint(1, 10)
        return Cube(side)


def main():
    shapes = [generate_random_shape() for _ in range(10)]

    for shape in shapes:
        print(f"\nShape: {shape}")
        print(f"Surface Area: {shape.surface_area():.2f}")
        print(f"Volume: {shape.volume():.2f}")


if __name__ == "__main__":
    main()