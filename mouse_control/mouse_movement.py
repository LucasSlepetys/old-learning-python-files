import pyautogui as pg

#! Gets size of the screen
size = pg.size()
print(size)

#! Gets position of the mouse
pos_1 = pg.position()
print(pos_1)

#! Mouve mouse to certain position
# pg.moveTo(1440, 0, 4)
# pg.click(324, 61)
pg.click()

pg.hotkey('command', 'v')
#! Click