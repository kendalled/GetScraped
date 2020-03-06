# Checks mouse position on windows
import pyautogui as pa 
import time
while True:
    try:
      pa.moveTo(2563, 171, duration=.25)
      pa.click()
      pa.moveRel(10, 0, duration=.25)
      for i in range(12):
        pa.moveRel(0, 50, duration=0.5)
        time.sleep(3)
      time.sleep(8)

    except KeyboardInterrupt:
        print('Stopping...\n')
        break
