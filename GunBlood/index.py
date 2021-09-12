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
    time.sleep(5)
    click(Cord.play_button_3)
    time.sleep(1)
    click(Cord.play_button_4)
    time.sleep(1)
    click(Cord.choose_char_button)
    time.sleep(1)
    click(Cord.char_continue)

class Cord:
    play_button_1 = (749, 452)
    play_button_2 = (747, 476)
    play_button_3 = (484, 394)
    play_button_4 = (484, 394)

    choose_char_button = (484, 394)
    char_continue = (583, 568)

    chamber = (189, 556)

    head_aim = (263, 325)

    restart_button = (493, 457)

    finish_aim = (779, 432)
    finish_aim_2 = (816, 408)

    next_round_button = (469, 478)

def playGunBlood():
    #startGame()
    #pyautogui.moveTo(Cord.chamber[0], Cord.chamber[1])
    #time.sleep(2.10)
    #click(Cord.head_aim)
    #time.sleep(0.1)
    #click(Cord.finish_aim)
    #time.sleep(0.1)
    #click(Cord.finish_aim_2)
    #time.sleep(0.1)
    #click(Cord.finish_aim)
    #time.sleep(0.1)
    #click(Cord.finish_aim_2)
    #time.sleep(0.1)
    #click(Cord.finish_aim_2)
    time.sleep(0.1)
    click(next_round_button)
    getCords()


if __name__ == "__main__":
    playGunBlood()