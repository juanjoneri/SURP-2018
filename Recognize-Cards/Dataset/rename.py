import os
import sys

def remane(directory, prefix, extension):
    for i, filename in enumerate(os.listdir(directory)):
        file_extension = filename.split('.').pop()
        if file_extension == extension:
            os.rename(directory + filename, f'{directory}{prefix}-{i}.{extension}')

if __name__ == '__main__':
    try:
        directory, prefix, extension = sys.argv[1], sys.argv[2], sys.argv[3]
        remane(directory, prefix, extension)
    except:
        print('directory', 'prefix', 'extension')
