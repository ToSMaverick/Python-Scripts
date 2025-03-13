import pyautogui
import time
import random

while True:
    x, y = pyautogui.position()
    x = x + random.randint(-5,5)
    y = y + random.randint(-5,5)
    pyautogui.moveTo(x,y)
    localtime = time.localtime()
    result = time.strftime("%I:&M:%S %p", localtime)
    print('Moved at ' + str(result) + ' ('  + str(x) + ', ' + str(y) + ')')
    time.sleep(30) 
