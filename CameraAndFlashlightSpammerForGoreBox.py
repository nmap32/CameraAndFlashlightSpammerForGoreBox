import pyautogui
import time
import keyboard

print("To make it work go to GoreBox and open esc menu, make sure that the creator mode is enabled. And go to Entities and go to tab called Items / Specials and then just close the esc menu and then make sure that you have empty inventory and just press Insert and enjoy")

def teleport_and_click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()

def main():
    while True:
        if keyboard.is_pressed('insert'):
            keyboard.press_and_release('esc')
            time.sleep(0.1)
            teleport_and_click(607, 316)
            time.sleep(0.1)
            teleport_and_click(830, 308)
            time.sleep(0.1)
            teleport_and_click(607, 316)
            time.sleep(0.1)
            teleport_and_click(830, 308)
            time.sleep(0.1)
            teleport_and_click(607, 316)
            time.sleep(0.1)
            teleport_and_click(830, 308)
            time.sleep(0.1)
            keyboard.press_and_release('esc')
            time.sleep(0.1)
            keyboard.press_and_release('2')
            time.sleep(0.1)
            keyboard.press_and_release('x')
            time.sleep(0.1)
            keyboard.press_and_release('2')
            time.sleep(0.1)
            keyboard.press_and_release('x')
            time.sleep(0.1)
            keyboard.press_and_release('2')
            time.sleep(0.1)
            keyboard.press_and_release('x')
            time.sleep(0.1)
            keyboard.press_and_release('2')
            time.sleep(0.1)
            keyboard.press_and_release('x')
            time.sleep(0.1)
            keyboard.press_and_release('2')
            time.sleep(0.1)
            keyboard.press_and_release('x')
            time.sleep(0.1)
            keyboard.press_and_release('2')
            time.sleep(0.1)
            keyboard.press_and_release('x')
            time.sleep(0.1)
        else:
            continue

if __name__ == "__main__":
    main()