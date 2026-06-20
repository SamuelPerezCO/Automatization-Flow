import pyautogui
import time 

x , y = pyautogui.locateCenterOnScreen('quequierescrear.png' , confidence=0.9)
# pyautogui.click(x , y)
# time.sleep(5)

# Read all lines
with open("366 prompts copy.txt", "r") as f:
    lines = f.readlines()

# Find and print the first match, then remove it
for i, line in enumerate(lines):
    if "CGI" in line:
        print(line)
        pyautogui.click(x , y)
        time.sleep(1)
        pyautogui.write(line)
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(5)
        lines.pop(i)  # Delete the matched line
        break

# Write the remaining lines back to the file
with open("366 prompts copy.txt", "w") as f:
    f.writelines(lines)