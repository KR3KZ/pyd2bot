from com.ankamagames.dofus.types.IdAccessors import IdAccessors
from com.ankamagames.jerakine.data.GameData import GameData
from com.ankamagames.jerakine.data.I18n import I18n
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter
from com.ankamagames.jerakine.logger.Log import Log
from com.ankamagames.jerakine.logger.Logger import Logger
from flash.utils.getQualifiedClassName import getQualifiedClassName

class ServerPopulation(IDataCenter):
   
   MODULE:str = "ServerPopulations"
   
   logger = Logger(__name__)
   
   idAccessors:IdAccessors = IdAccessors(getServerPopulationById,getServerPopulations)
   
   
   id:int
   
   nameId:int
   
   weight:int
   
   _name:str
   
   def __init__(self):
      super().__init__()

   
   @classmethod      
   def getServerPopulationById(cls, id:int) -> 'ServerPopulation':      
   return GameData.getObject(cls.MODULE, id)

   
   @classmethod      
   def getServerPopulations(cls) -> list['ServerPopulation']:      
   return GameData.getObjects(cls.MODULE)

   
   @property
   def name(self) -> str:
      if not self._name:
         self._name = I18n.getText(self.nameId)
      return self._name
