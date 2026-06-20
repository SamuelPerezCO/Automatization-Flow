import pyautogui
from time import sleep
import sys

def countdown(t):
    while t:
        mins , secs = divmod(t,60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer , end="\r")
        sleep(1)
        t -= 1
    print("00:00\nTimer completed!")

def analyze_text(file_path):
    try:
        with open(file_path , 'r') as file:
            char_count = 0
            line_count = 0

            for line in file:
                line_count += 1
                char_count += len(line)

            print("File analysis report:")
            print("Character count: " , char_count)

            if char_count != 0:
                send_prompt()
            else:
                sys.exit()
    except FileNotFoundError:
        print("File not found!")

def send_prompt():
    try:
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

        countdown(180)
        analyze_text("366 prompts copy.txt")
    except Exception as e:
        print(f"There was an error {e}")

if __name__ == '__main__':
    send_prompt()