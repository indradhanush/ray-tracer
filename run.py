import sys

from tracer.imager import ImagePlane

if __name__ == '__main__':
    dim = int(sys.argv[1])
    width = dim
    height = dim

    screen = ImagePlane(width, height)
    screen.create_scene()
    screen.render_image()
    screen.save('image' + sys.argv[1] + '.jpg')
