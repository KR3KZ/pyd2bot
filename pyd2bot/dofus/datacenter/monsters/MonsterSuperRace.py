               
from pyd2bot.gameData.IdAccessors import IdAccessors


class MonsterSuperRace(IDataCenter):
   
   MODULE:str = "MonsterSuperRaces"
   
   idAccessors:IdAccessors = IdAccessors(getMonsterSuperRaceById,getMonsterSuperRaces)
      
   
   id:int
   
   nameId:int
   
   _name:str
   
   def __init__(self):
      super().__init__()
   
   def getMonsterSuperRaceById(self, id:int) -> MonsterSuperRace:
      return GameData.getObject(MODULE,id)
   
   def getMonsterSuperRaces(self) -> list:
      return GameData.getObjects(MODULE)
   
   @property
   def name(self) -> str:
      if not self._name:
         self._name = I18n.getText(self.nameId)
      return self._name
