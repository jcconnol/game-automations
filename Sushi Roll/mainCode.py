import win32api, win32con
import os
import time
import PIL
from PIL import ImageGrab
from PIL import ImageOps
from numpy import *

pad_x = 352
pad_y = 135
 
def screenGrab():
	box = (pad_x, pad_y, pad_x+639, pad_y+479)
	im = ImageGrab.grab(box)
	#im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
	return im

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print("Click.")

def mousePos(cord):
    win32api.SetCursorPos((pad_x + cord[0], pad_y + cord[1]))

def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - pad_x
    y = y - pad_y
    print(x,y)

def startGame():
    #location of first menu
    mousePos((304, 206))
    leftClick()
    time.sleep(.1)
     
    #location of second menu
    mousePos((355, 394))
    leftClick()
    time.sleep(.1)
     
    #location of third menu
    mousePos((327, 399))
    leftClick()
    time.sleep(.1)

class Cord:
    f_shrimp = (34,322)
    f_rice = (86, 324)
    f_nori = (35, 376)
    f_roe = (93, 379)
    f_salmon = (37, 428)
    f_unagi = (92, 430)

    #-----------------------------------    
     
    phone = (583, 371)
 
    menu_toppings = (549, 274)
     
    t_shrimp = (492, 218)
    t_nori = (572, 217)
    t_roe = (485, 274)
    t_salmon = (564, 271)
    t_unagi = (490, 328)
    t_exit = (592, 334)
 
    menu_rice = (550, 292)
    buy_rice = (544, 273)
     
    delivery_norm = (510, 664)

def clear_tables():
    mousePos((83, 202))
    leftClick()
 
    mousePos((177, 203))
    leftClick()
 
    mousePos((281, 200))
    leftClick()
 
    mousePos((384, 206))
    leftClick()
 
    mousePos((484, 201))
    leftClick()
 
    mousePos((584, 199))
    leftClick()
    time.sleep(1)

def foldMat():
    mousePos((Cord.f_rice[0]+128, Cord.f_rice[1]+60)) 
    leftClick()
    time.sleep(.1)

'''
Recipes:
 
    onigiri
        2 rice, 1 nori
     
    caliroll:
        1 rice, 1 nori, 1 roe
         
    gunkan:
        1 rice, 1 nori, 2 roe
'''

def makeFood(food):
	if food == 'caliroll':
		print('Making a caliroll')
		mousePos(Cord.f_rice)
		leftClick()
		time.sleep(.05)
		mousePos(Cord.f_nori)
		leftClick()
		time.sleep(.05)
		mousePos(Cord.f_roe)
		leftClick()
		time.sleep(.1)
		foldMat()
		time.sleep(1.5)
     
	elif food == 'onigiri':
		print('Making a onigiri')
		mousePos(Cord.f_rice)
		leftClick()
		time.sleep(.05)
		mousePos(Cord.f_rice)
		leftClick()
		time.sleep(.05)
		mousePos(Cord.f_nori)
		leftClick()
		time.sleep(.1)
		foldMat()		 
		time.sleep(1.5)
 
	elif food == 'gunkan':
		print('Making a gunkan')
		mousePos(Cord.f_rice)
		leftClick()
		time.sleep(.05)
		mousePos(Cord.f_nori)
		leftClick()
		time.sleep(.05)
		mousePos(Cord.f_roe)
		leftClick()
		time.sleep(.05)
		mousePos(Cord.f_roe)
		leftClick()
		time.sleep(.1)
		foldMat()
		time.sleep(1.5)

def buyFood(food):

    if food != '' and food != None:
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()

    if food == 'rice':
        mousePos(Cord.menu_rice)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        if s.getpixel(Cord.buy_rice) != (109, 123, 127):
            print 'rice is available'
            mousePos(Cord.buy_rice)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print 'rice is NOT available'
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)
             
 
             
    if food == 'nori':
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        print 'test'
        time.sleep(.1)
        if s.getpixel(Cord.t_nori) != (94, 49, 8):
            print 'nori is available'
            mousePos(Cord.t_nori)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print 'nori is NOT available'
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)
 
    if food == 'roe':
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
         
        time.sleep(.1)
        if s.getpixel(Cord.t_roe) != (127, 61, 0):
            print 'roe is available'
            mousePos(Cord.t_roe)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print 'roe is NOT available'
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

def checkFood():
    for i, j in foodOnHand.items():
        if i == 'nori' or i == 'rice' or i == 'roe':
            if j <= 4:
                print '%s is low and needs to be replenished' % i
                buyFood(i)

def main():
    foodOnHand = {'shrimp':5,
              'rice':10,
              'nori':10,
              'roe':10,
              'salmon':5,
              'unagi':5}
    im = screenGrab()
    print(im.getpixel(Cord.t_nori))
    print(im.getpixel(Cord.t_roe))
    print(im.getpixel(Cord.t_salmon))
    print(im.getpixel(Cord.t_shrimp))
    print(im.getpixel(Cord.t_unagi))
    print(im.getpixel(Cord.buy_rice))

    (94, 49, 8)
    (33, 30, 11)
    (109, 123, 127)
    (127, 127, 127)
    (127, 71, 47)
    (109, 123, 127)

if __name__ == '__main__':
    main()