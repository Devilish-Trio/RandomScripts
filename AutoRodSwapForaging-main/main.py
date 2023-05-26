import pyautogui
import time
import random
import mouse

def random_delay():
    delay = round(random.uniform(0.1, 0.4), 2)
    print(f"Delay: {delay} seconds")
    time.sleep(delay)

def perform_actions():
    # Press the number 2 on the keyboard
    pyautogui.press('2')
    random_delay()

    # Perform a right click
    pyautogui.rightClick()
    random_delay()

    # Press the number 1 on the keyboard
    pyautogui.press('1')

# Bind the middle mouse button click event to the perform_actions function
mouse.on_middle_click(perform_actions)

# Keep the main thread alive with a while True loop
while True:
    time.sleep(1)
