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
    time.sleep(1)
    click(Cord.play_button_2)
    time.sleep(7)

class Cord:
    initial_hand = (743, 396)

    right_side_limit = (970, 416)
    left_side_limit = (100, 416)

    play_button_1 = (749, 452)
    play_button_2 = (747, 476)

def playSlapMonkey():
    startGame()
    while True:
        click(Cord.initial_hand)
        time.sleep(1)
        pyautogui.dragTo(Cord.right_side_limit[0], Cord.right_side_limit[1], button='left')
        time.sleep(1)
        pyautogui.moveTo(Cord.left_side_limit[0], Cord.left_side_limit[1])
        time.sleep(10)

if __name__ == "__main__":
    playSlapMonkey()