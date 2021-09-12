import pyautogui
import win32gui
from PIL import Image, ImageOps, ImageGrab
from numpy import *
import os
import time

def tupleSubtract(test_tup1, test_tup2):
    res = tuple(map(lambda i, j: i - j, test_tup1, test_tup2))
    return res

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
    time.sleep(1)
    pyautogui.press('esc')
    time.sleep(4)
    click(Cord.miner_play_button)
    time.sleep(12)
    click(Cord.got_it_button_1)
    time.sleep(12)
    click(Cord.got_it_button_2)
    time.sleep(15)
    click(Cord.lets_go_button)

class Color:
    shop_one = (238, 192, 71)

    mine = (1, 1, 1)

    earth_tab = (1, 1, 1)
    moon_tab = (1, 1, 1)

    upgrade_one = (248, 233, 189)
    upgrade_two = (236, 225, 185)
    upgrade_three = (237, 226, 185)

    shop_one = (212, 230)
    shop_two = (200, 220)
    shop_three = (200, 215)
    shop_four = (213, 230)
    shop_five = (213, 230)
    shop_six = (213, 230)

class Cord:
    play_button_1 = (749, 452)
    play_button_2 = (747, 476)

    miner_play_button = (494, 559)
    got_it_button_1 = (464, 559)
    got_it_button_2 = (493, 619)
    got_it_button_2 = (493, 619)
    lets_go_button = (473, 619)

    mine = (267, 425)

    earth_tab = (390, 13)
    moon_tab = (436, 7)

    open_menu = (34,322)

    upgrade_tab = (624, 175)
    upgrade_one = (841, 239)
    upgrade_two = (845, 287)
    upgrade_three = (836, 340)
    upgrade_four = (842, 388)

    shop_tab = (546, 176)
    shop_one = (558, 297)
    shop_two = (732, 299)
    shop_three = (558, 430)
    shop_four = (734, 428)
    shop_five = (558, 561)
    shop_six = (733, 560)

def upgradeDoge():
    click(Cord.upgrade_tab)
    time.sleep(0.5)
    click(Cord.upgrade_four)
    time.sleep(0.5)
    click(Cord.upgrade_three)
    time.sleep(0.5)
    click(Cord.upgrade_two)
    time.sleep(0.5)
    click(Cord.upgrade_one)

def storeDoge():
    #if colors are not upgradable then skip them
    click(Cord.shop_tab)
    time.sleep(1)

    while True:
        im = ImageOps.grayscale(ImageGrab.grab())
        time.sleep(0.5)
        if im.getpixel(Cord.shop_six) in range(Color.shop_six[0], Color.shop_six[1]):
            click(Cord.shop_six)
        elif im.getpixel(Cord.shop_five) in range(Color.shop_five[0], Color.shop_five[1]):
            click(Cord.shop_five)
        elif im.getpixel(Cord.shop_four) in range(Color.shop_four[0], Color.shop_four[1]):
            click(Cord.shop_four)
        elif im.getpixel(Cord.shop_three) in range(Color.shop_three[0], Color.shop_three[1]):
            click(Cord.shop_three)
            print(im.getpixel(Cord.shop_three))
        elif im.getpixel(Cord.shop_two) in range(Color.shop_two[0], Color.shop_two[1]):
            click(Cord.shop_two)
        elif im.getpixel(Cord.shop_one) in range(Color.shop_one[0], Color.shop_one[1]):
            click(Cord.shop_one)
        else:
            break
    
def shopEarthDoge():
    print("shop earth doge")

def runPlanet():
    print("click a bunch")

def clickDoge():
    for i in range(0, 300):
        click(Cord.mine)

def playDogeMiner():
    startGame()
    for i in range(0, 10):
        clickDoge()
        storeDoge()
        if i % 3:
            upgradeDoge()
        time.sleep(5)
    getCords()

if __name__ == "__main__":
    playDogeMiner()