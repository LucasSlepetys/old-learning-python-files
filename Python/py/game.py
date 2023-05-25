import random
import time

animal = input("Pick a animal: ")
time.sleep(2)

print("Picking number:")
n_color = random.randint(1, 3)
#! Text
if n_color == 1:
    color = "red"
elif n_color == 2:
    color ="blue"
elif n_color == 3:
    color = "orange"
time.sleep(1)
print("Your first number is: ",n_color)
time.sleep(2)
print("Picking number:")
n_items = random.randint(1, 3)
#! Text
if n_items == 1:
    items = "square"
elif n_items == 2:
    items ="circle"
elif n_items == 3:
    items = "rectangle"
print("Your second number is: ",n_items)
time.sleep(2)
print("Picking number:")
n_part = random.randint(1, 3)
#! Text
if n_part == 1:
    part = "head"
elif n_part == 2:
    part ="foot"
elif n_part == 3:
    part = "hand"
time.sleep(2)
print("Your thrird number is: ",n_part)
print("Draw a ", color, " ", items, " on your ", animal, " ", part)