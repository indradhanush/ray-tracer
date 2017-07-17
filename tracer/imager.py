import numpy as np
from PIL import Image

from tracer.shapes import Sphere


class Point():
    def __init__(self, x, y, z=None):
        self.x = x
        self.y = y
        self.z = z


class Ray():
    def __init__(self, start, direction):
        self.start = start
        self.direction = direction


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

    def render_pixel(self, row, col, pixel, sphere):
        ray = Ray(self.origin, pixel)

        result = sphere.trace(ray)
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

            if (col + 1) % self.width == 0:
                x = lowest_x
                y -= 1
            else:
                x += 1

    def save(self, filename):
        image = Image.fromarray(self.plane)
        with open(filename, 'w') as f:
            image.save(f)
