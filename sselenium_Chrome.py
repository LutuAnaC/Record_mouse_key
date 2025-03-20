import csv
import threading
import keyboard
import pyautogui, sys
from keyboard import KeyboardEvent
from selenium import webdriver
import time
from pathlib import Path
from sneakysnek.recorder import Recorder
from sneakysnek import keyboard_event
from pynput import mouse, keyboard
import mouse
import keyboard

from record_key import keyboard_events

mouse_events = []
mouse.hook(mouse_events.append)
#mouse.unhook(mouse_events.append)
driver = webdriver.Chrome()

with open("./new_file.csv", 'w', newline='') as file:
    fieldnames = ["event", "timestamp","mouse_x", "mouse_y"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

def write_in_file (output):
    if isinstance(output, KeyboardEvent):
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

'''k_thread = threading.Thread(target = lambda :keyboard.play(keyboard_events))
k_thread.start()

m_thread = threading.Thread(target = lambda :mouse.play(mouse_events))
m_thread.start()'''

recorder = Recorder.record(write_in_file)
time.sleep(60)

'''k_thread.join() 
m_thread.join()'''


recorder.stop()




