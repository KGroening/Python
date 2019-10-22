#! python3
import pyautogui
import time

#! Open Oracle

pyautogui.moveTo(99, 1002)
pyautogui.click(button='left')
time.sleep(0.5)
pyautogui.moveTo(103, 931)
pyautogui.click(button='left')
pyautogui.hotkey('ctrl', 'home')
time.sleep(0.7)

#! Copy SR number

pyautogui.moveTo(289, 207)
pyautogui.click(button='left', clicks=2)
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'c')

#! Open Incontact Paste Sr number

pyautogui.moveTo(99, 1002)
pyautogui.click(button='left')
time.sleep(0.5)
pyautogui.moveTo(64, 957)
pyautogui.click(button='left')
time.sleep(0.5)
pyautogui.moveTo(52,  753)
pyautogui.click(button='left')
time.sleep(0.5)
pyautogui.moveTo(191, 679)
pyautogui.click(button='left')
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.moveTo(101, 592)
pyautogui.click(button='left')
time.sleep(0.2)
pyautogui.click(button='left')
time.sleep(0.5)
pyautogui.moveTo(97, 717)
pyautogui.click(button='left')
