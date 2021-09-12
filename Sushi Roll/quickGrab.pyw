
# Imports PIL module
import PIL
from PIL import ImageGrab
import os
import time

pad_x = 352
pad_y = 135
 
def screenGrab():
    box = (pad_x, pad_y, pad_x+639, pad_y+479)
    im = ImageGrab.grab(box)
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
 	return im

def main():
    screenGrab()
 
if __name__ == '__main__':
    main()


    #352 x
    #135 y

    #991 x
    #614 y