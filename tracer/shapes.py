import numpy as np


class Shape():
    def trace(self, ray):
        raise NotImplementedError


class Sphere(Shape):
    def __init__(self, centre, radius, scene):
        self.centre = centre
        self.radius = radius
        self.scene = scene

    @staticmethod
    def is_valid_root(root):
        if isinstance(root, np.complex128):
            return False

        if root < 0:
            return False

        return True

    @classmethod
    def get_valid_root(cls, roots):
        valid_roots = [root for root in roots if cls.is_valid_root(root)]
        return min(valid_roots) if valid_roots else None

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

        root = self.get_valid_root(roots)
        if root is None:
            return (0, 0, 0)

        intersection_vector = np.add(
            self.scene.origin.vector,
            np.multiply(root, ray.vector)
        )

        radius_vector = np.subtract(intersection_vector, self.centre.vector)

        magnitude = np.linalg.norm(radius_vector)

        surface_normal = np.true_divide(radius_vector, magnitude)

        vectorized_remap = np.vectorize(lambda x: (x+1)/2)
        surface_normal = vectorized_remap(surface_normal)

        color = np.abs(np.multiply(255, surface_normal))

        # Ensure that all colors are between black and white
        if not all(i >= 0 and i <= 255 for i in color):
            raise Exception

        return color
