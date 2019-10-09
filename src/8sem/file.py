import os

with open('sample.txt', 'w') as f:
    f.write('wdefwf')

with open('sample.txt') as f:
    data = f.read()
    print(data)


def read_file():
    if os.path.exists('sample.txt'):
        f = open('sample.txt')
    try:
        data = f.read()
    finally:
        f.close()
    return data

read_file()