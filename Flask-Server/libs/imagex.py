from PIL import Image
import io


def save_small(file, width, height, temp_dst):
    img = Image.open(io.BytesIO(file.read()))
    img.thumbnail((width, height))
    img.save(temp_dst, optimize=True,quality=95)

if __name__ == '__main__':
    with open('test.png', 'rb') as f:
        save_small(f, 300,200, 'png')
