import pyautogui as pyauto
import time

pos_1 = (1411, 27)
pos_2 = (1309, 220)
pos_3 = (1293, 256)
pos_4 = (1292, 296)
pos_5 = (1140, 290)

time.sleep(5)
for i in range(20):
    pyauto.moveTo(pos_1)
    pyauto.click()

    time.sleep(1)

    pyauto.moveTo(pos_2)
    pyauto.click()

    time.sleep(1)

    pyauto.moveTo(pos_1)
    pyauto.click()

    time.sleep(1)

    pyauto.moveTo(pos_3)
    pyauto.click()

    time.sleep(1)

    pyauto.moveTo(pos_1)
    pyauto.click()

    time.sleep(1)

    pyauto.moveTo(pos_4)
    pyauto.click()

    time.sleep(1)

    pyauto.moveTo(pos_5)
    pyauto.click()
    time.sleep(1)
    pyauto.click()
    pyauto.click()

    time.sleep(1)
    print("done!")