# checkout  default python modules: https://docs.python.org/3/py-modindex.html
from random import random, randint, choice

# get random Int
randomVal = randint(10,200)
# to get random flot val use random
print(f'got integer {randomVal}')
defaultArray = [10,20,30, 'ten', 'one', 'three']
print(f'Pick from Array {choice(defaultArray)}')