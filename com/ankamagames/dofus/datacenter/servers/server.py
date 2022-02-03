from com.ankamagames.dofus.datacenter.servers.ServerCommunity import ServerCommunity
from com.ankamagames.dofus.datacenter.servers.ServerGameType import ServerGameType
from com.ankamagames.dofus.datacenter.servers.ServerPopulation import ServerPopulation
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.data.I18n import I18n
from com.ankamagames.dofus.types.IdAccessors import IdAccessors
from com.ankamagames.jerakine.data.GameData import GameData
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter

logger = Logger(__name__)

class Server(IDataCenter):
   
   
   MODULE:str = "Servers"
   
   id:int
   
   nameId:int
   
   commentId:int
   
   openingDate:float
   
   language:str
   
   populationId:int
   
   gameTypeId:int
   
   communityId:int
   
   restrictedToLanguages:list[str]
   
   monoAccount:bool
   
   _name:str
   
   _comment:str
   
   _gameType:ServerGameType
   
   _community:ServerCommunity
   
   _population:ServerPopulation
   
   def __init__(self):
      super().__init__()
   
   @staticmethod
   def getServerById(id:int) -> 'Server':
      return GameData.getobject(Server.MODULE,id)
   
   @staticmethod
   def getServers(self) -> list:
      return GameData.getobjects(Server.MODULE)
   
   idAccessors:IdAccessors = IdAccessors(getServerById,getServers)
   
   @property
   def name(self) -> str:
      if not self._name:
         self._name = I18n.getText(self.nameId)
      return self._name
   
   @property
   def comment(self) -> str:
      if not self._comment:
         self._comment = I18n.getText(self.commentId)
      return self._comment
   
   @property
   def gameType(self) -> ServerGameType:
      if not self._gameType or self._gameType.id != self.gameTypeId:
         self._gameType = ServerGameType.getServerGameTypeById(self.gameTypeId)
      return self._gameType
   
   @property
   def community(self) -> ServerCommunity:
      if not self._community or self._community.id != self.communityId:
         self._community = ServerCommunity.getServerCommunityById(self.communityId)
      return self._community
   
   @property
   def population(self) -> ServerPopulation:
      if not self._population:
         self._population = ServerPopulation.getServerPopulationById(self.populationId)
      return self._population
