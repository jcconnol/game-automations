import DogeMiner.index as dm
import SlapTheMonkey.index as slm
import GunBlood.index as gb
import GameHelper.gameSetup as gs

def main():
	while True:
		gs.printOptions()

		game_choice = input("Choose what game to autoplay: ")

		if game_choice == "dcm":
			gs.setupGame("https://www.crazygames.com/game/doge-miner")
			dm.playDogeMiner()
		elif game_choice == "stm":
			gs.setupGame("https://www.crazygames.com/game/slap-the-monkey")
			slm.playSlapMonkey()
		elif game_choice == "gb":
			gs.setupGame("https://www.crazygames.com/game/gunblood")
			gb.playGunBlood()
		elif game_choice == "q" or game_choice == "quit":
			print("break")
		else:
			print("That is not a valid option")

if __name__ == "__main__":
	main()