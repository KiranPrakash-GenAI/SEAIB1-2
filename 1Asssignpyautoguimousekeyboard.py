import pyautogui
import time

def open_google_and_search():
    # Open Run dialog
    pyautogui.hotkey('win', 'r')
    time.sleep(1)

    # Type browser (e.g., chrome)
    pyautogui.write('chrome')
    pyautogui.press('enter')
    time.sleep(3)

    #Click the chrome profile (approximate position - adjust if needed)
    pyautogui.moveTo(689, 659)  # Adjust this position based on your screen resolution
    pyautogui.click()
    time.sleep(3)

    # Type google.com and press enter
    pyautogui.write('https://www.google.com')
    pyautogui.press('enter')
    time.sleep(3)

    # Type "India vs England score"
    pyautogui.write('India vs England score')
    pyautogui.press('enter')
    time.sleep(3)

    # Click the first link (approximate position - adjust if needed)
    pyautogui.moveTo(400, 400)  # Adjust this position based on your screen resolution
    pyautogui.click()
    time.sleep(3)

    # Scroll down
    for _ in range(5):
        pyautogui.scroll(-500)
        time.sleep(1)

# Run the script
open_google_and_search()
