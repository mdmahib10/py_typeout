import time
import pyautogui
import random

def type_out(text, wpm=90):
    chars_per_minute = wpm * 5
    delay = 60 / chars_per_minute  # seconds per character

    for char in text:
        pyautogui.typewrite(char)
        if char != '\n':
            time.sleep(delay)

    
if __name__ == "__main__":
    input_text = input("Enter text to type out: ")
    print("You have 5 seconds to focus the target text box...")
    time.sleep(5)
    
    type_out(input_text, wpm= 120)