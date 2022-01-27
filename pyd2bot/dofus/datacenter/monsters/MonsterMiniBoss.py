            
from pyd2bot.gameData.IdAccessors import IdAccessors


class MonsterMiniBoss:
   
   MODULE:str = "MonsterMiniBoss"  
   
   def getMonsterById(self, id:int) -> 'MonsterMiniBoss':
      return GameData.getObject(MODULE,id)
   
   def getMonsters(self) -> list:
      return GameData.getObjects(MODULE)
   
   idAccessors:IdAccessors = IdAccessors(getMonsterById,getMonsters)
      
   
   id:int
   
   monsterReplacingId:int
   
   def __init__(self):
      super().__init__()
