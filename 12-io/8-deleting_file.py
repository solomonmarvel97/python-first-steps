import os

try:
    os.remove('marvelous.txt')
except FileNotFoundError as e:
    print(e)