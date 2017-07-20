import sys

from tracer.imager import ImagePlane

if __name__ == '__main__':
    width = 100 + 1
    height = 100 + 1

    screen = ImagePlane(width, height)
    screen.create_scene()
    screen.render_image()
    screen.save(sys.argv[1])
