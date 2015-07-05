import sys
import pyqrcode
from PIL import Image
import StringIO
import math

def main():
    f = file(sys.argv[1]).read()
    ch = chunk(f, 500)
    images = []
    p_size = 0
    print len(ch)
    count = 0
    for i in ch:
        print "%d" % count
        count += 1
        temp_s = StringIO.StringIO()
        padded_data = i.ljust(500, "\x00")
        qr = pyqrcode.create(padded_data.encode("base64"), encoding="base64")
        p_size = max(qr.get_png_size(), p_size)
        qr.png(temp_s)
        images.append(temp_s.getvalue())

    root_dimensions = math.sqrt(len(images))
    if root_dimensions**2 < len(images):
        root_dimensions += 1
    root_dimensions = int(root_dimensions)

    new_image = Image.new("RGBA", ((root_dimensions)*p_size, (root_dimensions+2)*p_size), color=(255,255,255))
    print "Writing new image with size (%d, %d)" % new_image.size

    x = 0
    y = 0
    for i in range(len(images)):
        if i != 0 and i % root_dimensions == 0:
            y += p_size
            x = 0
        im = Image.open(StringIO.StringIO(images[i]))
        print "Write %d at (%d, %d)" % (i, x, y)
        new_image.paste(im, (x, y))
        x += p_size

    new_image.save("wallstreet.png")

def chunk(it, n):
    return [it[i:i+n] for i in range(0, len(it), n)]

if __name__ == "__main__":
    main()