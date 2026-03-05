# py_typeout
A lightweight Python utility using pyautogui to simulate human typing. Automatically type out any text block into your active window at a customizable Words Per Minute (WPM) rate.
# ⌨️ TypeOut

A simple, lightweight Python tool that simulates keystrokes to type out any given text at a customizable Words Per Minute (WPM) rate. Whether you need to automate repetitive data entry, simulate user input for testing, or just want to sit back while your computer does the typing, TypeOut has you covered.

## ✨ Features
* **Customizable Speed:** Set your exact WPM, and the script calculates the exact millisecond delay between each keystroke.
* **Focus Delay:** Includes a built-in 5-second countdown, giving you plenty of time to click into your target window, terminal, or application before the typing begins.
* **Cross-Platform:** Powered by `pyautogui`, it works seamlessly across your OS of choice.

## 🚀 Getting Started

### Prerequisites
Make sure you have Python installed, along with the required library:
```bash
pip install pyautogui
```
### Running
Run this command and paste your text in the terminal:
```bash
python typeout.py
