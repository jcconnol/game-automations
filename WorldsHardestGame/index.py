import pyautogui
import win32gui
from PIL import Image, ImageOps, ImageGrab
from numpy import *
import os
import time

def click(coordnates):
    pyautogui.click(coordnates[0], coordnates[1])

def getCords():
    currentMouseX, currentMouseY = pyautogui.position()
    print(currentMouseX)
    print(currentMouseY)

def startGame():
    #location of first and second menus
    click(Cord.play_button_1)
    time.sleep(5)
    click(Cord.play_button_2)
    time.sleep(10)
    click(Cord.play_button_3)
    time.sleep(1)
    click(Cord.play_button_4)
    time.sleep(4)

class Cord:
    play_button_1 = (749, 452)
    play_button_2 = (500, 353)
    play_button_3 = (229, 467)
    play_button_4 = (591, 526)

def playWorldsHardestGame():
    startGame()
    getCords()

if __name__ == "__main__":
    playWorldsHardestGame()
