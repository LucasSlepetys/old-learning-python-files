import pyautogui as pyauto
import time

pos_1 = (18, 777)
pos_2 = (189, 709)
pos_3 = (353, 780)
x = 0

for ii in range(2):
    for i in range(100):
        x += 1

        pyauto.moveTo(pos_1)
        pyauto.click()

        time.sleep(1)

        pyauto.moveTo(pos_2)
        pyauto.click()

        time.sleep(1)

        pyauto.moveTo(pos_3)
        pyauto.click()

        time.sleep(1)
        print(x)
    time.sleep(10)