import pyautogui as pyauto
import time
start_time = time.time()

pos_1 = (196, 682)
pos_2 = (202, 513)
pos_3 = (340, 781)

pos_4 = (174, 541)

pos_5 = (362, 780)
pos_6 = (196, 779)

for ii in range(6):
    for i in range(10):
        time.sleep(1)
        pyauto.moveTo(pos_1)

        for i in range(8):
            pyauto.click()
            time.sleep(1)

        pyauto.moveTo(pos_2)
        pyauto.click()

        time.sleep(1)

        pyauto.moveTo(pos_3)
        pyauto.click()

        time.sleep(2)

        time.sleep(2)
        pyauto.moveTo(pos_4)
        pyauto.click()

        pyauto.moveTo(pos_5)
        pyauto.click()

        time.sleep(15)
        pyauto.moveTo(pos_6)
        pyauto.click()
        time.sleep(1)
    time.sleep(15)
    print("done")
    

print("--- %s seconds ---" % (time.time() - start_time))