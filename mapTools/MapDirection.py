class MapDirection:
   
   INVALID_DIRECTION:int = -1
   
   DEFAULT_DIRECTION:int = 1
   
   MAP_ORTHOGONAL_DIRECTIONS_COUNT:int = 4
   
   MAP_CARDINAL_DIRECTIONS_COUNT:int = 4
   
   MAP_INTER_CARDINAL_DIRECTIONS_COUNT:int = 8
   
   MAP_INTER_CARDINAL_DIRECTIONS_HALF_COUNT:int = 4
   
   EAST:int = 0
   
   SOUTH_EAST:int = 1
   
   SOUTH:int = 2
   
   SOUTH_WEST:int = 3
   
   WEST:int = 4
   
   NORTH_WEST:int = 5
   
   NORTH:int = 6
   
   NORTH_EAST:int = 7
   
   MAP_CARDINAL_DIRECTIONS:list = [0,2,4,6]
   
   MAP_ORTHOGONAL_DIRECTIONS:list = [1,3,5,7]
   
   MAP_DIRECTIONS:list = [0,1,2,3,4,5,6,7]
   
   @classmethod
   def isValidDirection(cls, param1:int) -> bool:
      if param1 >= 0:
         return param1 <= 7
      return False
   
   @classmethod
   def getOppositeDirection(cls, param1:int) -> int:
      return param1 ^ 4
   
   @classmethod
   def isCardinal(cls, param1:int) -> bool:
      return (param1 & 1) == 0
   
   @classmethod
   def isOrthogonal(cls, param1:int) -> bool:
      return (param1 & 1) == 1
