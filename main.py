from pathlib import Path
import pyautogui
import time
import pyscreeze
import PIL

__PIL_TUPLE_VERSION = tuple(int(x) for x in PIL.__version__.split("."))
pyscreeze.PIL__version__ = __PIL_TUPLE_VERSION

close_buttons = []
click_buttons = []

# Load images using pathlib
for p in Path().iterdir():
    if p.name.startswith('Click'):
        click_buttons.append(p.name)

for pname in click_buttons:
    close_buttons.append(pname.removeprefix('Click'))

while True:
    for btn, click_btn in zip(close_buttons, click_buttons):
        if pyautogui.locateOnScreen(btn, confidence=0.5) is not None:
            print('Close button detected. Closing...')

            x, y = pyautogui.locateCenterOnScreen(click_btn, confidence=0.5)
            pyautogui.click(x, y)

            time.sleep(5)
            break
            
    time.sleep(10)