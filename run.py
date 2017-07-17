import sys

from tracer.intersection import ImagePlane

if __name__ == '__main__':
    width = 250 + 1
    height = 250 + 1

    screen = ImagePlane(width, height)
    screen.create_scene()
    screen.render_image()
    screen.save(sys.argv[1])
