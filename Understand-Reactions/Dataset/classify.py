from visionx import detect_joy_file
import os

IMAGE_EXTENSIONS = ['jpeg', 'jpg', 'png']
dir = 'Unconfident/Thumbnails/'

if __name__ == '__main__':
    for filename in os.listdir(dir):
        extension = filename.split('.').pop()
        if extension in IMAGE_EXTENSIONS:
            with open( dir+filename, 'rb') as file:
                response = detect_joy_file(file)
                if response:
                    print(', '.join(list(map(str, [filename, response['joy'], response['anger'],response['surprise'],response['sorrow']]))))
                else:
                    print(filename)
