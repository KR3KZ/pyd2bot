from pyd2bot.gameData.reader.map import RawMap


class Map(RawMap):
	WIDTH = 14
	HEIGHT = 20 # 40 pour l'ancienne version du pathfinder
	RIGHT = 0
	DOWN_RIGHT = 1
	DOWN = 2
	DOWN_LEFT = 3
	LEFT = 4
	UP_LEFT = 5
	UP = 6
	UP_RIGHT = 7

	def __init__(self):
		super().__init__()
	
	def getNeighbourMapFromDirection(self, direction:int) -> int:
		if direction == self.LEFT: 
			return self.leftNeighbourId
		elif direction == self.RIGHT: 
			return self.rightNeighbourId
		elif direction == self.UP:
			return self.topNeighbourId
		elif direction == self.DOWN:
			return self.bottomNeighbourId
	
	def directionToString(self, direction:int) -> str:
		if direction == self.LEFT:
			return "left"
		elif direction == self.RIGHT:
			return "right"
		elif direction == self.UP:
			return "up"
		elif direction == self.DOWN:
			return "down"
		elif direction == self.DOWN_LEFT:
			return "down and left"
		elif direction == self.DOWN_RIGHT:
			return "down and right"
		elif direction == self.UP_LEFT:
			return "up and left"
		elif direction == self.UP_RIGHT:
			return "up and right"
	
	def __str__(self):
		mp = MapPosition.getMapPositionById(self.id)
		return self.id + " [" + mp.posX + ", " + mp.posY + "]"