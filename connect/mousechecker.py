# Checks mouse position on windows
import pyautogui as pa 

while True:
    try:
        print(pa.position())

    except KeyboardInterrupt:
        print('Stopping...\n')
        break
