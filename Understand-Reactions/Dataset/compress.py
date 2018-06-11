from PIL import Image
import glob, os

size = 256, 256

if __name__ == '__main__':
    for infile in glob.glob("*.jpg") + glob.glob("*.jpeg"):
        file, ext = os.path.splitext(infile)
        im = Image.open(infile)
        im.thumbnail(size)
        im.save(f'Thumbnails/{file}{ext}', "JPEG")

    for infile in glob.glob("*.png"):
        file, ext = os.path.splitext(infile)
        im = Image.open(infile)
        im.thumbnail(size)
        im.save(f'Thumbnails/{file}{ext}', "PNG")
