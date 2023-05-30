import random
import time

list = ["s","u", "o", "n", "z", "w"]

count = 1

for i in range(len(list)):
    count = count * (i + 1)

print(count)