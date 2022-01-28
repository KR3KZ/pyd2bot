from com.ankamagames.dofus.types.idAccessors import IdAccessors
from com.ankamagames.jerakine.data import GameData, I18n
from com.ankamagames.jerakine.interfaces.iDatacenter import IDataCenter


class MonsterSuperRace(IDataCenter):
   
   MODULE:str = "MonsterSuperRaces"
   id:int
   nameId:int
   _name:str
   
   def __init__(self):
      super().__init__()
   
   @staticmethod
   def getMonsterSuperRaceById(id:int) -> 'MonsterSuperRace':
      return GameData.getObject(MonsterSuperRace.MODULE, id)
   
   @staticmethod
   def getMonsterSuperRaces() -> list:
      return GameData.getObjects(MonsterSuperRace.MODULE)
   
   @property
   def name(self) -> str:
      if not self._name:
         self._name = I18n.getText(self.nameId)
      return self._name

   
   idAccessors:IdAccessors = IdAccessors(getMonsterSuperRaceById,getMonsterSuperRaces)