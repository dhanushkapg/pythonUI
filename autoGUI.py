import pyautogui
screenWidth, screenHeight = pyautogui.size() # screen width and height
print(screenWidth,screenHeight)
x,y = pyautogui.position() # current position of the mouse pointer
print(x,y)
pyautogui.typewrite('Hello, world!', interval=0.25) # automatic typing on given cursour location
pyautogui.move(600,500)
pyautogui.click()


