import pyautogui 
import time

time.sleep(1)
pyautogui.click()
# for i in range(72):
#     pyautogui.hotkey('command', 'd')
#     pyautogui.press("'")
#     pyautogui.press('down')

for i in range(250):
    # pyautogui.hotkey('command', 'd')
    pyautogui.press(",")
    pyautogui.press('down')
    pyautogui.hotkey('command', 'right')