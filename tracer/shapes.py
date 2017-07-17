import numpy as np


class Shape():
    def trace(self, ray):
        raise NotImplementedError


class Sphere(Shape):
    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius

    @staticmethod
    def is_valid_root(root):
        if isinstance(root, np.complex128):
            return False

        if root < 0:
            return False

        return True

    def trace(self, ray):
        px = ray.direction.x
        py = ray.direction.y
        pz = ray.direction.z

        a = (px ** 2) + (py ** 2) + (pz ** 2)

        qx = (ray.start.x - self.centre.x)
        qy = (ray.start.y - self.centre.y)
        qz = (ray.start.z - self.centre.z)

        b = 2 * ((px * qx) + (py * qy) + (pz * qz))

        c = (qx ** 2) + (qy ** 2) + (qz ** 2) - (self.radius ** 2)

        roots = np.roots([c, b, a])
        if any(self.is_valid_root(root) for root in roots) is True:
            return True
        else:
            return False
