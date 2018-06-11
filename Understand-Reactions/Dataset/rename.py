import os

if __name__ == '__main__':
    for i, filename in enumerate(os.listdir('.')):
        extension = filename.split('.').pop()
        if extension != 'py':
            os.rename(filename, f'{i}.{extension}')
