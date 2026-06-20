import pyautogui
from time import sleep

def main():
    x , y = pyautogui.locateCenterOnScreen('quequierescrear.png' , confidence=0.9)

    with open("366 prompts copy.txt", "r") as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if "CGI" in line:
            print(line)
            pyautogui.click(x , y)
            sleep(1)
            pyautogui.write(line)
            sleep(3)
            pyautogui.press('enter')
            sleep(5)
            lines.pop(i) 
            break

    with open("366 prompts copy.txt", "w") as f:
        f.writelines(lines)

if __name__ == '__main__':
    main()