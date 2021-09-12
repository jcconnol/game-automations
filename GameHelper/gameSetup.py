import pyautogui
import pygetwindow as gw
import webbrowser
import time

def setupGame(url):
	#launch browser and put in top left corner, make window height and width of screen
	screen_width, screen_height = pyautogui.size()
	print(screen_height)
	print(screen_width)
	webbrowser.open_new(url)
	time.sleep(3) #need to wait to change to browser being active window
	game_window = gw.getActiveWindow()
	game_window.move(0,0)
	game_window.maximize()

def printOptions():
	print("Doge coin miner: dcm")
	print("Slap the monkey: stm")
	print("Gun Blood: gb")
	print("Worlds Hardest Game: whg")
