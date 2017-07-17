import sys

import numpy as np
from PIL import Image


class Point():
    def __init__(self, x, y, z=None):
        self.x = x
        self.y = y
        self.z = z


class Sphere():
    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius


class ImagePlane():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.plane = np.arange(
            width * height,
            dtype=np.uint8
        ).reshape(width, height)

    def create_scene(self):
        # Point where the camera is placed at
        self.origin = Point(0, 0, 0)

        # Distance from the camera to the image plane
        self.distance = -50

        self.sphere1 = Sphere(
            centre=Point(0, 0, -250),
            radius=200
        )

    @staticmethod
    def is_valid_root(root):
        if isinstance(root, np.complex128):
            return False

        if root < 0:
            return False

        return True

    def trace_sphere(self, ray, sphere):
        centre = sphere.centre

        px = ray.direction.x
        py = ray.direction.y
        pz = ray.direction.z

        a = (px ** 2) + (py ** 2) + (pz ** 2)

        qx = (ray.start.x - centre.x)
        qy = (ray.start.y - centre.y)
        qz = (ray.start.z - centre.z)

        b = 2 * ((px * qx) + (py * qy) + (pz * qz))

        c = (qx ** 2) + (qy ** 2) + (qz ** 2) - (sphere.radius ** 2)

        roots = np.roots([c, b, a])
        if any(self.is_valid_root(root) for root in roots) is True:
            return True
        else:
            return False

    def render_pixel(self, row, col, pixel, sphere):
        ray = Ray(self.origin, pixel)

        result = self.trace_sphere(ray, sphere)

        if result is True:
            color = 255
        elif result is False:
            color = 0

        self.plane[row][col] = color

    def render_image(self):
        x = -int(self.width/2)
        y = int(self.height/2)

        lowest_x = x

        for row, col in np.ndindex(self.plane.shape):
            self.render_pixel(
                row,
                col,
                Point(x, y, self.distance),
                self.sphere1
            )

            if (col + 1) % width == 0:
                x = lowest_x
                y -= 1
            else:
                x += 1

    def save(self, filename):
        image = Image.fromarray(self.plane)
        with open(filename, 'w') as f:
            image.save(f)


class Ray():
    def __init__(self, start, direction):
        self.start = start
        self.direction = direction


if __name__ == '__main__':
    width = 250 + 1
    height = 250 + 1

    screen = ImagePlane(width, height)
    screen.create_scene()
    screen.render_image()
    screen.save(sys.argv[1])
