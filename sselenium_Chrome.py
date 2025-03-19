import csv

import keyboard
import pyautogui, sys
from selenium import webdriver
import time
from pathlib import Path
from sneakysnek.recorder import Recorder
from sneakysnek import keyboard_event

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

with open("./new_file.csv", 'w', newline='') as file:
    fieldnames = ["event", "timestamp","mouse_x", "mouse_y"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

def write_in_file (output):
    if type(output.event) is keyboard_event.KeyboardEvents:
        with open("./new_file.csv", 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({
                "event" : str(output.keyboard_key),
                "timestamp" : str(output.timestamp)
            })
    else:
        with open("./new_file.csv", 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({
                "event": str(output.event),
                "timestamp": str(output.timestamp),
                "mouse_x": str(output.x),
                "mouse_y": str(output.y)
            })

driver.get("https://www.python.org")
recorder = Recorder.record(write_in_file)


print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')
    #sys.exit(0)

"""try:
    while True:
        if keyboard.is_pressed('q'):  # Exit on 'q' key press
            print("\nExiting...")
            break
    time.sleep(60)
except KeyboardInterrupt:
    print('\n')
    #sys.exit(0)
"""


recorder.stop()
