import os

try:
    os.rename('ellajoyifeoma.txt', 'marvelous.txt')
except FileNotFoundError as e:
    print(e)