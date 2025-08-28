# from time import sleep
import time

print("start")
time.sleep(2)
print("finish",time.time())

import math_utils 

print(math_utils.square(4))

from math_utils import cube
print(cube(3))