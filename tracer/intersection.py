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


class Ray():
    def __init__(self, start, direction):
        self.start = start
        self.direction = direction


def trace_sphere(ray, sphere):
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
    root = min(roots)
    if isinstance(root, np.complex128):
        return False

    return True


def render_pixel(origin, plane, pixel, sphere):
    ray = Ray(origin, pixel)

    result = trace_sphere(ray, sphere)

    if result:
        color = 255
    else:
        color = 0

    plane[pixel.x][pixel.y] = color


if __name__ == '__main__':
    width = 100
    height = 100

    # Point where the camera is placed at
    origin = Point(0, 0, 0)

    # Distance from the camera to the image plane
    distance = -50

    sphere1 = Sphere(
        centre=Point(50, 0, -75),
        radius=35
    )

    screen = ImagePlane(width, height)

    for row, col in np.ndindex(screen.plane.shape):
        render_pixel(origin, screen.plane, Point(row, col, distance), sphere1)

    image = Image.fromarray(screen.plane)
    with open('image.jpg', 'w') as f:
        image.save(f)
