import pyautogui as pg
import time

#! Gets size of the screen
size = pg.size()
print(size)

#! Gets position of the mouse
time.sleep(3)

for i in range(5):
    pos_1 = pg.position()
    print(pos_1)
    time.sleep(2)
